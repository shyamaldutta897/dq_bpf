import json


def load_config(config_path):
    with open(config_path) as file:
        return json.load(file)  

