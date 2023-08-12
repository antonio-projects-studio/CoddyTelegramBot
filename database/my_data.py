import json
from typing import Dict, List


class MyData():
    def __init__(self):
        with open('database/my_data.txt', 'r') as f:
            self.data: Dict[str, str] = json.load(f)

    def upload(self):
        with open('database/my_data.txt', 'w') as f:
            json.dump(self.data, f)

    def load(self, key: str):
        return self.data.get(key, "Нет ключа")

    def delete(self, key: str):
        self.data.pop(key, None)

    def list_keys(self) -> List[str]:
        list_keys = list(self.data.keys())
        return list_keys

    def update_data(self, data_for_update: Dict):
        self.data.update(data_for_update)
