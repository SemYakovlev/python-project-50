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
