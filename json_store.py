from jsonbin_store import JsonBinStore
from jsonbox_store import JsonboxStore
from jsonstorage_store import JsonStorageStore
from json_mock_store import JsonMockstore
from requests_futures.sessions import FuturesSession


class JsonStore(object):
    def __init__(self):
        self.stores = []
        self._config_stores()

    def _config_stores(self):
        self.stores.append(JsonMockstore())
        self.stores.append(JsonMockstore())
        self.stores.append(JsonMockstore())
        # self.stores.append(JsonBinStore())
        # self.stores.append(JsonboxStore())
        # self.stores.append(JsonStorageStore())

    def create(self, json_data):
        tasks = []
        session = FuturesSession()
        for store in self.stores:
            tasks.append(store.create(json_data, session))

        results = []
        for task in tasks:
            result = task.result().content
            results.append(result)
            print(result)

        session.close()
        return results

    def update(self, store_id):
        pass

    def read(self, store_id):
        pass
