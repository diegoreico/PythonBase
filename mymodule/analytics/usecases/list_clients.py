import logging
from typing import List

from mymodule.common.usecases.base import BaseUseCase
from mymodule.analytics.infraestructure.abstract_clients_repository import AbstractClientsRepository
from mymodule.analytics.domain.services.client_manipulation_service import ClientManipulationService

class ListClientUseCase(BaseUseCase):
    
    def __init__(self,
                 clients_repository: AbstractClientsRepository,
                 manipulation_service: ClientManipulationService
                 ):
        super().__init__()

        self._clients_repository = clients_repository
        self._manipulation_service = manipulation_service
        self._result = None

    @property
    def result(self) -> List[str]:
        return self._result

    def execute(self):
        logging.info("Running sey hello use case")
        client_list = self._clients_repository.list()

        self._result = self._manipulation_service.extract_names(client_list)
        
