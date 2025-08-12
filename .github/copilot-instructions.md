# Copilot Instructions - FDE Package Sorting System

## Project Overview
This is a Python package sorting system for Thoughtful's robotic automation factory. The core business logic implements a `sort()` function that classifies packages into STANDARD, SPECIAL, or REJECTED categories based on dimensions and mass.

## Development Environment Setup
This project uses **uv** for dependency management. Use `uv run` to execute commands within the virtual environment:

```bash
# Install/sync dependencies
uv sync

# Run tests
uv run pytest

# Run tests with verbose output
uv run pytest -v

# Run tests with coverage
uv run pytest --cov=src/fde
```

## Architecture & Key Files
- `src/fde/core.py` - Main business logic with the `sort()` function
- `tests/test_core.py` - Comprehensive test suite covering all classification scenarios
- `pyproject.toml` - Project configuration with uv dependency management
- Empty placeholder files: `models.py`, `io.py`, `utils.py` for future extensions

## Core Business Logic
The sorting algorithm in `src/fde/core.py` follows this classification:
- **Bulky**: Volume ≥ 1,000,000 cm³ OR any dimension ≥ 150 cm
- **Heavy**: Mass ≥ 20 kg
- **REJECTED**: Both heavy AND bulky
- **SPECIAL**: Either heavy OR bulky (but not both)
- **STANDARD**: Neither heavy nor bulky

## Testing Patterns
Tests use AAA pattern (Arrange-Act-Assert) with descriptive docstrings:
- `test_standard_package()` - Normal packages
- `test_special_bulky_by_volume()` - Volume-based bulky classification
- `test_special_bulky_by_dimension()` - Dimension-based bulky classification
- `test_special_bulky_by_mass()` - Heavy package classification
- `test_reject_when_heavy_and_bulky()` - Rejection criteria

## Development Workflow
1. **Install/sync dependencies**: `uv sync`
2. **Install new dependencies**: `uv add <package>` or `uv add --dev <package>`
3. **Run tests**: `uv run pytest` (simple) or `uv run pytest -v` (verbose)
4. **Type checking**: Code uses type hints with `Union[int, float]` for numeric inputs

## Code Conventions
- Type hints are required (see `Number = Union[int, float]` pattern)
- Functions include comprehensive docstrings with Args/Returns
- Variable naming: `is_heavy`, `is_bulky` for boolean flags
- Early returns for conditional logic clarity
- Test functions have descriptive names and docstring explanations

## Critical Dependencies
- Python ≥ 3.13 (specified in pyproject.toml)
- pytest for testing framework
- uv for package management and virtual environment

## Common Tasks
- **Add new test**: Follow existing AAA pattern in `tests/test_core.py`
- **Extend functionality**: Use placeholder files in `src/fde/` (models.py, utils.py, io.py)
- **Debug failing tests**: Run `uv run pytest -v` for detailed output
- **Check test coverage**: Run `uv run pytest --cov=src/fde`
