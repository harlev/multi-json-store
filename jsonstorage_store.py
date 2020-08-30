import json
from urllib.parse import urlparse
from abstract_json_storage import AbstractJsonStorage


class JsonStorageStore(AbstractJsonStorage):
    def __init__(self):
        super().__init__()
        
    def get_name(self):
        return "jsonstorage.net"

    def create(self, session, json_data=None, store_id=None):
        return self._request(session, "post", "/api/items", json_data)

    def update(self, session, json_data=None, store_id=None):
        return self._request(session, "put", store_id or self.store_id, json_data)

    def read(self, session, json_data=None, store_id=None):
        return self._request(session, "get", store_id or self.store_id)

    def result_callback(self, method_name, result_content):
        print(f"{method_name} : {result_content}")
        if method_name == "create":
            content = json.loads(result_content)
            path_parts = urlparse(content["uri"])
            object_id = path_parts.path
            self._set_store_id(object_id)
        elif method_name == "read":
            return result_content

    def _get_api_root(self):
        # return "https://jsonstorage.net/api"
        return "https://jsonstorage.net"

