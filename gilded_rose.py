"""Main Gilded Rose implementation using the Strategy pattern."""

import logging
from typing import List, TYPE_CHECKING
from strategies import StrategyRegistry
from exceptions import InvalidItemException, StrategyUpdateException
from items import ItemValidator

if TYPE_CHECKING:
    from items import Item


logger = logging.getLogger(__name__)


class GildedRose:  # pylint: disable=too-few-public-methods
    """Main class for managing item quality updates using the Strategy pattern."""

    def __init__(self, items: List["Item"]) -> None:
        """Initialize GildedRose with a list of items.

        Args:
            items: List of items to manage
        """
        if not isinstance(items, list):
            raise ValueError("Items must be a list")

        self.items = items
        self.validator = ItemValidator()
        self.strategy_registry = StrategyRegistry()

    def update_quality(self) -> None:
        """Update quality for all items using their respective strategies."""
        for item in self.items:
            try:
                self.validator.validate(item)
                strategy = self.strategy_registry.get_strategy(item.name)
                strategy.update(item)

            # Note: We just re-raise in this demo, in general it would contain logic
            # to reroute, DLQ, handle broken records in a way that wouldn't
            # impact the processing of other records.

            except InvalidItemException as iie:
                logger.error("Item invalid %s: %s", item, str(iie))
                raise
            except StrategyUpdateException as iue:
                logger.error("Item update failed %s: %s", item, str(iue))
                raise
            except Exception as e:
                logger.critical("Unexpected error updating item %s: %s", item, str(e))
                raise
