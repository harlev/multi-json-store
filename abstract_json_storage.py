from abc import ABC, abstractmethod


class AbstractJsonStorage(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def get_name(self):
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

    def _request(self, session, method_name, api_route, json_data):
        func = getattr(session, method_name)
        return func(f"{self._get_api_root()}{api_route}", json_data)
