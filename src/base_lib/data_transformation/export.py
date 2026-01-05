from base_lib.data_transformation.table import Table
from base_lib.SQL.sql_helper import exec_sql,SqlEngine
from typing import List, Dict, Any
import pandas as pd
import json


def export_jsonl_to_file(data: List[Dict[str, Any]], filename: str):
    with open(filename, "w", encoding="utf-8") as f:
        for item in data:
            f.write(f"{json.dumps(item)}\n")


def export_json_to_file(data: Dict[str, Any], filename: str):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(data))


def export_to_excel(df: pd.DataFrame, filename: str, sheet_name: str):
    df.to_excel(excel_writer=filename, sheet_name=sheet_name, index=False)


def export_to_csv_txt(df: pd.DataFrame, filename: str):
    df.to_csv(filename, sep=";", index=False)


def export_table_to_jsonl(table: Table, filename: str):
    table.transform_to_dataframe()
    records = table.df.to_dict(orient="records")
    export_jsonl_to_file(records, filename)


def export_table_to_json(table: Table, filename: str):
    table.transform_to_dataframe()
    if "Index" not in table.header:
        raise ValueError(f"There is no Index column in {table.header}")
    records = table.df.to_dict(orient="records")
    json_record = {
        record["Index"]: {key: value for key, value in record.items() if key != "Index"}
        for record in records
    }
    export_json_to_file(json_record, filename)


def export_table_to_excel(table: Table, filename: str, sheet_name: str):
    table.transform_to_dataframe()
    export_to_excel(df=table.df, filename=filename, sheet_name=sheet_name)


def export_table_to_csv_txt(table: Table, filename: str):
    table.transform_to_dataframe()
    export_to_csv_txt(table.df, filename)

def export_table_to_sql(table:Table,table_name:str,sql_engine:SqlEngine,if_exists:str="replace"):
    table.transform_to_dataframe()
    df = table.df 
    df.to_sql(table_name,sql_engine,if_exists=if_exists,index=False)


