from typing import List, Dict, Iterable, Any, Tuple, Set
from collections.abc import Iterable as It
import pandas as pd


def validate_iterable_of_lists_structure(
    data_container: Iterable[List[Any]],
) -> bool | None:
    validate_is_container_iterable(data_container)
    validate_data_rows(data_container)
    validate_row_lengths(data_container)
    return True


def validate_row_lengths(
    data_container: List[List[Any] | Tuple[Any] | Set[Any]],
) -> None:
    row_lengths = {len(data_row) for data_row in data_container}
    validate_non_unique_set(row_lengths)


def validate_data_rows(data_container: Iterable[Any]) -> None:
    validation_result = [validate_container(data_row) for data_row in data_container]
    if not all(validation_result):
        raise ValueError("Not all rows have the appropriate iterable type.")


def validate_empty_container(variable: List[Any] | Tuple[Any] | Set[Any] | Dict[Any,Any]):
    if not variable:
        raise ValueError("Container is empty.")



def validate_is_container_iterable(data_container: Iterable[Any]) -> None:
    if not validate_iterable(data_container):
        raise ValueError("Not Iterable")


def validate_iterable(variable: Iterable[Any]) -> bool:
    if not isinstance(variable, It):
        return False
    return True


def validate_container(variable: List[Any] | Tuple[Any] | Set[Any]) -> bool:
    if (
        isinstance(variable, list)
        or isinstance(variable, tuple)
        or isinstance(variable, set)
    ):
        return True
    return False



def validate_jsonl_structure(data_container: Iterable[Dict[str, Any]]) -> bool | None:
    validate_empty_container(data_container)
    validate_is_container_iterable(data_container)
    validate_dict_data_container(data_container)
    validate_dict_keys(data_container)
    return True


def validate_dict_keys(data_container: Iterable[Dict[str, Any]]):
    columns_name_set, column_sizes = analyze_dict_keys(data_container)
    validate_non_unique_set(column_sizes)
    validate_column_amount_with_column_names(columns_name_set, column_sizes)


def analyze_dict_keys(data_container: Iterable[Dict[str, Any]]) -> Tuple[Set, Set]:
    columns_name_set = set()
    column_sizes = set()
    for data_row in data_container:
        for key in data_row.keys():
            columns_name_set.add(key)
        column_sizes.add(len(data_row.keys()))
    return (columns_name_set, column_sizes)


def validate_non_unique_set(data_set: Set) -> None:
    if len(data_set) > 1:
        raise ValueError("The values within the columns are not unique")


def validate_column_amount_with_column_names(
    columns_name_set: Set, column_sizes: Set
) -> None:
    if list(column_sizes)[0] != len(columns_name_set):
        raise ValueError("There are different keys within the rows")


def validate_row_dict(row_dict: Any) -> bool:
    if isinstance(row_dict, dict):
        return True
    return False


def validate_dict_data_container(data_container: Iterable[Any]) -> None:
    for row_dict in data_container:
        if not validate_row_dict(row_dict):
            raise ValueError("Data row is not a dict.")


def validate_json_structure(
    data_container: Dict[str | int, Dict[str, Any]],
) -> bool | None:
    values_data_container = list(data_container.values())
    return validate_jsonl_structure(values_data_container)


def validate_csv_xlsx_structure(df: pd.DataFrame):
    if df.empty:
        return False
    return True
