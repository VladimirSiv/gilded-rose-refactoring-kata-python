"""Test cases for all exceptions related to Gilded Rose Exception"""

import pytest
from gilded_rose import GildedRose
from items import Item
from exceptions import (
    GildedRoseException,
    InvalidItemException,
    StrategyUpdateException,
    AgedBrieStrategyUpdateException,
)


def test_gilded_rose_exception_without_item_name():
    with pytest.raises(GildedRoseException) as exc_info:
        raise GildedRoseException("Test error message")

    assert str(exc_info.value) == "Test error message"
    assert exc_info.value.message == "Test error message"
    assert exc_info.value.item_name is None


def test_gilded_rose_exception_with_item_name():
    with pytest.raises(GildedRoseException) as exc_info:
        raise GildedRoseException("Test error message", "Test Item")

    assert str(exc_info.value) == "Test error message (Item: Test Item)"
    assert exc_info.value.message == "Test error message"
    assert exc_info.value.item_name == "Test Item"


def test_gilded_rose_exception_inheritance():
    with pytest.raises(Exception) as exc_info:
        raise GildedRoseException("Test error")

    assert isinstance(exc_info.value, GildedRoseException)
    assert isinstance(exc_info.value, Exception)


def test_gilded_rose_invalid_items_parameter():
    with pytest.raises(ValueError, match="Items must be a list"):
        GildedRose("not a list")

    with pytest.raises(ValueError, match="Items must be a list"):
        GildedRose(None)

    with pytest.raises(ValueError, match="Items must be a list"):
        GildedRose(123)


def test_gilded_rose_valid_items_parameter():
    items = [Item("Test Item", 10, 20)]
    gilded_rose = GildedRose(items)
    assert gilded_rose.items == items


def test_gilded_rose_handles_none_items():
    items = [
        Item("Test Item", 10, 20),
        None,
        Item("Another Item", 5, 15),
    ]
    gilded_rose = GildedRose(items)
    with pytest.raises(
        InvalidItemException,
        match="Item must not be None",
    ):
        gilded_rose.update_quality()


def test_gilded_rose_handles_empty_list():
    gilded_rose = GildedRose([])
    gilded_rose.update_quality()


def test_gilded_rose_strategy_update_exception(mocker):
    fake_validator = mocker.Mock()
    fake_validator.validate.side_effect = AgedBrieStrategyUpdateException("boom")

    items = [Item("Test Item", 10, 10)]
    gilded_rose = GildedRose(items)
    gilded_rose.validator = fake_validator

    with pytest.raises(StrategyUpdateException) as exc_info:
        gilded_rose.update_quality()

    assert "boom" in str(exc_info.value)


def test_gilded_rose_broad_exception(mocker):
    fake_validator = mocker.Mock()
    fake_validator.validate.side_effect = RuntimeError("boom")

    items = [Item("Test Item", 10, 10)]
    gilded_rose = GildedRose(items)
    gilded_rose.validator = fake_validator

    with pytest.raises(Exception) as exc_info:
        gilded_rose.update_quality()

    assert "boom" in str(exc_info.value)


def test_gilded_rose_item_validation_exception(mocker):
    fake_validator = mocker.Mock()
    fake_validator.validate.side_effect = InvalidItemException("boom")

    items = [Item("Test Item", 10, 10)]
    gilded_rose = GildedRose(items)
    gilded_rose.validator = fake_validator

    with pytest.raises(InvalidItemException) as exc_info:
        gilded_rose.update_quality()

    assert "boom" in str(exc_info.value)
