from base_lib.utils.regex import regex_get_all_matches, regex_match, regex_match_exists
import pytest


@pytest.mark.fast
def test_regex_match_exists_positive():
    text = "Text1 T2345 T7"
    pattern = r"5\sT(\d{1})"
    assert regex_match_exists(text, pattern)


@pytest.mark.fast
def test_regex_match_exists_negative():
    text = "Text1 T2345 T7"
    pattern = r"4sT(\d{1})"
    assert not regex_match_exists(text, pattern)


@pytest.mark.fast
def test_regex_match_positive():
    text = "Text1 T2345 T7"
    pattern = r"5\sT(\d{1})"
    assert regex_match(text, pattern) == "5 T7"


@pytest.mark.fast
def test_regex_match_negative():
    text = "Text1 T2345 T7"
    pattern = r"4sT(\d{1})"
    assert regex_match(text, pattern) == ""


@pytest.mark.fast
def test_regex_match_positive_group():
    text = "Text1 T2345 T7"
    pattern = r"5\sT(\d{1})"
    assert regex_match(text, pattern, 1) == "7"


@pytest.mark.fast
def test_get_regex_all_matches_positive():
    text = "Text1 T2345 T7"
    pattern = r"\sT(\d{1})"
    result = ["2", "7"]
    assert regex_get_all_matches(text, pattern, 1) == result

@pytest.mark.fast
def test_get_regex_all_matches_negative():
    text = "Text1 T2345 T7"
    pattern = r"6\sT(\d{1})"
    assert regex_get_all_matches(text, pattern, 1) == []
