import json

import yaml


def define_format(file_path):
    with open(file_path) as f:
        file_data = f.read()
    if file_path.endswith("json"):
        return json.loads(file_data)
    elif file_path.endswith(("yml", "yaml")):
        return yaml.safe_load(file_data)


def generate_stubs(dict1, dict2) -> list:
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


def make_line(value, depth=0):
    indent = '    ' * depth
    line = []
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, dict):
        line.append('{')
        for k, v in value.items():
            line.append(f'{indent}    {k}: {make_line(v, depth+1)}')
        line.append(indent + '}')
        return ('\n').join(line)


def format_stylish(stubs, depth=0) -> str:
    lines = []
    indent = '    ' * depth
    lines.append("{")

    for stub in stubs:
        if stub["action"] == "added":
            lines.append(f"  + {stub['key']}: {make_line(stub['value'])}")

        elif stub["action"] == "deleted":
            lines.append(f"  - {stub['key']}: {make_line(stub['value'])}")

        elif stub["action"] == "modified":
            lines.append(f"  - {stub['key']}: {make_line(stub['old_value'])}")
            lines.append(f"  + {stub['key']}: {make_line(stub['new_value'])}")

        elif stub["action"] == "unchanged":
            lines.append(f"    {stub['key']}: {make_line(stub['value'])}")

        elif stub["action"] == "nested":
            lines.append(f"    {stub['key']}: {make_line(stub['children'], depth+1)}") 

    lines.append("}")
    return "\n".join(lines)


def generate_diff(file_path1, file_path2, format_name="stylish"):
    dict1 = define_format(file_path1)
    dict2 = define_format(file_path2)
    status = generate_stubs(dict1, dict2)
    if format_name == "stylish":
        return format_stylish(status)

    return format_stylish(status)
