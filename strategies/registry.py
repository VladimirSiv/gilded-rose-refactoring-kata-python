"""Strategy registry for mapping item names to update strategies."""

from typing import Optional, Dict
from utils.string_utils import (
    normalize_item_name,
    extract_item_type,
)
from items.constants import AGED_BRIE, BACKSTAGE_PASSES, SULFURAS
from .concrete import (
    AgedBrieStrategy,
    BackstagePassesStrategy,
    SulfurasStrategy,
    DefaultStrategy,
)
from .decorators import ConjuredModifier, ClampModifier
from .base import UpdateStrategy


class StrategyRegistry:  # pylint: disable=too-few-public-methods
    """Registry for mapping item names to update strategies."""

    def __init__(self) -> None:
        """Initialize the strategy registry with default strategies."""
        self._strategies: Dict[str, UpdateStrategy] = {
            AGED_BRIE: AgedBrieStrategy(),
            BACKSTAGE_PASSES: BackstagePassesStrategy(),
            SULFURAS: SulfurasStrategy(),
        }
        self._default_strategy = DefaultStrategy()

        self._normalized_lookup: Dict[str, str] = {}
        for item_name in self._strategies:
            normalized = normalize_item_name(item_name)
            self._normalized_lookup[normalized] = item_name

    def get_strategy(
        self,
        item_name: str,
    ) -> UpdateStrategy:
        """Get the appropriate strategy for an item name.

        Args:
            item_name: The name of the item

        Returns:
            The appropriate update strategy
        """

        normalized_name = normalize_item_name(item_name)

        if normalized_name in self._normalized_lookup:
            original_name = self._normalized_lookup[normalized_name]
            return ClampModifier(self._strategies[original_name])

        base_strategy = self._get_base_strategy_for_mixed_item(item_name)
        if base_strategy:
            return self._wrap_with_modifiers(item_name, base_strategy)

        return ClampModifier(self._default_strategy)

    def _get_base_strategy_for_mixed_item(
        self,
        item_name: str,
    ) -> Optional[UpdateStrategy]:
        """Extract base strategy from mixed item names.

        Args:
            item_name: The name of the item

        Returns:
            The base strategy if found, None otherwise
        """
        base_name, is_conjured = extract_item_type(item_name)

        if is_conjured:
            if base_name in self._normalized_lookup:
                original_name = self._normalized_lookup[base_name]
                return self._strategies[original_name]

            return self._default_strategy

        return None

    def _wrap_with_modifiers(
        self,
        item_name: str,
        base_strategy: UpdateStrategy,
    ) -> UpdateStrategy:
        """Wrap base strategy with appropriate modifiers.

        Args:
            item_name: The name of the item
            base_strategy: The base strategy to wrap

        Returns:
            The wrapped strategy
        """
        strategy = base_strategy

        _, is_conjured = extract_item_type(item_name)
        if is_conjured:
            strategy = ConjuredModifier(strategy)

        return ClampModifier(strategy)
