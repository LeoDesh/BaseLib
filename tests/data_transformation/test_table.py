from data_transformation.table import Table
import pytest

@pytest.mark.transformation
def test_table_column_transformation_with_empty_header(data_container_suitable):
    table = Table(data_container_suitable,[])
    assert table.shape == (4,4)
    assert table.columns[0] == [1,5,9,12]
    assert table.header == [f"Column{idx+1}" for idx in range(4)]

@pytest.mark.transformation
def test_table_column_transformation_with_header(data_container_suitable):
    header= ["PersonID","ProfileID","UserProfileID","OrderID"]
    table = Table(data_container_suitable,header)
    assert table.shape == (4,4)
    assert table.columns[2] == [3,7,11,14]
    assert table.header == header

@pytest.mark.transformation
def test_table_column_header_missmatch(data_container_suitable):
    header= ["PersonID","ProfileID","UserProfileID"]
    with pytest.raises(ValueError):
        Table(data_container_suitable,header)
