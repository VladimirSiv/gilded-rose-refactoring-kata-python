"""Strategy-related exceptions."""

from .base import GildedRoseException


class StrategyUpdateException(GildedRoseException):
    """Exception raised when an item update fails."""


class AgedBrieStrategyUpdateException(StrategyUpdateException):
    """Exception raised when an Aged Brie Strategy Update Failed"""


class BackstagePassesStrategyUpdateException(StrategyUpdateException):
    """Exception raised when an Backstage Passes Strategy Update Failed"""


class DefaultStrategyUpdateException(StrategyUpdateException):
    """Exception raised when an Default Strategy Update Failed"""
