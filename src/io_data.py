import json

def read_json(file_path: str)-> dict:
    with open(file_path, "r") as fi:
        d = json.loads(fi.read())
    return d