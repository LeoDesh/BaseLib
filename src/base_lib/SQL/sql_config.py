import json

def load_json_file(file_name:str):
    with open(file_name,"r") as file:
        return json.load(file)



SERVER_INFO = load_json_file("sql.json")
