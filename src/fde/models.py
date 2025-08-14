"""Data models for the FDE Package Sorting System.

This module contains data structures and models for future extensions
of the package sorting system.
"""

from dataclasses import dataclass
from typing import Union

Number = Union[int, float]


@dataclass
class Package:
    """Represents a package with dimensions and mass.
    
    This is a placeholder for future enhancements where packages
    might need to carry additional metadata like ID, destination, etc.
    """
    width: Number
    height: Number
    length: Number
    mass: Number
    
    @property
    def volume(self) -> Number:
        """Calculate the volume of the package."""
        return self.width * self.height * self.length
    
    @property
    def is_bulky(self) -> bool:
        """Check if package is bulky by volume or dimensions."""
        return (self.volume >= 1_000_000 or 
                self.width >= 150 or 
                self.height >= 150 or 
                self.length >= 150)
    
    @property
    def is_heavy(self) -> bool:
        """Check if package is heavy."""
        return self.mass >= 20


@dataclass
class SortingResult:
    """Result of package sorting operation.
    
    Placeholder for future enhancements where sorting results
    might include additional metadata like processing time, 
    destination stack location, etc.
    """
    category: str
    package: Package
    timestamp: str = ""
    stack_location: str = ""