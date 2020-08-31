import json
from abstract_json_storage import AbstractJsonStorage
import keys


class JsonBinStore(AbstractJsonStorage):
    def __init__(self):
        super().__init__()

    def get_name(self):
        return "jsonbin.io"

    def create(self, session, json_data=None, store_id=None):
        session.headers["X-Master-key"] = keys.JSONBIN_API_KEY
        return self._request(session, "post", "/b", json_data)

    def update(self, session, json_data=None, store_id=None):
        session.headers["X-Master-key"] = keys.JSONBIN_API_KEY
        id = store_id or self.store_id
        return self._request(session, "put", f"/b/{id}", json_data)

    def read(self, session, json_data=None, store_id=None):
        session.headers["X-Master-key"] = keys.JSONBIN_API_KEY
        id = store_id or self.store_id
        return self._request(session, "get", f"/b/{id}/latest", json_data)

    def result_callback(self, method_name, result_content):
        print(f"{method_name} : {result_content}")
        if method_name == "create":
            content = json.loads(result_content)
            bin_id = content["metadata"]["id"]
            self._set_store_id(bin_id)
        elif method_name == "read":
            content = json.loads(result_content)
            result = json.dumps(content["record"])
            return result

    def _get_api_root(self):
        return "https://api.jsonbin.io/v3"
