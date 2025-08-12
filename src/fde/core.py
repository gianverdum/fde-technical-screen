"""Core business logic for the FDE Technical Screen challenge."""

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
    is_heavy = mass >= 20
    is_bulky = (width * height * length) >= 1_000_000 or (width >= 150 or height >= 150 or length >= 150)

    if is_heavy and is_bulky:
        return "REJECTED"
    if is_bulky or is_heavy:
        return "SPECIAL"
    return "STANDARD"