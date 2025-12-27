import re 
from typing import List
def regex_match(text:str,reg_pattern_str:str,group_idx:int=0) -> str:
    reg_pattern = re.compile(reg_pattern_str)
    reg_match = reg_pattern.search(text)
    if reg_match:
        return reg_match.group(group_idx)
    return ""

def regex_match_exists(text:str,regex_pattern_str:str) -> bool:
    matched = regex_match(text,regex_pattern_str)
    if matched:
        return True
    return False

def regex_get_all_matches(text:str,reg_pattern_str:str,group_idx:int=0) -> List[str]:
    reg_pattern = re.compile(reg_pattern_str)
    matches = reg_pattern.finditer(text)
    return [match.group(group_idx) for match in matches]

