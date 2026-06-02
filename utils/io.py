import json

def json_to_list():
    with open("soldiers.json", "r") as f:
        return json.load(f)

def list_to_json(py_list):
    with open("soldiers.json", "w") as f:
        return json.dump(py_list, f, indent = 2)