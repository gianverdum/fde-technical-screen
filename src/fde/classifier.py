"""Classification engine that applies rules in priority order."""

from typing import List
from .strategies import ClassificationRule

class RuleEngine:
    """Applies classification rules in priority order."""
    
    def __init__(self):
        self.rules: List[ClassificationRule] = []
    
    def add_rule(self, rule: ClassificationRule) -> 'RuleEngine':
        """Add a rule to the engine."""
        self.rules.append(rule)
        return self
    
    def classify(self, width: float, height: float, length: float, mass: float) -> str:
        """Apply rules in order - first match wins."""
        for rule in self.rules:
            if rule.applies(width, height, length, mass):
                return rule.classify()
        
        return "STANDARD"  # Default when no rules apply

# Global rule engine instance
_default_engine = None

def get_classification_engine() -> RuleEngine:
    """Get the default classification engine."""
    global _default_engine
    if _default_engine is None:
        _default_engine = _create_default_engine()
    return _default_engine

def _create_default_engine() -> RuleEngine:
    """Create engine with original FDE rules."""
    from .strategies import RejectRule, SpecialHeavyRule, SpecialBulkyRule, FragileRule
    
    return (RuleEngine()
            .add_rule(RejectRule())          # Highest priority
            .add_rule(SpecialHeavyRule())    # Medium priority
            .add_rule(SpecialBulkyRule())     # Medium priority
            .add_rule(FragileRule())          # Lowest priority
    # STANDARD is implicit (no rules match)
    )

def configure_classification_engine(engine: RuleEngine):
    """Replace the default engine with a custom one."""
    global _default_engine
    _default_engine = engine