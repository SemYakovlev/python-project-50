import json

import yaml


def define_format(file_path):
    with open(file_path) as f:
        file_data = f.read()
    if file_path.endswith("json"):
        return json.loads(file_data)
    elif file_path.endswith("yml"):
        return yaml.safe_load(file_data)


def low_case(value):
    if isinstance(value, bool):
        return str(value).lower()
    return value


def generate_diff(file_path1, file_path2) -> str:
    dict1 = define_format(file_path1)
    dict2 = define_format(file_path2)

    united_keys = sorted(dict1.keys() | dict2.keys())

    stubs = []
    for key in united_keys:
        if key not in dict1:
            stubs.append({"action": "added", "key": key, "value": dict2[key]})
        elif key not in dict2:
            stubs.append({"action": "deleted", "key": key, "value": dict1[key]})
        elif key in dict1 and key in dict2:
            if dict1[key] == dict2[key]:
                stubs.append({"action": "unchanged", "key": key, "value": dict1[key]})
            else:
                stubs.append(
                    {
                        "action": "modified",
                        "key": key,
                        "old_value": dict1[key],
                        "new_value": dict2[key],
                    }
                )

    lines = []
    lines.append("{")

    for item in stubs:
        if item["action"] == "added":
            lines.append(f"  + {item['key']}: {low_case(item['value'])}")
        elif item["action"] == "deleted":
            lines.append(f"  - {item['key']}: {low_case(item['value'])}")
        elif item["action"] == "modified":
            lines.append(f"  - {item['key']}: {low_case(item['old_value'])}")
            lines.append(f"  + {item['key']}: {low_case(item['new_value'])}")
        elif item["action"] == "unchanged":
            lines.append(f"    {item['key']}: {low_case(item['value'])}")
    lines.append("}")

    return "\n".join(lines)
