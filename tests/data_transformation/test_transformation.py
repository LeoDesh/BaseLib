from base_lib.data_transformation.transformation import (
    convert_dataframe_to_table,
    convert_json_to_table,
    convert_jsonl_to_table,
)
import pytest

@pytest.mark.transformation
def test_convert_dataframe_to_table(data_container_dataframe):
    table = convert_dataframe_to_table(data_container_dataframe)
    assert str(table) == str(data_container_dataframe)

@pytest.mark.transformation
def test_convert_json_to_table(data_container_json_suitable,data_container_json_dataframe):
    table = convert_json_to_table(data_container_json_suitable)
    assert str(table) == str(data_container_json_dataframe)


@pytest.mark.transformation
def test_convert_jsonl_to_table(data_container_jsonl_suitable,data_container_dataframe):
    table = convert_jsonl_to_table(data_container_jsonl_suitable)
    assert str(table) == str(data_container_dataframe)