from core.ports.create_client import CreateClientInterface
from core.use_cases.create_client_use_case import CreateClientUseCase
from infrastructure.repositories.create_client_repository import (
    CreateClientRepository,
)


def get_create_use_case() -> CreateClientInterface:
    return CreateClientUseCase(repository=CreateClientRepository())
