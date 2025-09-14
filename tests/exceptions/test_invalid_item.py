"""Test cases for all exceptions in Invalid Item logic."""

import pytest
from typing import Optional, Any
from gilded_rose import GildedRose
from exceptions import (
    GildedRoseException,
    InvalidItemException,
)


class InvalidItem:
    def __init__(
        self,
        name: Optional[Any] = None,
        sell_in: Optional[Any] = None,
        quality: Optional[Any] = None,
    ):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality


def test_invalid_item_exception_basic():
    with pytest.raises(InvalidItemException) as exc_info:
        raise InvalidItemException("Invalid item data")

    assert str(exc_info.value) == "Invalid item data"
    assert exc_info.value.message == "Invalid item data"
    assert exc_info.value.item_name is None


def test_invalid_item_exception_with_item_name():
    with pytest.raises(InvalidItemException) as exc_info:
        raise InvalidItemException("Invalid quality value", "Test Item")

    assert str(exc_info.value) == "Invalid quality value (Item: Test Item)"
    assert exc_info.value.message == "Invalid quality value"
    assert exc_info.value.item_name == "Test Item"


def test_invalid_item_exception_inheritance():
    with pytest.raises(GildedRoseException) as exc_info:
        raise InvalidItemException("Invalid item")

    assert isinstance(exc_info.value, InvalidItemException)
    assert isinstance(exc_info.value, GildedRoseException)


def test_gilded_rose_raises_exception_name():
    items = [InvalidItem()]
    gilded_rose = GildedRose(items)

    with pytest.raises(
        InvalidItemException,
        match="Item must have name attribute",
    ):
        gilded_rose.update_quality()


def test_gilded_rose_raises_exception_name_str():
    items = [InvalidItem(1, 10, 80)]
    gilded_rose = GildedRose(items)

    with pytest.raises(
        InvalidItemException,
        match="Name must be a str, got int",
    ):
        gilded_rose.update_quality()


def test_gilded_rose_raises_exception_sell_in():
    items = [InvalidItem(name="Test Item", quality=80)]
    gilded_rose = GildedRose(items)

    with pytest.raises(
        InvalidItemException,
        match="Item must have sell_in attribute",
    ):
        gilded_rose.update_quality()


def test_gilded_rose_raises_exception_sell_in_str():
    items = [InvalidItem("Test Item", "10", 80)]
    gilded_rose = GildedRose(items)

    with pytest.raises(
        InvalidItemException,
        match="Sell_in must be a int, got str",
    ):
        gilded_rose.update_quality()


def test_gilded_rose_raises_exception_quality():
    items = [InvalidItem("Test Item", 10)]
    gilded_rose = GildedRose(items)

    with pytest.raises(
        InvalidItemException,
        match="Item must have quality attribute",
    ):
        gilded_rose.update_quality()


def test_gilded_rose_raises_exception_quality_str():
    items = [InvalidItem("Test Item", 10, "10")]
    gilded_rose = GildedRose(items)

    with pytest.raises(
        InvalidItemException,
        match="Quality must be a int, got str",
    ):
        gilded_rose.update_quality()
