from abstract_json_storage import AbstractJsonStorage


class JsonboxStore(AbstractJsonStorage):
    def __init__(self):
        super().__init__()

    def create(self, json_data, session):
        return session.post(f"{self._get_api_root()}/api/users?delay=5")

    async def update(self, store_id, json_data):
        pass

    async def read(self, store_id):
        pass

    def _get_api_root(self):
        # return "https://jsonbox.io"
        return "https://reqres.in/api/users"
