"""String utilities for item name handling."""

import re


def normalize_item_name(name: str) -> str:
    """Normalize an item name for consistent matching.

    Args:
        name: The item name to normalize

    Returns:
        Normalized item name
    """
    if not name or not isinstance(name, str):
        return ""

    normalized = name.lower().strip()
    normalized = re.sub(r"\s+", " ", normalized)
    normalized = re.sub(r"[^\w\s-]", "", normalized)

    return normalized


def extract_item_type(name: str) -> tuple[str, bool]:
    """Extract the base item type and whether it's conjured.

    Args:
        name: The item name to analyze

    Returns:
        Tuple of (base_name, is_conjured)
    """
    normalized = normalize_item_name(name)

    if normalized.startswith("conjured "):
        base_name = normalized[9:]
        return base_name, True

    return normalized, False
