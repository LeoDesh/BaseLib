import pytest
from base_lib.data_transformation.value_validation import (
    parse_datetime,
    parse_float,
    parse_int,
    determine_type,
    format_value,
    determine_column_date_type,
    determine_column_float_type,
    determine_column_integer_type,
    determine_column_type,
)
from datetime import datetime


@pytest.mark.fast
@pytest.mark.parametrize(
    "value,expected_type",
    [
        ("20251208", datetime),
        ("2025-12-08", datetime),
        ("20251232", str),
        ("12.12.2025", datetime),
        ("12121945", datetime),
        ("121245", datetime),
        ("145432", str),
    ],
)
def test_parse_datetime(value, expected_type):
    assert parse_datetime(value) is expected_type


@pytest.mark.fast
@pytest.mark.parametrize(
    "value,expected_type",
    [
        ("145432", int),
        ("20251232", int),
        ("12.12.2025", str),
    ],
)
def test_parse_int(value, expected_type):
    assert parse_int(value) is expected_type


@pytest.mark.fast
@pytest.mark.parametrize(
    "value,expected_type",
    [
        ("145432", float),
        ("202512.32", float),
        ("12.12.2025", str),
        ("12,025", str),
    ],
)
def test_parse_float(value, expected_type):
    assert parse_float(value) is expected_type


@pytest.mark.fast
@pytest.mark.parametrize(
    "value,expected_type",
    [
        ("145432", int),
        ("202512.32", float),
        ("12.12.2025", datetime),
        ("12,025", str),
        ("20251232", int),
    ],
)
def test_determine_type(value, expected_type):
    assert determine_type(value) is expected_type


@pytest.mark.fast
@pytest.mark.parametrize(
    "value,result",
    [
        ("145432", "145432"),
        (145432, "145432"),
        ("145432  ", "145432"),
        ("11 22 33", "11 22 33"),
    ],
)
def test_format_value(value, result):
    assert format_value(value) == result


@pytest.mark.fast
@pytest.mark.parametrize(
    "values,choice",
    [
        ((3, 5, 7, "hi"), False),
        ((3, "5", 7, 12), True),
        ([], True),
        ((3, 5, 7, 12), True),
    ],
)
def test_determine_column_integer_type(values, choice):
    assert determine_column_integer_type(values) is choice


@pytest.mark.fast
@pytest.mark.parametrize(
    "values,choice",
    [
        ((3, 5, 7, "hi"), False),
        ((3, "5.5", 7, 12), True),
        ([], True),
        ((3, "5.5", 7, "2,5"), False),
        (("2.5", "4.5", "8.74545454"), True),
    ],
)
def test_determine_column_float_type(values, choice):
    assert determine_column_float_type(values) is choice


@pytest.mark.fast
@pytest.mark.parametrize(
    "values,choice",
    [
        ((3, 5, 7, "hi"), False),
        (("15031945","14.02.68","17.03.1984 23:15:03"), True),
    ],
)
def test_determine_column_date_type(values, choice):
    assert determine_column_date_type(values) is choice


@pytest.mark.fast
@pytest.mark.parametrize(
    "values,result_type",
    [
        ((3, 5, 7, "hi"), str),
        (("15031945","14.02.68","17.03.1984 23:15:03"), datetime),
        (("15031945","22040907","17011968"), int),
        (("15031945","22040907","3.4568"), float),
    ],
)
def test_determine_column_type(values, result_type):
    assert determine_column_type(values) is result_type