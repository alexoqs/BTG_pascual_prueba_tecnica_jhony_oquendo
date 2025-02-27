from core.ports.create_client import CreateClientInterface
from core.entities.client_entity import ClientEntity
from infrastructure.database.database import MongoDBConnection
from core.errors.exeptions import DatabaseException


class CreateClientRepository(CreateClientInterface):
    def __init__(self):
        self.db = MongoDBConnection.get_db()
        self.collection = self.db.client

    async def create_client(self, client: ClientEntity) -> ClientEntity:
        try:
            result = await self.collection.insert_one(client)
            return result
        except Exception as e:
            raise DatabaseException(f"Error creating client: {str(e)}")
