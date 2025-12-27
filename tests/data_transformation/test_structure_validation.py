from base_lib.data_transformation.structure_validation import (
    validate_row_lengths,
    validate_container,
    validate_data_rows,
    validate_empty_container,
    validate_iterable,
    validate_iterable_of_lists_structure,
    validate_json_structure,
    validate_jsonl_structure,
    validate_dict_keys,
    validate_column_amount_with_column_names,
    analyze_dict_keys,
    validate_dict_data_container,
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
    with pytest.raises(ValueError):
        validate_empty_container(data_container_empty)


@pytest.mark.transformation
def test_validate_iterable(data_container_empty):
    validate_iterable(data_container_empty)


@pytest.mark.transformation
def test_validate_iterable_fail():
    assert not validate_iterable(2)


@pytest.mark.transformation
def test_validate_iterable_of_lists_structure(data_container_suitable):
    assert validate_iterable_of_lists_structure(data_container_suitable)


@pytest.mark.transformation
def test_validate_iterable_of_lists_structure_fail(
    data_container_different_columns_sizes,
):
    with pytest.raises(ValueError):
        validate_iterable_of_lists_structure(data_container_different_columns_sizes)


@pytest.mark.transformation
def test_validate_column_amount_with_column_names_error(
    data_container_jsonl_different_columns,
):
    with pytest.raises(ValueError):
        column_names_set, columns_sizes = analyze_dict_keys(
            data_container_jsonl_different_columns
        )
        validate_column_amount_with_column_names(column_names_set, columns_sizes)


@pytest.mark.transformation
def test_validate_column_amount_with_column_names(data_container_jsonl_suitable):
    column_names_set, columns_sizes = analyze_dict_keys(data_container_jsonl_suitable)
    validate_column_amount_with_column_names(column_names_set, columns_sizes)


@pytest.mark.transformation
def test_analyze_dict_keys(data_container_jsonl_different_columns):
    column_names_set, columns_sizes = analyze_dict_keys(
        data_container_jsonl_different_columns
    )
    assert column_names_set == {"PersonID", "OrderID", "PurchaseID"}
    assert columns_sizes == {2}


@pytest.mark.transformation
def test_validate_dict_data_container(data_container_jsonl_mixed_types):
    with pytest.raises(ValueError):
        validate_dict_data_container(data_container_jsonl_mixed_types)


@pytest.mark.transformation
def test_validate_dict_keys_error(data_container_jsonl_different_columns):
    with pytest.raises(ValueError):
        validate_dict_keys(data_container_jsonl_different_columns)


@pytest.mark.transformation
def test_validate_jsonl_structure(data_container_jsonl_suitable):
    assert validate_jsonl_structure(data_container_jsonl_suitable)


@pytest.mark.transformation
def test_validate_json_structure(data_container_json_suitable):
    assert validate_json_structure(data_container_json_suitable)


@pytest.mark.transformation
def test_validate_jsonl_structure_empty(data_container_empty):
    with pytest.raises(ValueError):
        validate_jsonl_structure(data_container_empty)

@pytest.mark.transformation
def test_validate_json_structure_empty(data_container_json_empty):
    with pytest.raises(ValueError):
        validate_jsonl_structure(data_container_json_empty)

