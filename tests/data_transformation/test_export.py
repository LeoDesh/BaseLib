from base_lib.data_transformation.export import (
    export_table_to_csv_txt,
    export_table_to_excel,
    export_table_to_json,
    export_table_to_jsonl,
    export_table_to_sql,
    Table,
)
import pytest
from base_lib.file_loader.load_data import (
    TextFileLoader,
    ExcelFileLoader,
    JSONLineLoader,
    JSONLoader,
    CSVFileLoader,
)
from base_lib.SQL.sql_connection import create_lite_engine
from base_lib.SQL.sql_helper import exec_sql,qry_data
from base_lib.data_transformation.transformation import convert_dataframe_to_table,convert_jsonl_to_table,convert_json_to_table


@pytest.mark.export
def test_text_file_export(tmp_path, table_example):
    table:Table = table_example
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
def test_csv_file_export(tmp_path, table_example):
    table:Table = table_example
    table.transform_data_within_table()
    file_path = tmp_path / "output.csv"
    export_table_to_csv_txt(table, file_path)
    assert file_path.exists()

    loader = CSVFileLoader()
    df = loader.load(file_path, sep=";")
    trg_table = convert_dataframe_to_table(df)
    trg_table.transform_data_within_table()
    assert table == trg_table

@pytest.mark.export
def test_excel_export(tmp_path, table_example):
    table:Table = table_example
    table.transform_data_within_table()
    file_path = tmp_path / "output.xlsx"
    export_table_to_excel(table, file_path,"Target")
    assert file_path.exists()

    loader = ExcelFileLoader()
    df = loader.load(file_path,"Target")
    trg_table = convert_dataframe_to_table(df)
    trg_table.transform_data_within_table()
    assert table == trg_table



@pytest.mark.export
def test_jsonl_export_timestamp(tmp_path, table_example):
    table:Table = table_example
    table.transform_data_within_table()
    file_path = tmp_path / "output.jsonl"
    with pytest.raises(TypeError):
        export_table_to_jsonl(table, file_path)
    

@pytest.mark.export
def test_jsonl_export(tmp_path, data_container_transformation):
    headers = ["Index", "Description", "Value", "Score"]
    table:Table = Table(data_container_transformation,headers,column_types=[int,str,int,float])
    table.transform_data_within_table()
    file_path = tmp_path / "output.jsonl"
    export_table_to_jsonl(table,file_path)
    assert file_path.exists()

    loader = JSONLineLoader()
    data = loader.load(file_path)
    trg_table = convert_jsonl_to_table(data)
    trg_table.column_types = [int,str,int,float]
    trg_table.transform_data_within_table()
    assert table == trg_table


@pytest.mark.export
def test_json_export_no_index(tmp_path, data_container_transformation):
    headers = ["ID", "Description", "Value", "Score"]
    table:Table = Table(data_container_transformation,headers,column_types=[int,str,int,float])
    table.transform_data_within_table()
    file_path = tmp_path / "output.json"
    with pytest.raises(ValueError):
        export_table_to_json(table,file_path)

@pytest.mark.export
def test_json_export(tmp_path, data_container_transformation):
    headers = ["Index", "Description", "Value", "Score"]
    table:Table = Table(data_container_transformation,headers,column_types=[int,str,int,float])
    table.transform_data_within_table()
    file_path = tmp_path / "output.json"
    export_table_to_json(table,file_path)
    assert file_path.exists()

    loader = JSONLoader()
    data = loader.load(file_path)
    trg_table = convert_json_to_table(data)
    trg_table.column_types = [str,int,float,int]
    trg_table.transform_data_within_table()
    trg_table.transform_to_dataframe()
    assert trg_table.columns[0] == table.columns[1]
    assert trg_table.columns[1] == table.columns[2]

@pytest.mark.export
def test_sql_export(table_example):
    engine = create_lite_engine()
    table_name = "Example"
    exec_stmt = f"DROP TABLE IF EXISTS {table_name}"
    exec_sql(exec_stmt,engine)
    table:Table = table_example
    table.transform_data_within_table()
    export_table_to_sql(table,table_name,engine)
    df = qry_data("Select * from Example",engine)
    assert len(df) > 0
