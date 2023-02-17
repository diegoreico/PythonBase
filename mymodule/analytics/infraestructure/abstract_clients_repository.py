
import logging
from typing import Any, List
from mymodule.common.infraestructure.abstract_repository import AbstractRepository
from mymodule.common.infraestructure.abstract_engine import AbstractEngine
from mymodule.analytics.domain.entities.client import Client

class AbstractClientsRepository(AbstractRepository):

    def __init__(self, engine: AbstractEngine) -> None:
        self._engine = engine

    def list(self) -> List[Client]:
        pass

    def get(self, entitie: Client) -> Client:
        pass

    def add(self, entitie: Client) -> Client:
        pass

    def remove(self, entitie: Client) -> Client:
        pass

    def update(self, entitie: Client) -> Client:
        pass