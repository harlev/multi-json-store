from abstract_json_storage import AbstractJsonStorage
import json
import keys


class JsonboxStore(AbstractJsonStorage):
    def __init__(self):
        super().__init__()

    def get_name(self):
        return "jsonbox.io"

    def create(self, session, json_data=None, store_id=None):
        box_id = keys.BOX_ID
        return self._request(session, "post", f"/{box_id}", json_data)

    def update(self, session, json_data=None, store_id=None):
        box_id = keys.BOX_ID
        record_id = self.store_id
        return self._request(session, "put", f"/{box_id}/{record_id}", json_data)

    def read(self, session, json_data=None, store_id=None):
        box_id = keys.BOX_ID
        record_id = self.store_id
        return self._request(session, "get", f"/{box_id}/{record_id}")

    def result_callback(self, method_name, result_content):
        print(f"{method_name} : {result_content}")
        if method_name == "create":
            content = json.loads(result_content)
            object_id = content["_id"]
            self._set_store_id(object_id)
            return result_content
        if method_name == "read":
            content = json.loads(result_content)
            self._delete_if_exists(content, "_id")
            self._delete_if_exists(content, "_createdOn")
            self._delete_if_exists(content, "_updatedOn")
            return json.dumps(content)

    @staticmethod
    def _delete_if_exists(dict_obj, field_name):
        if field_name in dict_obj:
            del dict_obj[field_name]

    def _get_api_root(self):
        return "https://jsonbox.io"
