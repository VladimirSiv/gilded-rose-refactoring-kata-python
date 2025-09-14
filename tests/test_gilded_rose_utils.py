"""Test cases for utility functions."""

import pytest
from utils import normalize_item_name


@pytest.mark.parametrize(
    "input_name, expected",
    [
        ("  Foo  ", "foo"),
        ("Foo   Bar", "foo bar"),
        ("FOO-BAR", "foo-bar"),
        (" Foo!@#Bar ", "foobar"),
        ("   ", ""),
        ("", ""),
        (None, ""),
        (0, ""),
        ("Foo   -   Bar", "foo - bar"),
    ],
)
def test_normalize_item_name(input_name, expected):
    assert normalize_item_name(input_name) == expected
