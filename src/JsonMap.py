import json

class JsonMap:
    def __init__(self, files_dict) -> None:
        self.files_json = json.dumps(files_dict, indent=4, sort_keys=True)
        with open("files.json", "w") as outfile:
            outfile.write(self.files_json)
    