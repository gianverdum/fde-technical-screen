"""Data models for package processing."""

from dataclasses import dataclass
from typing import Optional, Union

Number = Union[int, float]


@dataclass
class Package:
    """Represents a package with its dimensions and mass."""
    
    width: Optional[Number] = None
    height: Optional[Number] = None
    length: Optional[Number] = None
    mass: Optional[Number] = None
    volume: Optional[Number] = None
    stack: Optional[str] = None
    reject_reason: Optional[str] = None
    
    def calculate_volume(self) -> Optional[Number]:
        """Calculate volume if all dimensions are available and valid."""
        if (self.width is not None and 
            self.height is not None and 
            self.length is not None and
            self.width > 0 and 
            self.height > 0 and 
            self.length > 0):
            return self.width * self.height * self.length
        return None
    
    def is_valid_for_sorting(self) -> bool:
        """Check if package has all required data for sorting."""
        return (self.width is not None and 
                self.height is not None and 
                self.length is not None and 
                self.mass is not None and
                self.width > 0 and 
                self.height > 0 and 
                self.length > 0 and
                self.mass >= 0)


@dataclass
class ProcessingResult:
    """Result of processing packages with statistics."""
    
    total_packages: int
    valid_packages: int
    packages: list[Package]
    statistics: dict
