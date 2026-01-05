import pytest
import pandas as pd
from base_lib.data_transformation.table import Table


@pytest.fixture()
def data_container_empty():
    return []


@pytest.fixture(scope="session")
def data_row_str():
    return "list"


@pytest.fixture()
def data_container_mixed_types():
    return [(1, 2, 3), (4, 5), "str"]


@pytest.fixture()
def data_container_different_columns_sizes():
    return [(1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11), (12, 13, 14, 15)]


@pytest.fixture()
def data_container_suitable():
    return [(1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11, 12), (12, 13, 14, 15)]


@pytest.fixture()
def data_container_transformation():
    return [
        (1, "ID", 19640817, "4.42"),
        (5, "User", 1990111, "8.5"),
        (9, "Mister", 19880827, "12.1"),
        (12, "Admin", 20001217, "15.4"),
    ]


@pytest.fixture()
def table_example(data_container_transformation):
    data = data_container_transformation
    headers = ["ID", "Description", "Value", "Score"]
    return Table(data, headers)


@pytest.fixture()
def data_container_single_row():
    return [1, 2, 3, 4]


@pytest.fixture()
def data_container_jsonl_suitable():
    return [{"PersonID": 15, "OrderID": 22}, {"PersonID": 44, "OrderID": 62}]


@pytest.fixture()
def data_container_jsonl_different_columns():
    return [{"PersonID": 15, "PurchaseID": 22}, {"PersonID": 44, "OrderID": 62}]


@pytest.fixture()
def data_container_jsonl_different_column_sizes():
    return [
        {"PersonID": 15, "PurchaseID": 22},
        {"PersonID": 44, "OrderID": 62, "PurchaseID": 348},
    ]


@pytest.fixture()
def data_container_jsonl_mixed_types():
    return [
        {"PersonID": 15, "PurchaseID": 22},
        18,
        {"PersonID": 35, "PurchaseID": 42},
    ]


@pytest.fixture()
def data_container_json_suitable():
    return {"1": {"PersonID": 15, "OrderID": 22}, "2": {"PersonID": 44, "OrderID": 62}}


@pytest.fixture()
def data_container_dataframe():
    return pd.DataFrame({"PersonID": [15, 44], "OrderID": [22, 62]})


@pytest.fixture()
def data_container_json_dataframe():
    return pd.DataFrame(
        {"PersonID": [15, 44], "OrderID": [22, 62], "Index": ["1", "2"]}
    )


@pytest.fixture()
def data_container_json_empty():
    return {}
