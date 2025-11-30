import pytest
from file_verification import FileVerification
@pytest.fixture 
def txt_verification() -> FileVerification:
    return FileVerification(".txt")

@pytest.fixture 
def excel_verification() -> FileVerification:
    return FileVerification([".xlsx",".xls"])

@pytest.fixture 
def sample_file() -> str:
    return r"tests\load_data\simple.txt"
