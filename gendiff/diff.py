import json


def low_case(value):
    if isinstance(value, bool):
        return str(value).lower()
    return value


def generate_diff(file_path1, file_path2) -> str:
    js1 = json.load(open(file_path1))
    js2 = json.load(open(file_path2))

    united_keys = sorted(js1.keys() | js2.keys())

    stubs = []
    for key in united_keys:
        if key not in js1:
            stubs.append({"action": "added", "key": key, "value": js2[key]})
        elif key not in js2:
            stubs.append({"action": "deleted", "key": key, "value": js1[key]})
        elif key in js1 and key in js2:
            if js1[key] == js2[key]:
                stubs.append({"action": "unchanged", "key": key, "value": js1[key]})
            else:
                stubs.append(
                    {
                        "action": "modified",
                        "key": key,
                        "old_value": js1[key],
                        "new_value": js2[key],
                    }
                )
    lines = []
    lines.append("{")

    for item in stubs:
        if item["action"] == "added":
            lines.append(f"+ {item['key']}: {low_case(item['value'])}")
        elif item["action"] == "deleted":
            lines.append(f"- {item['key']}: {low_case(item['value'])}")
        elif item["action"] == "modified":
            lines.append(f"- {item['key']}: {low_case(item['old_value'])}")
            lines.append(f"+ {item['key']}: {low_case(item['new_value'])}")
        elif item["action"] == "unchanged":
            lines.append(f"  {item['key']}: {low_case(item['value'])}")
    lines.append("}")

    return "\n".join(lines)
