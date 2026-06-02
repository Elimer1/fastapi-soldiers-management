import json

def json_to_list(json_file):
    return json.load(json_file)

def list_to_json(py_list, filename):
    return json.dump(py_list, filename, indent = 2)