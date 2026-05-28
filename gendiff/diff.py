import json

import yaml

from gendiff.formatters.format import formatted
from gendiff.stubs import generate_stubs


def read_file(file_path):
    with open(file_path) as f:
        file_data = f.read()
    if file_path.endswith("json"):
        return json.loads(file_data)
    elif file_path.endswith(("yml", "yaml")):
        return yaml.safe_load(file_data)
    return None


def generate_diff(file_path1, file_path2, format_name="stylish"):
    dict1 = read_file(file_path1)
    dict2 = read_file(file_path2)
    status = generate_stubs(dict1, dict2)
    return formatted(status, format_name)