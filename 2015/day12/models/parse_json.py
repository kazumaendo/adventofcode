import json


class JSONParser():
    def __init__(self, json_str: str) -> None:
        self.json_document = json.loads(json_str)
        print(self.json_document)
        print(f"Type: {type(self.json_document)}")
        print("---------------")
