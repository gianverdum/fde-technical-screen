"""Input/Output operations for package data."""

import csv
import re
from typing import List, Optional, Union
from .models import Package, ProcessingResult
from .core import sort

Number = Union[int, float]


def normalize_value(value: str) -> Optional[str]:
    """Normalize CSV values by removing quotes and handling None/empty cases."""
    if not value:
        return None
    
    # Remove leading/trailing whitespace and quotes
    value = value.strip().strip('"\'')
    
    # Handle None as string or empty
    if value.lower() in ('none', '', 'null'):
        return None
    
    return value


def parse_numeric_value(value: str) -> Optional[Number]:
    """Parse a string value to a numeric value, handling edge cases."""
    normalized = normalize_value(value)
    
    if normalized is None:
        return None
    
    try:
        # Check if it contains non-numeric characters (except decimal point and minus)
        if re.search(r'[^\d\.\-]', normalized):
            return None
        
        # Try to convert to float
        num_value = float(normalized)
        
        # Return as int if it's a whole number, otherwise float
        if num_value.is_integer():
            return int(num_value)
        return num_value
        
    except (ValueError, AttributeError):
        return None


def validate_package(package: Package) -> Package:
    """Validate and classify a package, setting reject reasons if needed."""
    
    # Check for missing required fields
    missing_fields = []
    if package.width is None:
        missing_fields.append("width")
    if package.height is None:
        missing_fields.append("height")
    if package.length is None:
        missing_fields.append("length")
    if package.mass is None:
        missing_fields.append("mass")
    
    if missing_fields:
        package.stack = "REJECTED"
        package.reject_reason = f"Missing required fields: {', '.join(missing_fields)}"
        return package
    
    # Check for negative or zero dimensions
    if package.width <= 0:
        package.stack = "REJECTED"
        package.reject_reason = "Invalid width: must be positive"
        return package
    
    if package.height <= 0:
        package.stack = "REJECTED"
        package.reject_reason = "Invalid height: must be positive"
        return package
    
    if package.length <= 0:
        package.stack = "REJECTED"
        package.reject_reason = "Invalid length: must be positive"
        return package
    
    if package.mass < 0:
        package.stack = "REJECTED"
        package.reject_reason = "Invalid mass: cannot be negative"
        return package
    
    # Calculate volume
    package.volume = package.calculate_volume()
    
    # If all validations pass, use the sorting function
    if package.is_valid_for_sorting():
        package.stack = sort(package.width, package.height, package.length, package.mass)
    else:
        package.stack = "REJECTED"
        package.reject_reason = "Failed validation for sorting"
    
    return package


def read_packages_csv(file_path: str) -> ProcessingResult:
    """
    Read packages from CSV file and process them.
    
    Args:
        file_path: Path to the CSV file
        
    Returns:
        ProcessingResult with processed packages and statistics
    """
    packages = []
    total_lines = 0
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            # Read all lines first to count total
            lines = file.readlines()
            
        # Process lines
        for line_num, line in enumerate(lines, 1):
            total_lines += 1
            
            # Skip empty lines
            if not line.strip():
                continue
            
            # Parse CSV manually to handle edge cases
            try:
                # Use csv.reader for proper CSV parsing
                row = next(csv.reader([line.strip()]))
                
                # Skip header lines (detect by first column being "Width")
                if row and row[0].strip().lower() == 'width':
                    continue
                
                # Ensure we have at least 4 columns, pad with None if needed
                while len(row) < 4:
                    row.append('')
                
                # Take only first 4 columns if there are more
                row = row[:4]
                
                # Parse each field
                width = parse_numeric_value(row[0])
                height = parse_numeric_value(row[1])
                length = parse_numeric_value(row[2])
                mass = parse_numeric_value(row[3])
                
                # Create package object
                package = Package(
                    width=width,
                    height=height,
                    length=length,
                    mass=mass
                )
                
                # Validate and classify package
                package = validate_package(package)
                packages.append(package)
                
            except Exception as e:
                # Create rejected package for parsing errors
                rejected_package = Package()
                rejected_package.stack = "REJECTED"
                rejected_package.reject_reason = f"CSV parsing error on line {line_num}: {str(e)}"
                packages.append(rejected_package)
    
    except FileNotFoundError:
        raise FileNotFoundError(f"CSV file not found: {file_path}")
    except Exception as e:
        raise Exception(f"Error reading CSV file: {str(e)}")
    
    # Count valid packages (those that could be classified)
    valid_packages = len([p for p in packages if p.stack in ["STANDARD", "SPECIAL", "REJECTED"]])
    
    return ProcessingResult(
        total_packages=total_lines,
        valid_packages=valid_packages,
        packages=packages,
        statistics={}
    )


def print_package_summary(package: Package, index: int) -> None:
    """Print a summary of a single package for debugging."""
    print(f"Package {index + 1}:")
    print(f"  Dimensions: {package.width} x {package.height} x {package.length}")
    print(f"  Mass: {package.mass}")
    print(f"  Volume: {package.volume}")
    print(f"  Stack: {package.stack}")
    if package.reject_reason:
        print(f"  Reject Reason: {package.reject_reason}")
    print()
