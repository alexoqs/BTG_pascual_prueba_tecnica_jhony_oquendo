from abc import ABC, abstractmethod
from core.entities.client_entity import ClientEntity


class CreateClientInterface(ABC):
    @abstractmethod
    def create_client(self, name, lastname, city) -> ClientEntity:
        pass
