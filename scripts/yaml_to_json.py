"""
This script converts all yaml files in the current directory to json files.
Currently used for the development of the self-service project.
"""

import yaml, json
import os

for file in os.listdir():
    if file.endswith(".yaml"):
        with open(file, "r") as yaml_file:
            data = yaml.load(yaml_file, Loader=yaml.FullLoader)
        with open(file.replace(".yaml", ".json"), "w") as json_file:
            json.dump(data, json_file)