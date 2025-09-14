"""Base exception class for Gilded Rose system."""

from typing import Optional


class GildedRoseException(Exception):
    """Base exception class for all Gilded Rose related errors."""

    def __init__(
        self,
        message: str,
        item_name: Optional[str] = None,
    ) -> None:
        """Initialize the exception.

        Args:
            message: Error message
            item_name: Optional name of the item that caused the error
        """
        super().__init__(message)
        self.message = message
        self.item_name = item_name

    def __str__(self) -> str:
        """Return string representation of the exception."""
        if self.item_name:
            return f"{self.message} (Item: {self.item_name})"
        return self.message
