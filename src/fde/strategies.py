"""Individual classification rules using Strategy pattern."""

from abc import ABC, abstractmethod

class ClassificationRule(ABC):
    """Base class for classification rules."""
    
    @abstractmethod
    def applies(self, width: float, height: float, length: float, mass: float) -> bool:
        """Check if this rule applies to the package."""
        pass
    
    @abstractmethod
    def classify(self) -> str:
        """Return the classification for this rule."""
        pass

class RejectRule(ClassificationRule):
    """Rule: Heavy AND Bulky → REJECTED"""
    
    def __init__(self, heavy_threshold: float = 20.0, 
                 bulky_volume: float = 1_000_000, 
                 bulky_dimension: float = 150.0):
        self.heavy_threshold = heavy_threshold
        self.bulky_volume = bulky_volume
        self.bulky_dimension = bulky_dimension
    
    def applies(self, width: float, height: float, length: float, mass: float) -> bool:
        is_heavy = mass >= self.heavy_threshold
        is_bulky = (
            (width * height * length) >= self.bulky_volume or
            any(dim >= self.bulky_dimension for dim in [width, height, length])
        )
        return is_heavy and is_bulky
    
    def classify(self) -> str:
        return "REJECTED"

class SpecialHeavyRule(ClassificationRule):
    """Rule: Heavy (but not bulky) → SPECIAL"""
    
    def __init__(self, heavy_threshold: float = 20.0):
        self.heavy_threshold = heavy_threshold
    
    def applies(self, width: float, height: float, length: float, mass: float) -> bool:
        return mass >= self.heavy_threshold
    
    def classify(self) -> str:
        return "SPECIAL"

class SpecialBulkyRule(ClassificationRule):
    """Rule: Bulky (but not heavy) → SPECIAL"""
    
    def __init__(self, bulky_volume: float = 1_000_000, bulky_dimension: float = 150.0):
        self.bulky_volume = bulky_volume
        self.bulky_dimension = bulky_dimension
    
    def applies(self, width: float, height: float, length: float, mass: float) -> bool:
        return (
            (width * height * length) >= self.bulky_volume or
            any(dim >= self.bulky_dimension for dim in [width, height, length])
        )
    
    def classify(self) -> str:
        return "SPECIAL"

class FragileRule(ClassificationRule):
    """Rule: Low density → FRAGILE"""
    
    def __init__(self, density_threshold: float = 5.0):
        self.density_threshold = density_threshold
    
    def applies(self, width: float, height: float, length: float, mass: float) -> bool:
        volume = width * height * length
        if volume == 0:
            return False
        density = (mass / volume) * 1000
        return density <= self.density_threshold
    
    def classify(self) -> str:
        return "FRAGILE"

class ExpressRule(ClassificationRule):
    """Rule: Small and light → EXPRESS"""
    
    def __init__(self, max_volume: float = 50_000, max_mass: float = 5.0):
        self.max_volume = max_volume
        self.max_mass = max_mass
    
    def applies(self, width: float, height: float, length: float, mass: float) -> bool:
        volume = width * height * length
        return volume <= self.max_volume and mass <= self.max_mass
    
    def classify(self) -> str:
        return "EXPRESS"