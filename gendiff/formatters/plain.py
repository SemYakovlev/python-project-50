def make_string(value) -> str:
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    if isinstance(value, dict):
        return "[complex value]"
    if isinstance(value, str):
        return f"'{value}'"
    return str(value)


def format_plain(stubs, prefix=''):
    lines = []
    for stub in stubs:
        if stub["action"] == "added":
            lines.append(f"Property '{prefix}{stub['key']}' "
                         f"was added with value: {make_string(stub['value'])}")
        elif stub["action"] == "deleted":
            lines.append(f"Property '{prefix}{stub['key']}' was removed")
        elif stub["action"] == "modified":
            lines.append(f"Property '{prefix}{stub['key']}' "
                         f"was updated. From {make_string(stub['old_value'])} "
                         f"to {make_string(stub['new_value'])}")
        elif stub['action'] == "nested":
            lines.append(format_plain(stub["children"], f'{prefix}{stub["key"]}.'))
    return '\n'.join(lines)