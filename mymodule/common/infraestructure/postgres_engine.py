import logging
from sqlalchemy import create_engine, text
from typing import Any

from sqlalchemy.engine.row import Row

from mymodule.common.infraestructure.abstract_engine import AbstractEngine
from mymodule.common.configuration.config import DBConfig


class PostgresEngine(AbstractEngine):
    def __init__(self, config: DBConfig = DBConfig()):
        self._db_config = config
        self._engine = None

        self.connect()

    def connect(self):
        user = self._db_config.USER
        pwd = self._db_config.PASS
        host = self._db_config.HOST
        port = self._db_config.PORT
        dbname = self._db_config.DB

        connection_query = (
            "postgresql://"
            + user
            + ":"
            + pwd
            + "@"
            + host
            + ":"
            + str(port)
            + "/"
            + dbname
        )

        logging.info(f"Connecting to database {connection_query}")
        self._engine = create_engine(connection_query)

    def test_connection(self) -> bool:
        result = []
        with self._engine.connect() as connection:
            result = connection.execute(text("SELECT 1")).all()

        return len(result) == 1
 

    def execute(self, sql: str) -> None:
        
        with self._engine.connect() as connection:
            connection.execute(text(sql))


    def query(self, sql: str) -> list[Row]:
        result = None
        with self._engine.connect() as connection:
            result = connection.execute(text(sql)).all()

        return result
