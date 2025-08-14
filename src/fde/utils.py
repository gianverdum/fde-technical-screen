"""Utility functions for the FDE Package Sorting System.

This module contains helper functions and utilities for future extensions
of the package sorting system.
"""

from typing import List, Dict, Any
from .models import Package


def calculate_statistics(packages: List[Package]) -> Dict[str, Any]:
    """Calculate statistics for a list of packages.
    
    Args:
        packages: List of Package objects.
        
    Returns:
        Dictionary containing statistics about the packages.
    """
    if not packages:
        return {}
    
    total_packages = len(packages)
    total_volume = sum(pkg.volume for pkg in packages)
    total_mass = sum(pkg.mass for pkg in packages)
    
    heavy_count = sum(1 for pkg in packages if pkg.is_heavy)
    bulky_count = sum(1 for pkg in packages if pkg.is_bulky)
    
    return {
        'total_packages': total_packages,
        'total_volume': total_volume,
        'total_mass': total_mass,
        'average_volume': total_volume / total_packages,
        'average_mass': total_mass / total_packages,
        'heavy_packages': heavy_count,
        'bulky_packages': bulky_count,
        'heavy_percentage': (heavy_count / total_packages) * 100,
        'bulky_percentage': (bulky_count / total_packages) * 100
    }


def validate_package_dimensions(width: float, height: float, length: float, mass: float) -> bool:
    """Validate package dimensions and mass.
    
    Args:
        width: Width of the package.
        height: Height of the package.
        length: Length of the package.
        mass: Mass of the package.
        
    Returns:
        True if all dimensions and mass are positive, False otherwise.
    """
    return all(value > 0 for value in [width, height, length, mass])


def format_classification_summary(results: List[str]) -> Dict[str, int]:
    """Generate a summary of classification results.
    
    Args:
        results: List of classification results (STANDARD, SPECIAL, REJECTED).
        
    Returns:
        Dictionary with counts for each classification category.
    """
    summary = {
        'STANDARD': 0,
        'SPECIAL': 0,
        'REJECTED': 0
    }
    
    for result in results:
        if result in summary:
            summary[result] += 1
    
    return summary


def convert_units(value: float, from_unit: str, to_unit: str) -> float:
    """Convert between different units.
    
    Args:
        value: The value to convert.
        from_unit: Source unit (cm, m, kg, g).
        to_unit: Target unit (cm, m, kg, g).
        
    Returns:
        Converted value.
        
    Note:
        This is a placeholder for future unit conversion needs.
    """
    # Placeholder implementation for common conversions
    conversions = {
        ('cm', 'm'): 0.01,
        ('m', 'cm'): 100,
        ('kg', 'g'): 1000,
        ('g', 'kg'): 0.001
    }
    
    factor = conversions.get((from_unit, to_unit), 1.0)
    return value * factor