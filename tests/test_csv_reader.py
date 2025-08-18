"""Tests for CSV reading and package validation functionality."""

import pytest # type: ignore
import tempfile
import os
from src.fde.io import read_packages_csv, parse_numeric_value, normalize_value, validate_package
from src.fde.models import Package


class TestCSVReading:
    """Test CSV reading functionality."""
    
    def test_normalize_value(self):
        """Test value normalization."""
        assert normalize_value("") is None
        assert normalize_value("None") is None
        assert normalize_value("none") is None
        assert normalize_value("NULL") is None
        assert normalize_value('"100"') == "100"
        assert normalize_value("  50  ") == "50"
        assert normalize_value("abc") == "abc"
    
    def test_parse_numeric_value(self):
        """Test numeric value parsing."""
        assert parse_numeric_value("50") == 50
        assert parse_numeric_value("50.5") == 50.5
        assert parse_numeric_value("-15") == -15
        assert parse_numeric_value("abc") is None
        assert parse_numeric_value("23ab") is None
        assert parse_numeric_value("") is None
        assert parse_numeric_value("None") is None
    
    def test_validate_package_missing_fields(self):
        """Test package validation with missing fields."""
        package = Package(width=50, height=60, length=None, mass=10)
        validated = validate_package(package)
        
        assert validated.stack == "REJECTED"
        assert "Missing required fields: length" in validated.reject_reason
    
    def test_validate_package_negative_values(self):
        """Test package validation with negative values."""
        package = Package(width=-50, height=60, length=70, mass=10)
        validated = validate_package(package)
        
        assert validated.stack == "REJECTED"
        assert "Invalid width: must be positive" in validated.reject_reason
        
        package = Package(width=50, height=60, length=70, mass=-10)
        validated = validate_package(package)
        
        assert validated.stack == "REJECTED"
        assert "Invalid mass: cannot be negative" in validated.reject_reason
    
    def test_validate_package_valid(self):
        """Test package validation with valid data."""
        package = Package(width=50, height=60, length=70, mass=10)
        validated = validate_package(package)
        
        assert validated.stack == "STANDARD"
        assert validated.reject_reason is None
        assert validated.volume == 210000
    
    def test_read_csv_basic(self):
        """Test basic CSV reading functionality."""
        csv_content = """Width,Height,Length,Mass
50,60,70,10
100,100,100,30
200,100,50,25"""
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
            f.write(csv_content)
            f.flush()
            
            try:
                result = read_packages_csv(f.name)
                
                assert result.total_packages == 4  # Including header
                assert len(result.packages) == 3   # Excluding header
                assert result.packages[0].stack == "STANDARD"
                assert result.packages[1].stack == "REJECTED"  # Heavy and bulky
                assert result.packages[2].stack == "REJECTED"  # Volume >= 1,000,000
                
            finally:
                os.unlink(f.name)
    
    def test_read_csv_with_errors(self):
        """Test CSV reading with various data errors."""
        csv_content = """Width,Height,Length,Mass
50,60,70,10
,None,50,5
100,abc,100,40
-50,60,70,10"""
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
            f.write(csv_content)
            f.flush()
            
            try:
                result = read_packages_csv(f.name)
                
                assert result.total_packages == 5  # Including header
                assert len(result.packages) == 4   # Excluding header
                
                # First package should be valid
                assert result.packages[0].stack == "STANDARD"
                
                # Second package missing width and height
                assert result.packages[1].stack == "REJECTED"
                assert "Missing required fields" in result.packages[1].reject_reason
                
                # Third package has invalid height
                assert result.packages[2].stack == "REJECTED"
                assert "Missing required fields: height" in result.packages[2].reject_reason
                
                # Fourth package has negative width
                assert result.packages[3].stack == "REJECTED"
                assert "Invalid width" in result.packages[3].reject_reason
                
            finally:
                os.unlink(f.name)
    
    def test_read_csv_with_duplicate_headers(self):
        """Test CSV reading with duplicate headers."""
        csv_content = """Width,Height,Length,Mass
50,60,70,10
Width,Height,Length,Mass
100,100,100,30"""
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
            f.write(csv_content)
            f.flush()
            
            try:
                result = read_packages_csv(f.name)
                
                assert result.total_packages == 4  # Including both headers
                assert len(result.packages) == 2   # Excluding both headers
                assert result.packages[0].stack == "STANDARD"
                assert result.packages[1].stack == "REJECTED"  # Heavy and bulky
                
            finally:
                os.unlink(f.name)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
