"""Demonstration of the FDE Package Sorting System."""

from src.fde import sort


def main():
    """Demonstrate the package sorting functionality with example cases."""
    print("🚀 FDE Package Sorting System Demo")
    print("=" * 40)
    
    # Test cases demonstrating different package types
    test_cases = [
        {
            "name": "Standard Package",
            "dimensions": (10, 10, 10),
            "mass": 5,
            "expected": "STANDARD"
        },
        {
            "name": "Bulky by Volume",
            "dimensions": (100, 100, 100),
            "mass": 10,
            "expected": "SPECIAL"
        },
        {
            "name": "Bulky by Dimension",
            "dimensions": (150, 50, 50),
            "mass": 10,
            "expected": "SPECIAL"
        },
        {
            "name": "Heavy Package",
            "dimensions": (50, 50, 50),
            "mass": 25,
            "expected": "SPECIAL"
        },
        {
            "name": "Rejected Package",
            "dimensions": (150, 100, 100),
            "mass": 25,
            "expected": "REJECTED"
        }
    ]
    
    for case in test_cases:
        width, height, length = case["dimensions"]
        mass = case["mass"]
        result = sort(width, height, length, mass)
        
        print(f"\n📦 {case['name']}:")
        print(f"   Dimensions: {width}×{height}×{length} cm")
        print(f"   Mass: {mass} kg")
        print(f"   Volume: {width * height * length:,} cm³")
        print(f"   Classification: {result}")
        
        # Verify result matches expectation
        status = "✅" if result == case["expected"] else "❌"
        print(f"   Status: {status} Expected {case['expected']}")
    
    print("\n🎯 All package classifications completed!")


if __name__ == "__main__":
    main()
