import pytest


@pytest.fixture()
def data_container_empty():
    return []


@pytest.fixture(scope="session")
def data_row_str():
    return "list"


@pytest.fixture()
def data_container_mixed_types():
    return [(1,2,3),(4,5),"str"]


@pytest.fixture()
def data_container_different_columns_sizes():
    return [(1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11), (12, 13, 14, 15)]

@pytest.fixture()
def data_container_suitable():
    return [(1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11,12), (12, 13, 14, 15)]

@pytest.fixture()
def data_container_single_row():
    return [1, 2, 3, 4]
