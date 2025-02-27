from core.ports.create_client import CreateClientInterface
from core.entities.client_entity import ClientEntity
from core.errors.exeptions import ValidationException


class CreateClientUseCase:
    def __init__(self, repository: CreateClientInterface):
        self.repository = repository

    async def create_client(
        self, name: str, lastname: str, city: str
    ) -> ClientEntity:
        if not name:
            raise ValidationException('Name is required')
        if not lastname:
            raise ValidationException('Lastname is required')
        if not city:
            raise ValidationException('City is required')
        client = ClientEntity(name, lastname, city)
        return await self.repository.create_client(client)
