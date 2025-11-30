from pathlib import Path
from typing import List

class FileVerification:
    def __init__(self,file_endings:str|List[str]):
        if isinstance(file_endings,str):
            self.file_endings = [file_endings]
        else:
            self.file_endings = file_endings


    def convert_path(self,path:str|Path) -> Path:
        if isinstance(path,str):
            return Path(path)
        return path

    def verify_file(self,path:str|Path) -> None:
        path = self.convert_path(path)
        if not self.verify_file_exists(path):
            raise ValueError(f"Path {path} does not belong to a file.")

        if not self.verify_format(path):
            raise ValueError(f"Path {path} does not have the right extension.")


    def verify_format(self,path:str|Path) -> bool:
        path = self.convert_path(path)
        path_ending = path.suffix
        for ending in self.file_endings:
            if path_ending == ending:
                return True
        return False

    def verify_file_exists(self,path:str|Path) -> bool:
        path = self.convert_path(path)
        return path.exists() and path.is_file()
