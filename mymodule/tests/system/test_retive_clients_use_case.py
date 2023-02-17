from mymodule.analytics.usecases.list_clients import ListClientUseCase
from mymodule.common.infraestructure.postgres_engine import PostgresEngine
from mymodule.analytics.infraestructure.clients_repository import ClientsRepository

def test_retrieves_list_of_clients():

    engine = PostgresEngine()
    client_repository = ClientsRepository(engine)
    uc = ListClientUseCase(client_repository)
    uc.execute()

    result = uc.result
    assert len(result) > 0