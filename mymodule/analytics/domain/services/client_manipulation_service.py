from mymodule.analytics.domain.entities.client import Client
from typing import List

class ClientManipulationService():

    def extract_names(self, clients: List[Client]) -> List[str]:
        return [client.id for client in clients]