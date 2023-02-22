
from typing import List
from mymodule.common.infraestructure.postgres_engine import PostgresEngine
from mymodule.analytics.infraestructure.clients_repository import ClientsRepository
from mymodule.analytics.usecases.list_clients import ListClientUseCase
from mymodule.analytics.domain.services.client_manipulation_service import ClientManipulationService

class AnalyticsController:
    def __init__(self) -> None:
        self._engine = PostgresEngine()
        self._clients_repository = ClientsRepository(self._engine)
        self._manipulation_service = ClientManipulationService()

    def list_clients(self) -> List[str]:
        uc = ListClientUseCase(self._clients_repository, self._manipulation_service)
        uc.execute()
        
        return uc.result
