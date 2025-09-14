"""Decorator pattern implementations for modifying strategy behavior."""

from typing import TYPE_CHECKING
from items.constants import (
    QUALITY_LOWER_LIMIT,
    QUALITY_UPPER_LIMIT,
    SULFURAS,
    SULFURAS_QUALITY,
)
from .base import UpdateStrategy

if TYPE_CHECKING:
    from items import Item


class StrategyDecorator(UpdateStrategy):  # pylint: disable=too-few-public-methods
    """Base decorator for wrapping other strategies."""

    def __init__(self, strategy: UpdateStrategy) -> None:
        """Initialize the decorator with a strategy to wrap.

        Args:
            strategy: The strategy to wrap
        """
        self.strategy = strategy


class ConjuredModifier(StrategyDecorator):  # pylint: disable=too-few-public-methods
    """Decorator that doubles the quality degradation of any strategy."""

    def update(self, item: "Item") -> None:
        """Update item with doubled quality degradation.

        Args:
            item: The item to update
        """
        original_quality = item.quality
        self.strategy.update(item)
        quality_delta = item.quality - original_quality
        item.quality = original_quality + (quality_delta * 2)


class ClampModifier(StrategyDecorator):  # pylint: disable=too-few-public-methods
    """Decorator that invokes an update from a specific strategy and
    ensures quality stays within bounds, with special cases.
    """

    def update(self, item: "Item") -> None:
        """Update item and ensure quality stays within bounds.

        Args:
            item: The item to update
        """
        self.strategy.update(item)

        if item.name == SULFURAS:
            item.quality = SULFURAS_QUALITY
        else:
            item.quality = max(
                QUALITY_LOWER_LIMIT, min(QUALITY_UPPER_LIMIT, item.quality)
            )
