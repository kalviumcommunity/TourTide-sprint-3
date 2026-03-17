#!/usr/bin/env python3
"""
Environment Setup Verification Script
This script verifies that Python and Anaconda are properly installed
and ready for Data Science work.
"""

import sys
import subprocess
import os

def check_python_installation():
    """Check Python installation and version."""
    print("=== Python Installation Check ===")
    version = sys.version
    print(f"✓ Python version: {version}")
    print(f"✓ Python executable: {sys.executable}")
    return True

def check_conda_installation():
    """Check Conda installation."""
    print("\n=== Conda Installation Check ===")
    try:
        # Try to find conda in common locations
        conda_paths = [
            r"C:\Users\amuly\anaconda3\Scripts\conda.exe",
            r"C:\Users\amuly\anaconda3\condabin\conda.bat",
            "conda"
        ]
        
        conda_found = False
        for conda_path in conda_paths:
            try:
                result = subprocess.run([conda_path, "--version"], 
                                      capture_output=True, text=True, timeout=10)
                if result.returncode == 0:
                    print(f"✓ Conda found at: {conda_path}")
                    print(f"✓ Conda version: {result.stdout.strip()}")
                    conda_found = True
                    break
            except (subprocess.TimeoutExpired, FileNotFoundError):
                continue
        
        if not conda_found:
            print("✗ Conda not found in standard locations")
            return False
            
        return True
    except Exception as e:
        print(f"✗ Error checking conda: {e}")
        return False

def test_basic_python_functionality():
    """Test basic Python functionality for DS work."""
    print("\n=== Basic Python Functionality Test ===")
    
    try:
        # Test basic imports
        import math
        import json
        import datetime
        print("✓ Basic Python modules imported successfully")
        
        # Test simple calculation
        result = sum(range(100))
        print(f"✓ Basic calculation test: sum(range(100)) = {result}")
        
        # Test file operations
        with open("test_file.txt", "w") as f:
            f.write("Environment verification test")
        with open("test_file.txt", "r") as f:
            content = f.read()
        os.remove("test_file.txt")
        print("✓ File operations test passed")
        
        return True
    except Exception as e:
        print(f"✗ Basic functionality test failed: {e}")
        return False

def main():
    """Main verification function."""
    print("Data Science Environment Setup Verification")
    print("=" * 50)
    
    checks = [
        check_python_installation(),
        check_conda_installation(),
        test_basic_python_functionality()
    ]
    
    print("\n" + "=" * 50)
    if all(checks):
        print("🎉 ALL CHECKS PASSED! Environment is ready for Data Science work.")
        print("\nNext steps:")
        print("1. Create conda environments for specific projects")
        print("2. Install data science packages (numpy, pandas, matplotlib, etc.)")
        print("3. Set up your development environment (IDE, Jupyter, etc.)")
        return 0
    else:
        print("❌ Some checks failed. Please review the output above.")
        return 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
