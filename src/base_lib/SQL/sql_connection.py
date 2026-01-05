from __future__ import annotations
from sqlalchemy.engine import URL, create_engine
from typing import Protocol
from base_lib.SQL.sql_config import SERVER_INFO


class SqlEngine(Protocol):
    def connect(self) -> Connection:
        pass


class Connection(Protocol):
    def __enter__(self) -> Connection:
        pass  # returned as the variable after "as"

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def commit(self):
        pass

    def execute(self, text: str):
        pass


class MS_SQL_ConnectionHandler:
    def __init__(self, driver: str, db: str, server: str, trusted: str):
        self.DRIVER = driver
        self.DATABASE = db
        self.SERVER = server
        self.TRUSTED_CONNECTION = trusted

    def connection_string(self):
        # return f"DRIVER={self.DRIVER};SERVER={self.SERVER};DATABASE={self.DATABASE};TrustServerCertificate={self.TRUSTED_CONNECTION}"
        return f"DRIVER={self.DRIVER};SERVER={self.SERVER};DATABASE={self.DATABASE};Trusted_Connection={self.TRUSTED_CONNECTION}"

    def create_engine(self) -> SqlEngine:
        conn_str = self.connection_string()
        connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": conn_str})
        return create_engine(connection_url)


def create_postgres_sql_engine(
    postgres_db: str, postgres_user: str, postgres_pw: str, db_host: str, db_port: str
) -> SqlEngine:
    connection_str = f"postgresql+psycopg2://{postgres_user}:{postgres_pw}@{db_host}:{db_port}/{postgres_db}"
    return create_engine(connection_str)


def create_mysql_engine(mysql_db: str, mysql_user: str, mysql_pw: str, db_host: str, db_port: str) -> SqlEngine:
    connection_str = f"mysql+pymysql://{mysql_user}:{mysql_pw}@{db_host}:{db_port}/{mysql_db}"
    return create_engine(connection_str)


def create_ms_sql_engine() -> SqlEngine:
    conn = MS_SQL_ConnectionHandler(**SERVER_INFO)
    return conn.create_engine()


def create_lite_engine(db_path: str = "sqlite:///response.db") -> SqlEngine:
    return create_engine(db_path)


SERVER_ENGINE: SqlEngine = create_ms_sql_engine()
