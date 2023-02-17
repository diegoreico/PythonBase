
from abc import ABC, abstractmethod
from typing import Any, List


class AbstractRepository(ABC):

    @abstractmethod
    def list(self) -> List[Any]:
        pass

    @abstractmethod
    def get(self, entitie: Any) -> Any:
        pass

    @abstractmethod
    def add(self, entitie: Any) -> Any:
        pass

    @abstractmethod
    def remove(self, entitie: Any) -> Any:
        pass

    @abstractmethod
    def update(self, entitie: Any) -> Any:
        pass