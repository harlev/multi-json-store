from abc import ABC, abstractmethod


class AbstractJsonStorage(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def create(self, json_data, session):
        pass

    @abstractmethod
    async def update(self, store_id, json_data):
        pass

    @abstractmethod
    async def read(self, store_id):
        pass

    @abstractmethod
    def _get_api_root(self):
        pass
