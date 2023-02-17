import logging
from typing import List

from mymodule.common.usecases.base import BaseUseCase
from mymodule.analytics.infraestructure.clients_repository import ClientsRepository

class ListClientUseCase(BaseUseCase):
    
    def __init__(self,
                 clients_repository: ClientsRepository):
        super().__init__()

        self._clients_repository = clients_repository

        self._result = None

    @property
    def result(self) -> List[str]:
        return self._result

    def execute(self):
        logging.info("Running sey hello use case")
        client_list = self._clients_repository.list()

        self._result = [client.id for client in client_list]
