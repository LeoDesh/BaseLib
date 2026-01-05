from __future__ import annotations
from typing import Iterable, List, Any, Callable

# from LoggerConfig import app_logger
from base_lib.data_transformation.value_validation import (
    convert_to_datetime,
    convert_to_float,
    convert_to_int,
    format_value,
    determine_column_type,
)
from base_lib.data_transformation.structure_validation import (
    validate_iterable_of_lists_structure,
)
from datetime import datetime
import pandas as pd

TRANSFORMATION_DICT = {
    str: format_value,
    datetime: convert_to_datetime,
    float: convert_to_float,
    int: convert_to_int,
}


class Table:
    def __init__(
        self,
        data_container: Iterable[List[Any]],
        header: List[str] = [],
        column_types: List[type] = [],
        transform_data: bool = False,
    ):
        validate_iterable_of_lists_structure(data_container)
        if not header:
            size = len(data_container[0])
            header = [f"Column{idx + 1}" for idx in range(size)]
        self.header = header
        self.rows = [list(row) for row in data_container]
        self.compare_header_with_row()
        self.shape = (len(self.rows), len(self.header))
        self.convert_rows_to_columns()
        self.column_types = column_types
        if transform_data:
            self.transform_data_within_table()

    def transform_data_within_table(self):
        if not self.column_types:
            self.compute_column_types()
        self.convert_column_types()

    def compare_header_with_row(self):
        if len(self.rows[0]) != len(self.header):
            raise ValueError(
                f"Header size {len(self.header)} does not match with elements in row ({len(self.rows[0])}"
            )

    def convert_rows_to_columns(self):
        self.columns = [[row[i] for row in self.rows] for i in range(self.shape[1])]

    def compute_column_types(self):
        self.column_types = [determine_column_type(column) for column in self.columns]

    def convert_column_types(self):
        if len(self.column_types) != len(self.columns):
            raise ValueError(
                f"Column Type Length {len(self.column_types)} does not match Column Length {len(self.columns)}."
            )
        for column_idx, column_type in enumerate(self.column_types):
            self.update_column_values(column_idx, TRANSFORMATION_DICT[column_type])
            self.update_row_values_of_column_idx(
                column_idx, TRANSFORMATION_DICT[column_type]
            )

    def update_row_values_of_column_idx(self, column_idx: int, func: Callable) -> None:
        for row in self.rows:
            row[column_idx] = func(row[column_idx])

    def update_column_values(self, column_idx: int, func: Callable) -> None:
        rows, _ = self.shape
        for row_idx in range(rows):
            self.columns[column_idx][row_idx] = func(self.columns[column_idx][row_idx])

    def transform_to_dataframe(self) -> None:
        data = {header: column for header, column in zip(self.header, self.columns)}
        self.df = pd.DataFrame(data)

    def __str__(self):
        self.transform_to_dataframe()
        return str(self.df)

    def __eq__(self, other: Table):
        if not isinstance(other, Table):
            return NotImplemented
        if not self.compare_header(other.header):
            return False
        if not self.compare_columns(other.columns):
            return False
        return True

    def compare_header(self, other_header: List[str]) -> bool:
        for src_header, trg_header in zip(self.header, other_header):
            if src_header != trg_header:
                # app_logger.info(f"{src_header}:{trg_header}")
                return False
        return True

    def compare_columns(self, other_columns: List[List[Any]]) -> bool:
        for src_column, trg_column in zip(self.columns, other_columns):
            for src_value, trg_value in zip(src_column, trg_column):
                if src_value != trg_value:
                    # app_logger.info(f"{src_value}:{trg_value}")
                    return False
        return True
