"""Test cases for all exceptions in Strategy implementations"""

import pytest
from items import Item
from strategies.concrete import (
    AgedBrieStrategy,
    BackstagePassesStrategy,
    DefaultStrategy,
)
from exceptions import (
    AgedBrieStrategyUpdateException,
    BackstagePassesStrategyUpdateException,
    DefaultStrategyUpdateException,
)


def test_aged_brie_strategy_update_exception():
    strategy = AgedBrieStrategy()

    with pytest.raises(AgedBrieStrategyUpdateException) as exc_info:
        strategy.update(Item("item", "a", "a"))

    assert (
        str(exc_info.value)
        == "Failed to update (Aged Brie). TypeError: unsupported operand type(s) for -=: 'str' and 'int' (Item: item)"
    )
    assert isinstance(exc_info.value.__cause__, TypeError)


def test_backstage_passes_strategy_update_exception():
    strategy = BackstagePassesStrategy()

    with pytest.raises(BackstagePassesStrategyUpdateException) as exc_info:
        strategy.update(Item("item", "a", "a"))

    assert (
        str(exc_info.value)
        == "Failed to update (Backstage Passes). TypeError: unsupported operand type(s) for -=: 'str' and 'int' (Item: item)"
    )
    assert isinstance(exc_info.value.__cause__, TypeError)


def test_default_strategy_update_exception():
    strategy = DefaultStrategy()

    with pytest.raises(DefaultStrategyUpdateException) as exc_info:
        strategy.update(Item("item", "a", "a"))

    assert (
        str(exc_info.value)
        == "Failed to update (Default). TypeError: unsupported operand type(s) for -=: 'str' and 'int' (Item: item)"
    )
    assert isinstance(exc_info.value.__cause__, TypeError)
