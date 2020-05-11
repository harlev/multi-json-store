from abstract_json_storage import AbstractJsonStorage


class JsonStorageStore(AbstractJsonStorage):
    def __init__(self):
        self.homepage = "https://jsonstorage.net/"
        super().__init__()
        
    def create(self, json_data):
        pass

    def update(self, store_id, json_data):
        pass

    def read(self, store_id):
        pass

