"""Core business logic for the FDE Technical Screen challenge."""

import time
from .metrics import default_metrics
import logging

logger = logging.getLogger(__name__)

from typing import Union

Number = Union[int, float]

def sort(width: Number, height: Number, length: Number, mass: Number) -> str:
    """
    Sort packages based on their dimensions and mass.

    Args:
        width (Number): Width of the package.
        height (Number): Height of the package.
        length (Number): Length of the package.
        mass (Number): Mass of the package.

    Returns:
        str: The category of the package.
    """
    start = time.perf_counter()
    
    try:
        validate_package_data(width, height, length, mass)
        is_heavy = mass >= 20
        is_bulky = (width * height * length) >= 1_000_000 or (width >= 150 or height >= 150 or length >= 150)

        if is_heavy and is_bulky:
            category = "REJECTED"
        elif is_bulky or is_heavy:
            category = "SPECIAL"
        else:
            category = "STANDARD"

        duration = time.perf_counter() - start

        try:
            default_metrics.observe(category, duration)
        except Exception:
            logger.exception("metrics_observe_failed")
        
        return category
    
    except Exception:
        try:
            default_metrics.record_error()
        except Exception:
            logger.exception("metrics_record_error_failed")
        raise

def validate_package_data(width: Number, height: Number, length: Number, mass: Number) -> None:
    """
    Validate the package data.

    Args:
        width (Number): Width of the package.
        height (Number): Height of the package.
        length (Number): Length of the package.
        mass (Number): Mass of the package.

    Raises:
        ValueError: If any dimension or mass is negative.
    """
    if not all(isinstance(value, (int, float)) for value in [width, height, length, mass]):
        raise TypeError("All dimensions and mass must be numbers.")
    if not (width > 0 and height > 0 and length > 0 and mass > 0):
        raise ValueError("All dimensions and mass must be positive.")