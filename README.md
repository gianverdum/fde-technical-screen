# FDE Technical Screen - Package Sorting System

A Python implementation for Thoughtful's robotic automation factory package sorting system. This project implements a function that dispatches packages to the correct stack based on their volume and mass criteria.

## 🎯 Objective

This solution implements a robotic arm function that sorts packages into different stacks according to their physical properties (dimensions and mass), ensuring proper handling in an automated warehouse environment.

## 📋 Sorting Rules

### Package Classification:
- **Bulky Package**: Volume ≥ 1,000,000 cm³ OR any dimension ≥ 150 cm
- **Heavy Package**: Mass ≥ 20 kg

### Dispatch Stacks:
- **STANDARD**: Packages that are neither bulky nor heavy (normal handling)
- **SPECIAL**: Packages that are either heavy OR bulky (requires special handling)
- **REJECTED**: Packages that are both heavy AND bulky (cannot be processed)

## 🏗️ Project Structure

```
fde/
├── src/
│   ├── main.py              # Entry point (placeholder)
│   └── fde/
│       ├── __init__.py      # Package initialization
│       ├── core.py          # Main sorting logic implementation
│       ├── models.py        # Data models (placeholder for future extensions)
│       ├── io.py            # I/O utilities (placeholder)
│       └── utils.py         # Utility functions (placeholder)
├── tests/
│   ├── __init__.py
│   └── test_core.py         # Comprehensive test suite
├── main.py                  # Simple entry point
├── pyproject.toml           # Project configuration
├── pytest.ini              # Test configuration
├── uv.lock                  # Dependency lock file
└── README.md               # This file
```

## 🧪 Testing

The project includes a comprehensive test suite in `tests/test_core.py` covering:

- **Standard packages**: Normal size and weight
- **Bulky packages**: By volume (≥1M cm³) and by dimension (≥150cm)
- **Heavy packages**: Mass ≥20kg
- **Rejected packages**: Both heavy and bulky
- **Edge cases**: Boundary conditions

### Running Tests

```bash
# Install dependencies
uv sync

# Run tests
uv run pytest

# Run tests with verbose output
uv run pytest -v

# Run tests with coverage
uv run pytest --cov=src/fde
```

## 🛠️ Setup and Installation

### Prerequisites
- Python ≥ 3.13
- uv (recommended) or pip

### Installation

```bash
# Clone the repository
git clone <repository-url>
cd fde

# Install dependencies and create virtual environment using uv
uv sync

# Alternative: using pip (not recommended for this project)
# pip install -e .
# pip install pytest
```

### Usage

```python
from fde.core import sort

# Example usage
result = sort(width=100, height=100, length=100, mass=10)
print(result)  # Output: "SPECIAL" (bulky by volume)

result = sort(width=10, height=10, length=10, mass=25)
print(result)  # Output: "SPECIAL" (heavy)

result = sort(width=150, height=50, length=50, mass=25)
print(result)  # Output: "REJECTED" (both bulky and heavy)
```

## 📊 Test Results

All tests pass successfully, ensuring the implementation correctly handles:
- ✅ Standard package classification
- ✅ Bulky package detection (both by volume and dimension)
- ✅ Heavy package detection
- ✅ Rejected package identification
- ✅ Edge cases and boundary conditions

## 🔧 Development

### Code Quality
- Type hints throughout the codebase
- Comprehensive docstrings
- Clear variable naming
- Modular architecture for future extensions

### Future Enhancements
The project structure supports easy extension with:
- Custom data models in `models.py`
- I/O operations in `io.py`
- Additional utilities in `utils.py`
- Integration with external systems

## 📄 License

This project is part of the FDE Technical Screen challenge.
