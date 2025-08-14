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

def test_throws_error_when_negative_dimension():
    """
    Negative dimension -> ValueError
    """
    try:
        sort(-1, 10, 10, 10)
    except ValueError as e:
        assert str(e) == "All dimensions and mass must be positive."

def test_throws_error_when_negative_mass():
    """
    Negative mass -> ValueError
    """
    try:
        sort(10, 10, 10, -1)
    except ValueError as e:
        assert str(e) == "All dimensions and mass must be positive."

def test_throws_error_when_zero_dimension():
    """
    Zero dimension -> ValueError
    """
    try:
        sort(0, 10, 10, 10)
    except ValueError as e:
        assert str(e) == "All dimensions and mass must be positive."

def test_throws_error_when_zero_mass():
    """
    Zero mass -> ValueError
    """
    try:
        sort(10, 10, 10, 0)
    except ValueError as e:
        assert str(e) == "All dimensions and mass must be positive."

def test_throws_error_when_non_numeric_dimension():
    """
    Non-numeric dimension -> TypeError
    """
    try:
        sort("a", 10, 10, 10)
    except TypeError as e:
        assert str(e) == "All dimensions and mass must be numbers."

def test_throws_error_when_non_numeric_mass():
    """
    Non-numeric mass -> TypeError
    """
    try:
        sort(10, 10, 10, "b")
    except TypeError as e:
        assert str(e) == "All dimensions and mass must be numbers."