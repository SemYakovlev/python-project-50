import json

import yaml

from .formatters.stylish import format_stylish


def generate_stubs(dict1, dict2) -> list[dict]:
    united_keys = sorted(dict1.keys() | dict2.keys())

    stubs = []
    for key in united_keys:
        if key not in dict1:
            stubs.append(
                {
                    "action": "added", 
                    "key": key, 
                    "value": dict2[key]
                }
            )
        elif key not in dict2:
            stubs.append(
                {
                    "action": "deleted",
                    "key": key,
                    "value": dict1[key]
                }
            )
        elif key in dict1 and key in dict2:
            if dict1[key] == dict2[key]:
                stubs.append(
                    {
                        "action": "unchanged", 
                        "key": key, 
                        "value": dict1[key]
                    }
                )
            elif isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
                stubs.append(
                    {
                        "action": "nested", 
                        "key": key, 
                        "children": generate_stubs(dict1[key], dict2[key]) 
                    }
                )    
            else:
                stubs.append(
                    {
                        "action": "modified",
                        "key": key,
                        "old_value": dict1[key],
                        "new_value": dict2[key],
                    }
                )   
    return stubs


def define_format(file_path):
    with open(file_path) as f:
        file_data = f.read()
    if file_path.endswith("json"):
        return json.loads(file_data)
    elif file_path.endswith(("yml", "yaml")):
        return yaml.safe_load(file_data)


def generate_diff(file_path1, file_path2, format_name="stylish"):
    dict1 = define_format(file_path1)
    dict2 = define_format(file_path2)
    status = generate_stubs(dict1, dict2)
    if format_name == "stylish":
        return format_stylish(status)
    return format_stylish(status)