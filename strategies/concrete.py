"""Concrete strategy implementations for different item types."""

from typing import TYPE_CHECKING
from exceptions import (
    AgedBrieStrategyUpdateException,
    BackstagePassesStrategyUpdateException,
    DefaultStrategyUpdateException,
)
from items.constants import (
    BACKSTAGE_DAYS_5,
    BACKSTAGE_DAYS_10,
    BACKSTAGE_INCREASE_5_DAYS,
    BACKSTAGE_INCREASE_10_DAYS,
    BACKSTAGE_INCREASE_NORMAL,
    BACKSTAGE_QUALITY_AFTER_CONCERT,
    NORMAL_DEGRADATION,
    EXPIRED_DEGRADATION,
)
from .base import BaseStrategy

if TYPE_CHECKING:
    from items import Item


class AgedBrieStrategy(BaseStrategy):
    """Strategy for Aged Brie items"""

    def update(self, item: "Item") -> None:
        """Update Aged Brie item quality.

        Raises:
            AgedBrieStrategyUpdateException: If the update fails
        """

        try:
            self.decrement_sell_in(item)

            if item.quality < self.UPPER_LIMIT:
                if item.sell_in >= 0:
                    item.quality += NORMAL_DEGRADATION
                else:
                    item.quality += EXPIRED_DEGRADATION
        except TypeError as e:
            raise AgedBrieStrategyUpdateException(
                f"Failed to update (Aged Brie). {type(e).__name__}: {e}",
                item.name,
            ) from e


class BackstagePassesStrategy(BaseStrategy):
    """Strategy for Backstage Passes"""

    def update(self, item: "Item") -> None:
        """Update Backstage Passes item quality.

        Raises:
            BackstagePassesStrategyUpdateException: If the update fails
        """
        try:
            self.decrement_sell_in(item)

            if item.sell_in < 0:
                item.quality = BACKSTAGE_QUALITY_AFTER_CONCERT
            elif item.sell_in < BACKSTAGE_DAYS_5:
                item.quality += BACKSTAGE_INCREASE_5_DAYS
            elif item.sell_in < BACKSTAGE_DAYS_10:
                item.quality += BACKSTAGE_INCREASE_10_DAYS
            else:
                item.quality += BACKSTAGE_INCREASE_NORMAL
        except TypeError as e:
            raise BackstagePassesStrategyUpdateException(
                f"Failed to update (Backstage Passes). {type(e).__name__}: {e}",
                item.name,
            ) from e


class SulfurasStrategy(BaseStrategy):
    """Strategy for Sulfuras"""

    def update(self, item: "Item") -> None:
        """Update Sulfuras item"""


class DefaultStrategy(BaseStrategy):
    """Default strategy for Default items"""

    def update(self, item: "Item") -> None:
        """Update Default item quality.

        Raises:
            DefaultStrategyUpdateException: If the update fails
        """
        try:
            self.decrement_sell_in(item)

            if item.sell_in < 0:
                item.quality -= EXPIRED_DEGRADATION
            else:
                item.quality -= NORMAL_DEGRADATION
        except TypeError as e:
            raise DefaultStrategyUpdateException(
                f"Failed to update (Default). {type(e).__name__}: {e}",
                item.name,
            ) from e
