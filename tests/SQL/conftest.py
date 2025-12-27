import pytest 
from base_lib.SQL.sql_connection import create_lite_engine,create_ms_sql_engine
from base_lib.SQL.sql_helper import exec_sql


class SqlLiteTestDB:
    def __init__(self, db_path="sqlite:///tests/SQL/test.db"):
        self.db_path = db_path
        self.conn = create_lite_engine(db_path)


    def setup_schema(self):
        qry_users = """
            CREATE TABLE IF NOT EXISTS Users (
                id INTEGER PRIMARY KEY,
                name NVARCHAR(300)
            )
        """
        exec_sql(qry_users,self.conn)

    def insert_data(self):
        stmt = """Insert into Users
                Select 1,'Martin' UNION ALL SELECT 2,'David'
        """
        exec_sql(stmt,self.conn)

    def remove_data(self):
        stmt = "DROP TABLE IF EXISTS Users;"
        exec_sql(stmt,self.conn)

@pytest.fixture(scope="session", autouse=True)
def setup_environment():
    db = SqlLiteTestDB()
    db.remove_data()
    db.setup_schema()
    db.insert_data()
    yield db 
    db.remove_data()

@pytest.fixture(scope="session")
def get_lite_engine(setup_environment):
    db:SqlLiteTestDB = setup_environment
    return db.conn


@pytest.fixture(scope="session")
def get_ms_sql_engine():
    return create_ms_sql_engine()