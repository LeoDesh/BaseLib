from load_data import TextFileLoader,ExcelFileLoader,CSVFileLoader,JSONLineLoader
from load_helper import clean_up_text,get_file_lines
import pytest


def test_find_sep(sample_file):
    loader = TextFileLoader()
    text_lines = get_file_lines(sample_file)
    assert "," == loader.find_field_separator(text_lines)


def test_find_sep_fail(modified_file):
    loader = TextFileLoader()
    text_lines = get_file_lines(modified_file)
    with pytest.raises(ValueError):
        loader.find_field_separator(text_lines)


def test_clean_up_line():
    text = " LineID,ContentID\n"
    assert clean_up_text(text) == "LineID,ContentID"


def test_load_txt(sample_file):
    loader = TextFileLoader()
    content = [["OrderID", "ItemID", "Quantity"], ["1", "4", "15"]]
    assert content == loader.load(sample_file)


def test_load_excel(excel_file):
    loader = ExcelFileLoader()
    df = loader.load(excel_file,"Main")
    assert df.shape == (3,3)


def test_load_csv(csv_file):
    loader = CSVFileLoader()
    df = loader.load(csv_file,sep=",")
    assert df.shape == (1,3)


def test_load_jsonl(json_file):
    loader = JSONLineLoader()
    data = loader.load(json_file)
    assert len(data) == 2
    for line_dict in data:
        assert line_dict["level"] == "INFO"