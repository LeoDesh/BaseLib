from abc import ABC  
from pathlib import Path



class IFileLoader(ABC):
    def load(filename:str|Path, * , sep=","):
        pass


     


