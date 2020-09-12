from abstract_json_storage import AbstractJsonStorage
import keys
import uuid


class PantryStore(AbstractJsonStorage):
    def __init__(self):
        super().__init__()

    def get_name(self):
        return "getpantry.cloud"

    def create(self, session, json_data=None, store_id=None):
        pantry_id = keys.PANTRY_ID
        basket_id = store_id or str(uuid.uuid4())
        self._set_store_id(basket_id)
        return self._request(session, "post", f"/pantry/{pantry_id}/basket/{basket_id}", json_data)

    def update(self, session, json_data=None, store_id=None):
        pass

    def read(self, session, json_data=None, store_id=None):
        pantry_id = keys.PANTRY_ID
        basket_id = self.store_id
        return self._request(session, "get", f"/pantry/{pantry_id}/basket/{basket_id}")

    def result_callback(self, method_name, result_content):
        print(f"{method_name} : {result_content}")
        if method_name == "create":
            return result_content
        if method_name == "read":
            return result_content

    def _get_api_root(self):
        return "https://getpantry.cloud/apiv1"
