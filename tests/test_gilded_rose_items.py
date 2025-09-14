"""Test cases for all item strategies."""

from gilded_rose import GildedRose
from items import Item


def test_item_repr():

    item = Item("Test", 10, 10)
    expected_repr = "Test, 10, 10"
    assert repr(item) == expected_repr


def test_decrease_sell_in_and_quality_by_one():
    # Default update, decreasing sell_in and quality by one
    item_current = {
        "name": "+5 Dexterity Vest",
        "sell_in": 10,
        "quality": 20,
    }
    item_updated = {
        "name": "+5 Dexterity Vest",
        "sell_in": 9,
        "quality": 19,
    }
    items = [
        Item(
            name=item_current["name"],
            sell_in=item_current["sell_in"],
            quality=item_current["quality"],
        )
    ]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert item_updated["name"] == items[0].name
    assert item_updated["sell_in"] == items[0].sell_in
    assert item_updated["quality"] == items[0].quality


def test_decrease_quality_by_two():
    # sell_in date expired, decrease quality by two
    item_current = {
        "name": "+5 Dexterity Vest",
        "sell_in": 0,
        "quality": 20,
    }
    item_updated = {
        "name": "+5 Dexterity Vest",
        "sell_in": -1,
        "quality": 18,
    }
    items = [
        Item(
            name=item_current["name"],
            sell_in=item_current["sell_in"],
            quality=item_current["quality"],
        )
    ]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert item_updated["name"] == items[0].name
    assert item_updated["sell_in"] == items[0].sell_in
    assert item_updated["quality"] == items[0].quality


def test_quality_never_negative():
    # Tests that quality is never negative
    item_current = {
        "name": "+5 Dexterity Vest",
        "sell_in": 2,
        "quality": 0,
    }
    item_updated = {
        "name": "+5 Dexterity Vest",
        "sell_in": 1,
        "quality": 0,
    }
    items = [
        Item(
            name=item_current["name"],
            sell_in=item_current["sell_in"],
            quality=item_current["quality"],
        )
    ]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert item_updated["name"] == items[0].name
    assert item_updated["sell_in"] == items[0].sell_in
    assert item_updated["quality"] == items[0].quality


def test_aged_brie_quality():
    # Tests that quality increases as Aged Brie gets older
    item_current = {
        "name": "Aged Brie",
        "sell_in": 2,
        "quality": 1,
    }
    item_updated = {
        "name": "Aged Brie",
        "sell_in": 1,
        "quality": 2,
    }
    items = [
        Item(
            name=item_current["name"],
            sell_in=item_current["sell_in"],
            quality=item_current["quality"],
        )
    ]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert item_updated["name"] == items[0].name
    assert item_updated["sell_in"] == items[0].sell_in
    assert item_updated["quality"] == items[0].quality


def test_aged_brie_quality_after_sell_in():
    # Tests that quality increases as Aged Brie gets older
    # after sell_in the quality should increase by 2
    item_current = {
        "name": "Aged Brie",
        "sell_in": -1,
        "quality": 1,
    }
    item_updated = {
        "name": "Aged Brie",
        "sell_in": -2,
        "quality": 3,
    }
    items = [
        Item(
            name=item_current["name"],
            sell_in=item_current["sell_in"],
            quality=item_current["quality"],
        )
    ]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert item_updated["name"] == items[0].name
    assert item_updated["sell_in"] == items[0].sell_in
    assert item_updated["quality"] == items[0].quality


def test_quality_upper_limit():
    # Tests that quality never gets above 50
    item_current = {
        "name": "Aged Brie",
        "sell_in": 2,
        "quality": 50,
    }
    item_updated = {
        "name": "Aged Brie",
        "sell_in": 1,
        "quality": 50,
    }
    items = [
        Item(
            name=item_current["name"],
            sell_in=item_current["sell_in"],
            quality=item_current["quality"],
        )
    ]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert item_updated["name"] == items[0].name
    assert item_updated["sell_in"] == items[0].sell_in
    assert item_updated["quality"] == items[0].quality


def test_legendary_item_sulfuras():
    # Tests that Sulfuras never has to be sold and never decreases in quality
    # its quality is 80
    item_current = {
        "name": "Sulfuras, Hand of Ragnaros",
        "sell_in": 2,
        "quality": 80,
    }
    item_updated = {
        "name": "Sulfuras, Hand of Ragnaros",
        "sell_in": 2,
        "quality": 80,
    }
    items = [
        Item(
            name=item_current["name"],
            sell_in=item_current["sell_in"],
            quality=item_current["quality"],
        )
    ]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert item_updated["name"] == items[0].name
    assert item_updated["sell_in"] == items[0].sell_in
    assert item_updated["quality"] == items[0].quality


