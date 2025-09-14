"""Gilded Rose Item Validator implementation"""

from typing import TYPE_CHECKING
from exceptions import InvalidItemException

if TYPE_CHECKING:
    from .base import Item


class ItemValidator:  # pylint: disable=too-few-public-methods
    """Class that defines logic for validating Gilded Rose Items."""

    def validate(self, item: "Item") -> None:
        """Validates the item.

        Args:
            item: The item to validate.

        Raises:
            InvalidItemException: If the item is invalid.
        """
        if item is None:
            raise InvalidItemException("Item must not be None")

        required_attrs = {
            "name": str,
            "sell_in": int,
            "quality": int,
        }

        for attr, expected_type in required_attrs.items():
            if not hasattr(item, attr) or getattr(item, attr) is None:
                raise InvalidItemException(f"Item must have {attr} attribute")

            value = getattr(item, attr)
            if not isinstance(value, expected_type):
                raise InvalidItemException(
                    f"{attr.capitalize()} must be a {expected_type.__name__}, "
                    f"got {type(value).__name__}"
                )
