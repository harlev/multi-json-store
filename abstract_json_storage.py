from abc import ABC, abstractmethod


class AbstractJsonStorage(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def create(self, json_data):
        pass

    @abstractmethod
    def update(self, store_id, json_data):
        pass

    @abstractmethod
    def read(self, store_id):
        pass
