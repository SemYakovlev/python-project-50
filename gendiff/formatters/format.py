from gendiff.formatters.json import format_json
from gendiff.formatters.plain import format_plain
from gendiff.formatters.stylish import format_stylish


def formatted(status, format_name):
    if format_name == "stylish":
        return format_stylish(status)
    elif format_name == "plain":
        return format_plain(status, prefix='')
    elif format_name == "json":
        return format_json(status)
    return format_stylish(status)