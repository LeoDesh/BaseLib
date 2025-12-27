import pytest 
from base_lib.SQL.sql_helper import read_qry_from_file,qry_multiple_data
from pathlib import Path

@pytest.mark.slow
def test_qry_multiple_data(get_ms_sql_engine):
    main_path = Path(r"tests\SQL\ms_sql_qry")
    files = ["Course.sql","Student.sql"]
    qry_paths = [main_path / file for file in files]
    qry_contents = [read_qry_from_file(file) for file in qry_paths]
    qry_dict = {file:content for file,content in zip(files,qry_contents)}
    df_dict = qry_multiple_data(qry_dict,get_ms_sql_engine)
    for file in files:
        assert len(df_dict[file]) > 0
