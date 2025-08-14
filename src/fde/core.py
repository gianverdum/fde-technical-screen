"""Core business logic for the FDE Technical Screen challenge."""

from typing import Union
from .classifier import get_classification_engine

Number = Union[int, float]

def sort(width: Number, height: Number, length: Number, mass: Number) -> str:
    """
    Sort packages based on their dimensions and mass.
    
    Uses configurable rules internally while maintaining the same API.
    """
    validate_package_data(width, height, length, mass)
    
    engine = get_classification_engine()
    return engine.classify(width, height, length, mass)

def validate_package_data(width: Number, height: Number, length: Number, mass: Number) -> None:
    """Validate the package data."""
    if not all(isinstance(value, (int, float)) for value in [width, height, length, mass]):
        raise TypeError("All dimensions and mass must be numbers.")
    if not (width > 0 and height > 0 and length > 0 and mass > 0):
        raise ValueError("All dimensions and mass must be positive.")