from datetime import datetime
from typing import Any
#RANKING = {1: str, 2: float, 3: int, 4: datetime}
FORMATS = [
    "%Y-%m-%dT%H:%M:%S%z",
    "%Y-%m-%dT%H:%M:%S",
    "%Y-%m-%d %H:%M:%S",
    "%Y-%m-%d",
    "%d/%m/%Y",
    "%d.%m.%Y %H:%M:%S",
    "%d.%m.%Y",
    "%d.%m.%y",
    "%d%m%y",
    "%d%m%Y",
    "%Y%m%d"
]


def determine_type(value: str) -> type:
    type_func = [parse_datetime,parse_int,parse_float]
    for func in type_func:
        value_type = func(value)
        if value_type is not str:
            return value_type
    return str
    


def parse_datetime(value: str) -> datetime:
    for fmt in FORMATS:
        #print(fmt)
        try:
            yr = datetime.strptime(value, fmt).year
            if validate_year(yr):
                return datetime
        except ValueError:
            pass
    return str

def validate_year(yr:int):
    if yr < 1900 or yr > 2100:
        return False
    return True

def parse_int(value: str) -> int | str:
    try: 
        int(value)
        return int
    except ValueError:
        return str


def parse_float(value: str) -> float | str:
    try: 
        float(value)
        return float
    except ValueError:
        return str


def format_value(value:Any):
    return str(value).strip()
    