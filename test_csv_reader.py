#!/usr/bin/env python3
"""Test script for CSV reading and validation."""

import sys
import os

# Add src to path to import fde modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from fde.io import read_packages_csv, print_package_summary


def main():
    """Test the CSV reading functionality."""
    csv_file = "packages.csv"
    
    print("Testing CSV reading and validation...")
    print("=" * 50)
    
    try:
        result = read_packages_csv(csv_file)
        
        print(f"Total lines processed: {result.total_packages}")
        print(f"Valid packages: {result.valid_packages}")
        print(f"Packages parsed: {len(result.packages)}")
        print()
        
        # Count by stack
        stacks = {}
        reject_reasons = {}
        
        for package in result.packages:
            stack = package.stack or "UNPARSED"
            stacks[stack] = stacks.get(stack, 0) + 1
            
            if package.reject_reason:
                reason = package.reject_reason
                reject_reasons[reason] = reject_reasons.get(reason, 0) + 1
        
        print("Distribution by stack:")
        for stack, count in sorted(stacks.items()):
            print(f"  {stack}: {count}")
        
        print("\nReject reasons:")
        for reason, count in sorted(reject_reasons.items()):
            print(f"  {reason}: {count}")
        
        print("\nFirst 10 packages details:")
        print("-" * 40)
        for i, package in enumerate(result.packages[:10]):
            print_package_summary(package, i)
        
        # Show some rejected packages
        rejected_packages = [p for p in result.packages if p.stack == "REJECTED"]
        if rejected_packages:
            print(f"\nSample rejected packages (showing first 5 of {len(rejected_packages)}):")
            print("-" * 40)
            for i, package in enumerate(rejected_packages[:5]):
                print_package_summary(package, i)
        
    except Exception as e:
        print(f"Error: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
