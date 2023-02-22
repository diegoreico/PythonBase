from abc import ABC, abstractmethod
from typing import Any


class AbstractEngine(ABC):
    @abstractmethod
    def execute(sql: str) -> bool:
        pass

    @abstractmethod
    def query(sql: str) -> Any:
        pass
