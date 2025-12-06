import pytest
from file_loader.file_verification import FileVerification


@pytest.fixture
def txt_verification() -> FileVerification:
    return FileVerification(".txt")


@pytest.fixture
def excel_verification() -> FileVerification:
    return FileVerification([".xlsx", ".xls"])


@pytest.fixture
def sample_file() -> str:
    return r"tests\load_data\files\simple.txt"

@pytest.fixture
def modified_file() -> str:
    return r"tests\load_data\files\modified.txt"

@pytest.fixture
def excel_file() -> str:
    return r"tests\load_data\files\excel.xlsx"


@pytest.fixture
def csv_file() -> str:
    return r"tests\load_data\files\data.csv"


@pytest.fixture
def json_file() -> str:
    return r"tests\load_data\files\logs.jsonl"