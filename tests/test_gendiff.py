import pytest
from gendiff.diff import generate_diff
import json

@pytest.mark.parametrize(
    "ext, expected_result, format_name",
    [
        ("json", "expected_result.txt", "stylish"),
        ("yml", "expected_result_yaml", "stylish"),
        ("json", "expected_result_plain", "plain"),
        ("json", "expected_result.json", "json"),
    ]
)

def test_compare_files(ext, expected_result, format_name):
    result = generate_diff(
        f"tests/test_data/file1.{ext}",
        f"tests/test_data/file2.{ext}",
        format_name=format_name,
    )
    with open(f"tests/test_data/{expected_result}") as f:
        expected_result = f.read()
    assert result == expected_result


# def test_compare_json_files():
#     result = generate_diff("tests/test_data/file1.json",
#                            "tests/test_data/file2.json",
#                            format_name="stylish")
#     with open("tests/test_data/expected_result.txt") as f:
#         expected_result = f.read()
#     assert result == expected_result
#
#
# def test_compare_yaml_files():
#     result = generate_diff("tests/test_data/file1.yml",
#                            "tests/test_data/file2.yml",
#                            format_name="stylish")
#     with open("tests/test_data/expected_result_yaml") as f:
#         expected_result = f.read()
#     assert result == expected_result
#
#
# def test_compare_json_plain():
#     result = generate_diff("tests/test_data/file1.json",
#                            "tests/test_data/file2.json",
#                            format_name="plain")
#     with open("tests/test_data/expected_result_plain") as f:
#         expected_result = f.read()
#     assert result == expected_result
#
#
# def test_compare_two_jsons():
#     result = generate_diff("tests/test_data/file1.json",
#                            "tests/test_data/file2.json",
#                            format_name="json")
#     with open("tests/test_data/expected_result.json") as f:
#         expected_result = json.load(f)
#         result = json.loads(result)
#     assert result == expected_result
