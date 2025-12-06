from pathlib import Path
import json

def load_json_file(file_name:str):
    with open(file_name,"r") as file:
        return json.load(file)


SETUP_PATH = Path(r"SQL\sql_setup")
SERVER_INFO = load_json_file(str(SETUP_PATH / "sql.json"))
