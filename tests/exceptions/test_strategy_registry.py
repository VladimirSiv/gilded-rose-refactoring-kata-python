"""Test cases for all exceptions related to Strategy Registry logic"""

from strategies.registry import StrategyRegistry
from strategies.decorators import ClampModifier


def test_strategy_registry_returns_strategy_for_known_item():
    registry = StrategyRegistry()
    strategy = registry.get_strategy("Aged Brie")
    assert isinstance(strategy, ClampModifier)
