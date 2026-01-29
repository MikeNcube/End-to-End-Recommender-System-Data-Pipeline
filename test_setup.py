#!/usr/bin/env python3
"""Basic test to verify project setup."""

import os
import sys

def test_imports():
    """Test that basic imports work."""
    print("Testing imports...")
    
    try:
        import pandas
        print("✓ pandas imported successfully")
    except ImportError:
        print("✗ pandas import failed")
        return False
    
    try:
        import boto3
        print("✓ boto3 imported successfully")
    except ImportError:
        print("✗ boto3 import failed")
        return False
    
    return True

def test_project_structure():
    """Test that project structure exists."""
    print("\nTesting project structure...")
    
    required_dirs = ['src', 'tests', 'data', 'config']
    required_files = ['README.md', 'requirements.txt', '.env.example']
    
    all_good = True
    
    for dir_name in required_dirs:
        if os.path.exists(dir_name):
            print(f"✓ Directory exists: {dir_name}")
        else:
            print(f"✗ Directory missing: {dir_name}")
            all_good = False
    
    for file_name in required_files:
        if os.path.exists(file_name):
            print(f"✓ File exists: {file_name}")
        else:
            print(f"✗ File missing: {file_name}")
            all_good = False
    
    return all_good

def main():
    """Run all tests."""
    print("=== Project Setup Test ===\n")
    
    tests_passed = 0
    tests_total = 0
    
    # Run import test
    tests_total += 1
    if test_imports():
        tests_passed += 1
    
    # Run structure test
    tests_total += 1
    if test_project_structure():
        tests_passed += 1
    
    # Summary
    print(f"\n=== Test Summary ===")
    print(f"Passed: {tests_passed}/{tests_total}")
    
    if tests_passed == tests_total:
        print("✓ All tests passed! Project is set up correctly.")
        return 0
    else:
        print("✗ Some tests failed. Please check the setup.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
