from data_transformation.structure_validation import (
    validate_row_lengths,
    validate_container,
    validate_data_rows,
    validate_empty_container,
    validate_iterable,
    validate_iterable_of_lists_structure,
)
import pytest


@pytest.mark.transformation
def test_validate_row_lengths_error(data_container_different_columns_sizes):
    with pytest.raises(ValueError):
        validate_row_lengths(data_container_different_columns_sizes)


@pytest.mark.transformation
def test_validate_row_lengths(data_container_suitable):
    validate_row_lengths(data_container_suitable)


@pytest.mark.transformation
def test_validate_container(data_container_empty):
    assert validate_container(data_container_empty)


@pytest.mark.transformation
def test_validate_container_not_suitable(data_row_str):
    assert not validate_container(data_row_str)


@pytest.mark.transformation
def test_validate_data_rows_error(data_row_str):
    with pytest.raises(ValueError):
        validate_data_rows(data_row_str)


@pytest.mark.transformation
def test_validate_data_rows(data_container_different_columns_sizes):
    validate_data_rows(data_container_different_columns_sizes)


@pytest.mark.transformation
def test_validate_data_rows_mixed(data_container_mixed_types):
    with pytest.raises(ValueError):
        validate_data_rows(data_container_mixed_types)

@pytest.mark.transformation
def test_validate_empty_container(data_container_empty):
    assert not validate_empty_container(data_container_empty)


@pytest.mark.transformation
def test_validate_iterable(data_container_empty):
    assert validate_iterable(data_container_empty)


@pytest.mark.transformation
def test_validate_iterable_fail():
    assert not validate_iterable(2)


@pytest.mark.transformation
def test_validate_iterable_of_lists_structure(data_container_suitable):
    assert validate_iterable_of_lists_structure(data_container_suitable)


@pytest.mark.transformation
def test_validate_iterable_of_lists_structure_fail(data_container_different_columns_sizes):
    with pytest.raises(ValueError):
        validate_iterable_of_lists_structure(data_container_different_columns_sizes)