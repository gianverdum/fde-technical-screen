"""
Tests for sort():
"""

from fde.core import sort

def test_standard_package():
    """
    Arrange: small dimensions and mass < 20
    Act: call sort
    Assert: returns STANDARD
    """
    width, height, length, mass = 10, 10, 10, 10
    result = sort(width, height, length, mass)
    assert result == "STANDARD"

def test_special_bulky_by_volume():
    """
    Bulky when volume >= 1_000_000 cm³
    100 * 100 * 100 = 1_000_000 -> SPECIAL (if not heavy)
    """
    result = sort(100, 100, 100, 10)
    assert result == "SPECIAL"

def test_special_bulky_by_dimension():
    """
    Bulky when any dimension >= 150 cm
    """
    result = sort(150, 1, 1, 1)
    assert result == "SPECIAL"

def test_special_bulky_by_mass():
    """
    Heavy when mass >= 20 kg (but not bulky)
    """
    result = sort(10, 10, 10, 20)
    assert result == "SPECIAL"

def test_reject_when_heavy_and_bulky():
    """
    Both heavy and bulky -> REJECTED
    """
    result = sort(150, 1, 1, 25)
    assert result == "REJECTED"