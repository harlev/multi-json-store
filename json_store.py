from jsonbin_store import JsonBinStore
from jsonbox_store import JsonboxStore
from jsonstorage_store import JsonStorageStore
from abstract_json_storage import AbstractJsonStorage
from json_mock_store import JsonMockstore
from requests_futures.sessions import FuturesSession


class RequestTask(object):
    def __init__(self, service_name, task):
        self.service_name = service_name
        self.task = task

    def get_name(self):
        return self.service_name

    def get_task(self):
        return self.task


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

    @staticmethod
    def _get_result_object(task: RequestTask):
        return {
            "service_name": task.get_name(),
            "result": task.get_task().result().content,
            "status_code": task.get_task().result().status_code
        }

    def _async_request(self, method_name, store_id=None, json_data=None):
        tasks = []
        session = FuturesSession()
        for store in self.stores:
            func = getattr(store, method_name)
            request_task = RequestTask(store.get_name(), func(session, json_data=json_data, store_id=store_id))
            tasks.append(request_task)

        results = []
        for task in tasks:
            result = self._get_result_object(task)
            results.append(result)
            print(result)

        session.close()
        return results

    def create(self, json_data):
        return self._async_request("create", json_data=json_data)

    def update(self, store_id, json_data):
        return self._async_request("update", store_id=store_id, json_data=json_data)

    def read(self, store_id):
        return self._async_request("read", store_id=store_id)
