def make_line(value, depth=0) -> str:
    indent = '    ' * depth
    line = []
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, dict):
        line.append('{')
        for k, v in value.items():
            line.append(f'{indent}    {k}: {make_line(v, depth + 1)}')
        line.append(indent + '}')
        return '\n'.join(line)
    return str(value)


def format_stylish(stubs, depth=0) -> str:
    lines = []
    indent = '    ' * depth
    lines.append("{")

    for stub in stubs:
        if stub["action"] == "added":
            lines.append(f"{indent}  + {stub['key']}: "
                         f"{make_line(stub['value'], depth + 1)}")

        elif stub["action"] == "deleted":
            lines.append(f"{indent}  - {stub['key']}: "
                         f"{make_line(stub['value'], depth + 1)}")

        elif stub["action"] == "modified":
            lines.append(f"{indent}  - {stub['key']}: "
                         f"{make_line(stub['old_value'], depth + 1)}")
            lines.append(f"{indent}  + {stub['key']}: "
                         f"{make_line(stub['new_value'], depth + 1)}")

        elif stub["action"] == "unchanged":
            lines.append(f"{indent}    {stub['key']}: "
                         f"{make_line(stub['value'], depth + 1)}")

        elif stub["action"] == "nested":
            lines.append(f"{indent}    {stub['key']}: "
                         f"{format_stylish(stub['children'], depth + 1)}")

    lines.append(indent + "}")
    return "\n".join(lines)
