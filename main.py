from base_lib.logger_setup.constants import app_logger,ordinary_logger
from base_lib.data_transformation.table import Table
from base_lib.data_transformation.export import export_table_to_sql
from base_lib.data_transformation.export import export_table_to_csv_txt
from base_lib.file_loader.load_data import TextFileLoader
from base_lib.SQL.sql_connection import create_mysql_engine,create_postgres_sql_engine,create_lite_engine
from base_lib.SQL.sql_helper import qry_data
from pathlib import Path

def get_example_table() -> Table:
    headers =["ID","Description","Value","Score"] 
    data_container =  [
        (1, "ID", 19640817, "4.42"),
        (5, "User", 1990111, "8.5"),
        (9, "Mister", 19880827, "12.1"),
        (12, "Admin", 20001217, "15.4"),
    ]
    return Table(data_container,headers)

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

    loader = TextFileLoader()
    data =loader.load(file_path)
    loaded_table = Table(data[1:],data[0])
    table.transform_data_within_table()
    loaded_table.transform_data_within_table()
    print(table)
    print(loaded_table)
    print(table==loaded_table)
    #assert table == loaded_table

def test_mysql():
    engine = create_mysql_engine(mysql_db="mydatabase",mysql_user="myuser",mysql_pw="secretpassword",db_host="localhost",db_port="3306")
    df = qry_data("Select * from users;",engine)
    print(df)

def test_postgres():
    engine = create_postgres_sql_engine(postgres_db="mydb",postgres_user="myuser",postgres_pw="mypassword",db_host="localhost",db_port="5432")
    df = qry_data("Select * from users;",engine)
    print(df)

def test_export_table_to_db():
    engine = create_lite_engine()
    table = get_example_table()
    export_table_to_sql(table,"Example",engine)
    qry = "Select * from Example"
    df = qry_data(qry,engine)
    print(df)
    table.transform_to_dataframe()
    print(table.df)

def main():
    #ordinary_logger.critical("Test")
    app_logger.error("Next")
    

if __name__ == "__main__":
    main()