def test_backstage_passes_more_than_ten_days():
    # Tests that Backstage Passes increases in quality by one if there
    # are more than 10 days
    item_current = {
        "name": "Backstage passes to a TAFKAL80ETC concert",
        "sell_in": 11,
        "quality": 3,
    }
    item_updated = {
        "name": "Backstage passes to a TAFKAL80ETC concert",
        "sell_in": 10,
        "quality": 4,
    }
    items = [
        Item(
            name=item_current["name"],
            sell_in=item_current["sell_in"],
            quality=item_current["quality"],
        )
    ]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert item_updated["name"] == items[0].name
    assert item_updated["sell_in"] == items[0].sell_in
    assert item_updated["quality"] == items[0].quality


def test_backstage_passes_less_than_ten_days():
    # Tests that Backstage Passes increases in quality by 2 if there
    # are 10 or less days
    item_current = {
        "name": "Backstage passes to a TAFKAL80ETC concert",
        "sell_in": 8,
        "quality": 3,
    }
    item_updated = {
        "name": "Backstage passes to a TAFKAL80ETC concert",
        "sell_in": 7,
        "quality": 5,
    }
    items = [
        Item(
            name=item_current["name"],
            sell_in=item_current["sell_in"],
            quality=item_current["quality"],
        )
    ]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert item_updated["name"] == items[0].name
    assert item_updated["sell_in"] == items[0].sell_in
    assert item_updated["quality"] == items[0].quality


def test_backstage_passes_less_than_five_days():
    # Tests that Backstage Passes increases in quality by 3 if there
    # are 5 or less days
    item_current = {
        "name": "Backstage passes to a TAFKAL80ETC concert",
        "sell_in": 5,
        "quality": 3,
    }
    item_updated = {
        "name": "Backstage passes to a TAFKAL80ETC concert",
        "sell_in": 4,
        "quality": 6,
    }
    items = [
        Item(
            name=item_current["name"],
            sell_in=item_current["sell_in"],
            quality=item_current["quality"],
        )
    ]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert item_updated["name"] == items[0].name
    assert item_updated["sell_in"] == items[0].sell_in
    assert item_updated["quality"] == items[0].quality


def test_backstage_passes_less_than_zero_days():
    # Test that Backstage Passes quality drops to 0 after the concert
    item_current = {
        "name": "Backstage passes to a TAFKAL80ETC concert",
        "sell_in": 0,
        "quality": 3,
    }
    item_updated = {
        "name": "Backstage passes to a TAFKAL80ETC concert",
        "sell_in": -1,
        "quality": 0,
    }
    items = [
        Item(
            name=item_current["name"],
            sell_in=item_current["sell_in"],
            quality=item_current["quality"],
        )
    ]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert item_updated["name"] == items[0].name
    assert item_updated["sell_in"] == items[0].sell_in
    assert item_updated["quality"] == items[0].quality


def test_conjured_default_item():
    # Test Conjured item double decrease in quality for a Default Item
    item_current = {
        "name": "Conjured Default Item",
        "sell_in": 4,
        "quality": 2,
    }
    item_updated = {
        "name": "Conjured Default Item",
        "sell_in": 3,
        "quality": 0,
    }
    items = [
        Item(
            name=item_current["name"],
            sell_in=item_current["sell_in"],
            quality=item_current["quality"],
        )
    ]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert item_updated["name"] == items[0].name
    assert item_updated["sell_in"] == items[0].sell_in
    assert item_updated["quality"] == items[0].quality


def test_conjured_registered_item():
    # Test Conjured item double decrease in quality for a Registered Item
    item_current = {
        "name": "Conjured Backstage passes to a TAFKAL80ETC concert",
        "sell_in": 10,
        "quality": 2,
    }
    item_updated = {
        "name": "Conjured Backstage passes to a TAFKAL80ETC concert",
        "sell_in": 9,
        "quality": 6,
    }
    items = [
        Item(
            name=item_current["name"],
            sell_in=item_current["sell_in"],
            quality=item_current["quality"],
        )
    ]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert item_updated["name"] == items[0].name
    assert item_updated["sell_in"] == items[0].sell_in
    assert item_updated["quality"] == items[0].quality
