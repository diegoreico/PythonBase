from mymodule.analytics.usecases.list_clients import ListClientUseCase
from mymodule.common.infraestructure.abstract_engine import AbstractEngine
from mymodule.common.infraestructure.postgres_engine import PostgresEngine
from mymodule.analytics.infraestructure.abstract_clients_repository import AbstractClientsRepository
from mymodule.analytics.domain.services.client_manipulation_service import ClientManipulationService
from mymodule.analytics.domain.entities.client import Client
from typing import List

class TestClientRespositroy(AbstractClientsRepository):

    def __init__(self, engine: AbstractEngine) -> None:
        super().__init__(engine)
    def list(self) -> List[Client]:
        return [Client(id=1,active=1, prediction_horizon="patatas", airport=False, weather=False, lead_time=0)]

    def get(self, entitie: Client) -> Client:
        pass

    def add(self, entitie: Client) -> Client:
        pass

    def remove(self, entitie: Client) -> Client:
        pass

    def update(self, entitie: Client) -> Client:
        pass

def test_retrieves_list_of_clients():

    repo = TestClientRespositroy(None)
    uc = ListClientUseCase(repo, ClientManipulationService())
    uc.execute()

    result = uc.result
    assert len(result) > 0