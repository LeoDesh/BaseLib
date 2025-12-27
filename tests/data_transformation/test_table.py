from base_lib.data_transformation.table import Table
from datetime import datetime
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

#data_container_transformation
@pytest.mark.transformation
def test_table_column_types(data_container_transformation):
    header= ["PersonID","Description","Birthdate","Score"]
    table = Table(data_container_transformation,header)
    table.compute_column_types()
    assert table.column_types == [int,str,datetime,float]

@pytest.mark.transformation
def test_table_data_transformation(data_container_transformation):
    header= ["PersonID","Description","Birthdate","Score"]
    table = Table(data_container_transformation,header)
    table.transform_data_within_table()
    assert table.rows[0][2] == datetime(1964,8,17)
    assert table.columns[2][0] == datetime(1964,8,17)
    assert table.rows[3][3] == 15.4


@pytest.mark.transformation
def test_table_data_transformation_provided_types(data_container_transformation):
    header= ["PersonID","Description","Birthdate","Score"]
    column_types = [int,str,int,str]
    table = Table(data_container_transformation,header,column_types)
    table.transform_data_within_table()
    assert table.column_types == column_types
    assert table.rows[0][2] == 19640817
    assert table.rows[3][3] == "15.4"

@pytest.mark.transformation
def test_table_data_equal(data_container_transformation):
    header= ["PersonID","Description","Birthdate","Score"]
    column_types = [int,str,int,str]
    table = Table(data_container_transformation,header,column_types)
    table.transform_data_within_table()
    table_trg = Table(data_container_transformation,header,column_types)
    table_trg.transform_data_within_table()
    assert table == table_trg

@pytest.mark.transformation
def test_table_header_not_equal(data_container_transformation):
    header= ["PersonID","Description","Birthdate","Score"]
    column_types = [int,str,int,str]
    table = Table(data_container_transformation,header,column_types)
    table.transform_data_within_table()
    header_trg = ["PersonID","Birthdate","Description","Score"]
    table_trg = Table(data_container_transformation,header_trg,column_types)
    table_trg.transform_data_within_table()
    assert not table.compare_header(table_trg.header)

@pytest.mark.transformation
def test_table_columns_not_equal(data_container_transformation):
    header= ["PersonID","Description","Birthdate","Score"]
    column_types = [int,str,int,str]
    table = Table(data_container_transformation,header,column_types)
    table.transform_data_within_table()
    header_trg = ["PersonID","Birthdate","Description","Score"]
    table_trg = Table(data_container_transformation,header_trg,column_types)
    table_trg.transform_data_within_table()
    table_trg.columns[0][0] = -1
    assert not table.compare_columns(table_trg.header)