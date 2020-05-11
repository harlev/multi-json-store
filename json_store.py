from jsonbin_store import JsonBinStore
from jsonbox_store import JsonboxStore
from jsonstorage_store import JsonStorageStore


class JsonStore(object):
    def __init__(self):
        self.stores = []
        self._config_stores()

    def _config_stores(self):
        self.stores.append(JsonBinStore())
        self.stores.append(JsonboxStore())
        self.stores.append(JsonStorageStore())

    def create(self):
        pass

    def update(self, store_id):
        pass

    def read(self, store_id):
        pass
