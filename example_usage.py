#!/usr/bin/env python3
"""Example usage of the CSV reading and validation functionality."""

import sys
import os

# Add src to path to import fde modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from fde import read_packages_csv


def main():
    """Demonstrate CSV reading and basic statistics."""
    csv_file = "packages.csv"
    
    print("FDE Package Analysis")
    print("=" * 50)
    
    try:
        # Read and process the CSV
        result = read_packages_csv(csv_file)
        
        print(f"📦 Total packages processed: {result.total_packages}")
        print(f"✅ Valid packages: {result.valid_packages}")
        print()
        
        # Calculate basic statistics by stack
        stacks = {"STANDARD": 0, "SPECIAL": 0, "REJECTED": 0}
        reject_reasons = {}
        
        for package in result.packages:
            if package.stack:
                stacks[package.stack] += 1
                
            if package.reject_reason:
                reason = package.reject_reason
                reject_reasons[reason] = reject_reasons.get(reason, 0) + 1
        
        # Display distribution
        print("📊 Package Distribution:")
        for stack, count in stacks.items():
            percentage = (count / len(result.packages)) * 100 if result.packages else 0
            print(f"  {stack:10}: {count:3} packages ({percentage:.1f}%)")
        
        print()
        print("❌ Top Rejection Reasons:")
        sorted_reasons = sorted(reject_reasons.items(), key=lambda x: x[1], reverse=True)
        for reason, count in sorted_reasons[:5]:
            print(f"  • {reason}: {count} packages")
        
        print()
        print("✨ Successfully implemented CSV reading and validation!")
        print("Next step: Implement detailed statistics and reporting.")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
