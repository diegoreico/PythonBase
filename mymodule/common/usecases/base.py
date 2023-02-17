from abc import ABC, abstractmethod
from typing import Any

class BaseUseCase(ABC):

    def __init__(self):
        super().__init__()
        self._result = None

    @property
    @abstractmethod
    def result() -> Any:
        pass

    @abstractmethod
    def execute(self) -> None:
        pass
