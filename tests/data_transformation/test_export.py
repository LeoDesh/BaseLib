from base_lib.data_transformation.export import (
    export_table_to_csv_txt,
    # export_table_to_excel,
    # export_table_to_json,
    # export_table_to_jsonl,
    Table,
)
import pytest
from base_lib.file_loader.load_data import (
    TextFileLoader,
    # ExcelFileLoader,
    # JSONLineLoader,
    # JSONLoader,
    CSVFileLoader,
)

from base_lib.data_transformation.transformation import convert_dataframe_to_table


@pytest.mark.export
def test_text_file_export(tmp_path, data_container_transformation):
    headers = ["ID", "Description", "Value", "Score"]
    table = Table(data_container_transformation, headers)
    table.transform_data_within_table()
    file_path = tmp_path / "output.txt"
    export_table_to_csv_txt(table, file_path)
    assert file_path.exists()

    loader = TextFileLoader()
    data = loader.load(file_path)
    loaded_table = Table(data[1:], data[0])
    loaded_table.transform_data_within_table()
    assert table == loaded_table


@pytest.mark.export
def test_csv_file_export(tmp_path, data_container_transformation):
    headers = ["ID", "Description", "Value", "Score"]
    table = Table(data_container_transformation, headers)
    table.transform_data_within_table()
    file_path = tmp_path / "output.csv"
    export_table_to_csv_txt(table, file_path)
    assert file_path.exists()

    loader = CSVFileLoader()
    df = loader.load(file_path, sep=";")
    trg_table = convert_dataframe_to_table(df)
    trg_table.transform_data_within_table()

    assert table == trg_table
