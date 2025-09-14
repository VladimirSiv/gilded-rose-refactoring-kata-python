"""Item-related exceptions."""

from .base import GildedRoseException


class InvalidItemException(GildedRoseException):
    """Exception raised when an item is invalid or malformed."""
