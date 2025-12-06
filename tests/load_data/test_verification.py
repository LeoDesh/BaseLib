from pathlib import Path
from file_loader.file_verification import FileVerification


def test_file_verification_initialization(txt_verification: FileVerification):
    assert not isinstance(txt_verification.file_endings, str)


def test_file_verification_path_conversion(txt_verification: FileVerification):
    filepath = "pyproject"
    assert isinstance(txt_verification.convert_path(filepath), Path)


def test_file_exists(txt_verification: FileVerification, sample_file: str):
    assert txt_verification.verify_file_exists(sample_file)


def test_file_not_exists(txt_verification: FileVerification, sample_file: str):
    assert not txt_verification.verify_file_exists(f"text\\{sample_file}")


def test_file_format(txt_verification: FileVerification, sample_file: str):
    assert txt_verification.verify_format(sample_file)


def test_file_format_fail(excel_verification: FileVerification, sample_file: str):
    assert not excel_verification.verify_format(sample_file)


def test_multiple_file_format(excel_verification: FileVerification, sample_file: str):
    new_sample_file = sample_file.replace(".txt", ".xlsx")
    assert excel_verification.verify_format(new_sample_file)
