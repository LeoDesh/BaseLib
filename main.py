from LoggerConfig import app_logger,ordinary_logger
from data_transformation.table import Table
from data_transformation.export import export_table_to_csv_txt
from file_loader.load_data import TextFileLoader
from pathlib import Path

def test_text_file_export(tmp_path:Path):
    headers =["ID","Description","Value","Score"] 
    data_container =  [
        (1, "ID", 19640817, "4.42"),
        (5, "User", 1990111, "8.5"),
        (9, "Mister", 19880827, "12.1"),
        (12, "Admin", 20001217, "15.4"),
    ]
    table = Table(data_container,headers)
    file_path = tmp_path / "output.txt"
    export_table_to_csv_txt(table,file_path)
    assert file_path.exists()

    loader = TextFileLoader()
    data =loader.load(file_path)
    loaded_table = Table(data[1:],data[0])
    table.transform_data_within_table()
    loaded_table.transform_data_within_table()
    print(table)
    print(loaded_table)
    print(table==loaded_table)
    #assert table == loaded_table

def main():
    ordinary_logger.info("FirstEntry")
    test_text_file_export(Path(""))

if __name__ == "__main__":
    main()
