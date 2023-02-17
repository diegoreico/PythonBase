from mymodule.common.infraestructure.postgres_engine import PostgresEngine

def test_engine_can_connect_to_database():
    engine = PostgresEngine()
    connected = engine.test_connection()
    assert connected
