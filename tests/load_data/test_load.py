from load_data import TextFileLoader
import pytest


def test_find_sep(sample_file):
    loader = TextFileLoader()
    text_lines = loader.get_text_lines(sample_file)
    assert "," == loader.find_field_separator(text_lines)


def test_find_sep_fail(modified_file):
    loader = TextFileLoader()
    text_lines = loader.get_text_lines(modified_file)
    with pytest.raises(ValueError):
        loader.find_field_separator(text_lines)


def test_clean_up_line():
    loader = TextFileLoader()
    text = " LineID,ContentID\n"
    assert loader.clean_up_text(text) == "LineID,ContentID"


def test_load_txt(sample_file):
    loader = TextFileLoader()
    content = [["OrderID", "ItemID", "Quantity"], ["1", "4", "15"]]
    assert content == loader.load(sample_file)
