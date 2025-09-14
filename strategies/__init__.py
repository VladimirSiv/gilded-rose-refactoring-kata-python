"""Strategy pattern implementation for Gilded Rose item quality updates."""

from .base import UpdateStrategy, BaseStrategy
from .concrete import (
    AgedBrieStrategy,
    BackstagePassesStrategy,
    SulfurasStrategy,
    DefaultStrategy,
)
from .decorators import ConjuredModifier, ClampModifier
from .registry import StrategyRegistry

__all__ = [
    "UpdateStrategy",
    "BaseStrategy",
    "AgedBrieStrategy",
    "BackstagePassesStrategy",
    "SulfurasStrategy",
    "DefaultStrategy",
    "ConjuredModifier",
    "ClampModifier",
    "StrategyRegistry",
]
