from gendiff.diff import generate_diff


def test_compare_json_files():
    result = generate_diff("tests/test_data/file1.json", "tests/test_data/file2.json")
    with open("tests/test_data/expected_result.txt") as f:
        expected_result = f.read()
    assert result == expected_result
