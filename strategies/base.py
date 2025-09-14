"""Base strategy classes and interfaces for item quality updates."""

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
from items.constants import QUALITY_UPPER_LIMIT, QUALITY_LOWER_LIMIT

if TYPE_CHECKING:
    from items import Item


class UpdateStrategy(ABC):  # pylint: disable=too-few-public-methods
    """Abstract base class for item update strategies."""

    @abstractmethod
    def update(self, item: "Item") -> None:
        """Update the given item according to this strategy.

        Args:
            item: The item to update
        """


class BaseStrategy(UpdateStrategy):
    """Base strategy with common functionality."""

    UPPER_LIMIT = QUALITY_UPPER_LIMIT
    LOWER_LIMIT = QUALITY_LOWER_LIMIT

    def decrement_sell_in(self, item: "Item") -> None:
        """Decrement the sell_in value by 1.

        Args:
            item: The item to update
        """
        item.sell_in -= 1
