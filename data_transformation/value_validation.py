from __future__ import annotations
from datetime import datetime
from typing import Any, List

# RANKING = {1: str, 2: float, 3: int, 4: datetime}
FORMATS = [
    "%Y-%m-%d %H:%M:%S",
    "%Y-%m-%d",
    "%d/%m/%Y",
    "%d.%m.%Y %H:%M:%S",
    "%d.%m.%Y",
    "%d.%m.%y",
    "%d%m%y",
    "%d%m%Y",
    "%Y%m%d",
]


def determine_column_type(values: List[Any]):
    choice_functions = {
        datetime: determine_column_date_type,
        int: determine_column_integer_type,
        float: determine_column_float_type,
    }
    for data_type,func in choice_functions.items():
        if func(values):
            return data_type
    return str
    


def determine_column_date_type(values: List[Any]) -> bool:
    for value in values:
        value_str = format_value(value)
        if parse_datetime(value_str) is not datetime:
            return False
    return True


def determine_column_integer_type(values: List[Any]) -> bool:
    for value in values:
        value_str = format_value(value)
        if parse_int(value_str) is not int:
            return False
    return True


def determine_column_float_type(values: List[Any]) -> bool:
    for value in values:
        value_str = format_value(value)
        if parse_float(value_str) is not float:
            return False
    return True


def determine_type(value: Any) -> type:
    type_func = [parse_datetime, parse_int, parse_float]
    for func in type_func:
        value_type = func(value)
        if value_type is not str:
            return value_type
    return str


def parse_datetime(value: Any) -> datetime:
    try:
        convert_to_datetime(value)
        return datetime
    except ValueError:
        return str


def convert_to_datetime(value: Any):
    value = format_value(value)
    for fmt in FORMATS:
        try:
            date_value = datetime.strptime(value, fmt)
            yr = date_value.year
            if validate_year(yr):
                return date_value
        except ValueError:
            pass
    raise ValueError(f"{value} cannot be parsed to datetime.")


def convert_to_int(value: Any):
    try:
        value = format_value(value)
        int_value = int(value)
        return int_value
    except ValueError:
        raise ValueError(f"{value} cannot be converted to int.")


def convert_to_float(value: Any):
    try:
        value = format_value(value)
        float_value = float(value)
        return float_value
    except ValueError:
        raise ValueError(f"{value} cannot be converted to float.")


def validate_year(yr: int):
    if yr < 1900 or yr > 2100:
        return False
    return True


def parse_int(value: Any) -> int | str:
    try:
        convert_to_int(value)
        return int
    except ValueError:
        return str


def parse_float(value: Any) -> float | str:
    try:
        convert_to_float(value)
        return float
    except ValueError:
        return str


def format_value(value: Any):
    return str(value).strip()
