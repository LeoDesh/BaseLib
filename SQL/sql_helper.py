from SQL.sql_connection import SqlEngine
from sqlalchemy import text
import pandas as pd
from typing import List, Dict


def qry_data(qry: str, sql_engine: SqlEngine):
    with sql_engine.connect() as sql_conn:
        return pd.read_sql(qry, con=sql_conn)


def qry_multiple_data(qry_dict: Dict[str, str], sql_engine: SqlEngine):
    with sql_engine.connect() as sql_conn:
        return {
            description: pd.read_sql(qry, con=sql_conn)
            for description, qry in qry_dict.items()
        }


def exec_sql(sqlStmt: str, sql_engine: SqlEngine):
    with sql_engine.connect() as sql_conn:
        sql_conn.execute(text(sqlStmt))
        sql_conn.commit()


def exec_multiple_sql_stmt(sqlStmtList: List[str], sql_engine: SqlEngine):
    with sql_engine.connect() as sql_conn:
        for sqlStmt in sqlStmtList:
            sql_conn.execute(text(sqlStmt))
        sql_conn.commit()


def read_qry_from_file(path: str):
    with open(path, "r") as file:
        return file.read()


def modify_qry(qry: str, trg_words: List[str], replace_words: List[str]):
    for trg_word, rep_word in zip(trg_words, replace_words):
        mod_trg_word = f"[[{trg_word}]]"
        qry = qry.replace(mod_trg_word, rep_word)
    return qry
