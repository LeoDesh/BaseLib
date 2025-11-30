from abc import ABC
from pathlib import Path
from file_verification import FileVerification
from typing import List, Iterable
from LoggerConfig import app_logger

class IFileLoader(ABC):
    def load(self, filename: str | Path, *, sep=","):
        pass


class TextFileLoader:
    def __init__(self):
        self.file_verification = FileVerification(".txt")
        self.common_file_sep = [",", ";", "\t", " "]

    def load(self, filename: str | Path, *, sep="") -> List[List[str]]:
        self.file_verification.verify_file(filename)
        text_lines = self.get_text_lines(filename)
        if not sep:
            sep = self.find_field_separator(text_lines)
        return [list(line.split(sep)) for line in text_lines]

    def clean_up_text(self,field:str):
        return field.replace("\n","").strip()

    def get_text_lines(self, filename: str | Path) -> List[str]:
        with open(str(filename), "r") as file:
            return [self.clean_up_text(line) for line in  file.readlines() if self.clean_up_text(line)]

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


