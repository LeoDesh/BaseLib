from typing import Iterable,List,Any,Callable
from data_transformation.value_validation import format_value,parse_int,parse_datetime,parse_float,determine_type
from datetime import datetime
import pandas as pd

TRANSFORMATION_DICT = {
    str: format_value,
    datetime: parse_datetime,
    float: parse_float,
    int: parse_int,
}


class Table:
    def __init__(self,data_container:Iterable[List[Any]],header:List[str]):
        if not header:
            size = len(data_container[0])
            header = [f"Column{idx+1}" for idx in range(size)]
        self.header = header
        self.rows = data_container
        self.compare_header_with_row()
        self.shape = (len(self.rows),len(self.header))
        self.convert_rows_to_columns()
        
        #self.compute_column_types()
        #self.convert_column_types()
    def compare_header_with_row(self):
        if len(self.rows[0]) != len(self.header):
            raise ValueError(f"Header size {len(self.header)} does not match with elements in row ({len(self.rows[0])}")

    def convert_rows_to_columns(self):
        self.columns = [[row[i] for row in self.rows]  for i in range(self.shape[1])]

    def compute_column_types(self):
        pass

    def convert_column_types(self):
        pass

    def update_row_values_of_column_idx(self,column_idx:int,func:Callable) -> None:
        for row in self.rows:
            row[column_idx] = func(row[column_idx])

    def update_column_values(self,column_idx:int,func:Callable) -> None:
        rows,_ = self.shape
        for row_idx in range(rows):
            self.columns[column_idx][row_idx] = func(self.columns[column_idx][row_idx])

    def transform_to_dataframe(self) -> None:
        data = {header:column for header,column in zip(self.header,self.columns)}
    