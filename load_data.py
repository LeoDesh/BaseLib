from abc import ABC
from pathlib import Path
from file_verification import FileVerification
from typing import List, Iterable, Dict, Any
from load_helper import get_file_lines
import pandas as pd
import json
from LoggerConfig import app_logger


class IFileLoader(ABC):
    def load(self, filename: str | Path):
        pass


class TextFileLoader:
    def __init__(self):
        self.file_verification = FileVerification(".txt")
        self.common_file_sep = [",", ";", "\t", " "]

    def load(self, filename: str | Path, *, sep="") -> List[List[str]]:
        self.file_verification.verify_file(filename)
        text_lines = get_file_lines(filename)
        if not sep:
            sep = self.find_field_separator(text_lines)
        return [list(line.split(sep)) for line in text_lines]

    def find_field_separator(self, file_lines: List[str]) -> str:
        for sep in self.common_file_sep:
            if self.check_field_separator(file_lines, sep):
                return sep
        raise ValueError("Cannot find a suitable separator.")

    def check_field_separator(self, file_lines: Iterable[str], sep: str) -> bool:
        col_lengths = list({len(list(line.split(sep))) for line in file_lines})
        app_logger.debug(f"Sep:'{sep}' , Set:{col_lengths}")
        if len(col_lengths) > 1 or col_lengths[0] == 1:
            app_logger.info(f"Sep:'{sep}' , Set:{col_lengths}")
            return False
        return True


class CSVFileLoader:
    def __init__(self):
        self.file_verification = FileVerification(".csv")

    def load(self, filename: str | Path, sep: str) -> pd.DataFrame:
        self.file_verification.verify_file(filename)
        return pd.read_csv(filename, sep=sep)


class ExcelFileLoader:
    def __init__(self):
        self.file_verification = FileVerification([".xlsx", ".xls", ".xlsm"])

    def load(self, filename: str | Path, sheet_name: str) -> pd.DataFrame:
        self.file_verification.verify_file(filename)
        return pd.read_excel(filename, sheet_name=sheet_name)


class JSONLineLoader:
    def __init__(self):
        self.file_verification = FileVerification(".jsonl")

    def load(self, filename: str | Path) -> List[Dict[str, Any]]:
        self.file_verification.verify_file(filename)
        file_lines = get_file_lines(filename)
        return [json.loads(line) for line in file_lines]
