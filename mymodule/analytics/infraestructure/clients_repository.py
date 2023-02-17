
import logging
from typing import Any, List
from mymodule.analytics.infraestructure.abstract_clients_repository import AbstractClientsRepository
from mymodule.common.infraestructure.abstract_engine import AbstractEngine
from mymodule.analytics.domain.entities.client import Client

class ClientsRepository(AbstractClientsRepository):

    def __init__(self, engine: AbstractEngine) -> None:
        self._engine = engine

    def list(self) -> List[Client]:
        clients_rows = self._engine.query("SELECT * from public.clients")


        clients_list = [
            Client(
                id=row.id,
                active=row.active,
                prediction_horizon=row.prediction_horizon,
                airport=row.airport,
                weather=row.weather,
                lead_time=row.lead_time
                )
            for row in clients_rows
        ]

        return clients_list


    def get(self, entitie: Client) -> Client:
        pass

    def add(self, entitie: Client) -> Client:
        pass

    def remove(self, entitie: Client) -> Client:
        pass

    def update(self, entitie: Client) -> Client:
        pass