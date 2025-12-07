from typing import List, Dict, Iterable, Any, Tuple, Set
from collections.abc import Iterable as It


def validate_iterable_of_lists_structure(data_container: Iterable[List[Any]]) -> bool|None:
    validate_is_container_iterable(data_container)
    validate_data_rows(data_container)
    validate_row_lengths(data_container)
    return True

def validate_row_lengths(data_container: List[List[Any] | Tuple[Any] | Set[Any]]) -> None:
    row_lengths = {len(data_row) for data_row in data_container}
    if len(row_lengths) > 1:
        raise ValueError("Not all rows have the same amount of values.")


def validate_data_rows(data_container: Iterable[Any]) -> None:
    validation_result = [validate_container(data_row) for data_row in data_container]
    if not all(validation_result):
        raise ValueError("Not all rows have the appropriate iterable type.")


def validate_empty_container(variable: List[Any] | Tuple[Any] | Set[Any]) -> bool:
    if variable:
        return True
    return False


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


def validate_jsonl_structure(data_container: Iterable[Dict[str, Any]]):
    pass
