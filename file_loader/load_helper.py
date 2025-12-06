from pathlib import Path


def clean_up_text(field:str):
        return field.replace("\n","").strip()

def get_file_lines(filename:str|Path):
    with open(str(filename), "r") as file:
        return [clean_up_text(line) for line in  file.readlines() if clean_up_text(line)]