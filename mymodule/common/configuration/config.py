import os
from dotenv import load_dotenv

import logging

from mymodule.common.errors.aplication_exception import (
    AplicationException,
)


load_dotenv(".env")


class InvalidConfig(AplicationException):
    def __init__(
        self, description: str, root_exception: Exception = None, *args: object
    ) -> None:

        self.description = description

        super().__init__(root_exception, *args)


class LoggingConfig:
    LEVEL = os.getenv(key="LOG_LEVEL", default=logging.INFO)

    def __init__(self) -> None:
        config_to_levels = {
            "CRITICAL": logging.CRITICAL,
            "ERROR": logging.ERROR,
            "WARNING": logging.WARNING,
            "INFO": logging.INFO,
            "DEBUG": logging.DEBUG,
            "NOTSET": logging.NOTSET,
        }

        if self.LEVEL not in config_to_levels.keys():
            raise InvalidConfig(
                "Supported config for logging levels are: {}".format(
                    self.LEVEL
                )
            )

        self.LEVEL = config_to_levels[self.LEVEL]


class DBConfig:
    HOST = os.getenv("DB_HOST")
    PORT = os.getenv("DB_PORT")
    DB = os.getenv("DB_DB")
    USER = os.getenv("DB_USER")
    PASS = os.getenv("DB_PASS")

    def __init__(self) -> None:

        if (
            self.HOST is None
            or self.PORT is None
            or self.DB is None
            or self.USER is None
            or self.PASS is None
        ):

            raise InvalidConfig(
                "All fields for DB config should be provided"
            )
