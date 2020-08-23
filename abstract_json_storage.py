from abc import ABC, abstractmethod


class AbstractJsonStorage(ABC):
    def __init__(self):
        self.store_id = ""

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def create(self, session, json_data=None, store_id=None):
        pass

    @abstractmethod
    async def update(self, session, json_data=None, store_id=None):
        pass

    @abstractmethod
    def read(self, session, json_data=None, store_id=None):
        pass

    @abstractmethod
    def _get_api_root(self):
        pass

    @abstractmethod
    def result_callback(self, method_name, result_content):
        pass

    def _request(self, session, method_name, api_route, json_data=None):
        func = getattr(session, method_name)
        return func(f"{self._get_api_root()}{api_route}", data=json_data)

    def _set_store_id(self, store_id):
        print(f"New store ID {store_id}")
        self.store_id = store_id
