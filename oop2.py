import json
import os
import sys



class JsonReader:
    def __init__(self, path_file):
        self._path_file = path_file

    def __repr__(self):
        return self._path_file

    def read_json(self):
        with open(self._path_file, "r") as file:
            return json.load(file)



test = JsonReader(os.path.join("vlans", "VLANs.json"))
test2 = JsonReader(os.path.join("stasya", "hom9.json"))

print(test.read_json())
#print(test2.read_json())
print(sys.getsizeof(test), sys.getsizeof(test2))


class ListReader(JsonReader):
    pass

class DictReader(JsonReader):
    pass
