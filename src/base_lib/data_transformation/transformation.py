from base_lib.data_transformation.table import Table
from base_lib.data_transformation.structure_validation import (
    validate_json_structure,
    validate_csv_xlsx_structure,
    validate_jsonl_structure,
)
from typing import Dict, List, Any
import pandas as pd


def convert_dataframe_to_table(df: pd.DataFrame) -> Table:
    validate_csv_xlsx_structure(df)
    data_container = df.to_dict(orient="records")
    return transform_list_of_dict_to_table(data_container)

def convert_jsonl_to_table(data_container: List[Dict[str, Any]]) -> Table: 
    validate_jsonl_structure(data_container)
    return transform_list_of_dict_to_table(data_container)

def convert_json_to_table(data_container: Dict[str | int, Dict[str, Any]]) -> Table: 
    validate_json_structure(data_container)
    #Take keys as Index // first column
    data = list(data_container.values())
    index_data = list(data_container.keys())
    for line_dict,index in zip(data,index_data):
        line_dict.update({"Index":index})
    return transform_list_of_dict_to_table(data)

def transform_list_of_dict_to_table(data_container:List[Dict[str, Any]]) -> Table:
    header = list(data_container[0].keys())
    data = [list(row_values.values()) for row_values in data_container]
    return Table(data,header)