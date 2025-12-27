import pytest 
from base_lib.SQL.sql_helper import qry_data,SqlEngine
from sqlalchemy import text
import pandas as pd
@pytest.mark.slow
def test_load_sql_lite_data(get_lite_engine):
    qry = "SELECT * from Users"
    df = qry_data(qry,get_lite_engine)
    assert len(df) > 0

@pytest.mark.slow
def test_insert_sql_lite_data(get_lite_engine):
    engine:SqlEngine = get_lite_engine
    with engine.connect() as conn:
        stmt = "Insert into Users Select 14,'Markus'"
        conn.execute(text(stmt))
        qry = "Select * FROM Users"
        df = pd.read_sql(qry,conn)
        assert len(df) > 2


@pytest.mark.slow
def test_update_sql_lite_data(get_lite_engine):
    engine:SqlEngine = get_lite_engine
    with engine.connect() as conn:
        stmt = "Update Users Set Name = 'Martina' Where Name = 'Martin'"
        conn.execute(text(stmt))
        qry = "Select * FROM Users Where Name = 'Martin'"
        df = pd.read_sql(qry,conn)
        assert len(df) == 0