#!/usr/bin/env python3
"""
Test script for Flight Price Predictor app
Run: python test_app.py
"""

import sys
import requests
import subprocess
import time
from pathlib import Path

def test_imports():
    """Test all required imports"""
    try:
        import streamlit
        import pandas
        import numpy
        import sklearn
        import pickle
        print("✓ All imports successful")
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def test_files():
    """Test required files exist"""
    required_files = [
        'app.py',
        'requirements.txt',
        '.streamlit/config.toml',
        'model_artifacts.pkl',
        'Indian Airlines.csv'
    ]
    
    missing = []
    for file in required_files:
        if not Path(file).exists():
            missing.append(file)
    
    if missing:
        print(f"❌ Missing files: {missing}")
        return False
    
    print("✓ All required files present")
    return True

def test_app_syntax():
    """Test app.py syntax"""
    try:
        import ast
        with open('app.py', 'r', encoding='utf-8') as f:
            ast.parse(f.read())
        print("✓ App syntax valid")
        return True
    except SyntaxError as e:
        print(f"❌ Syntax error: {e}")
        return False

def test_local_run():
    """Test app runs locally"""
    try:
        # Start streamlit in background
        process = subprocess.Popen([
            sys.executable, '-m', 'streamlit', 'run', 'app.py',
            '--server.port', '8502',
            '--server.headless', 'true'
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Wait for startup
        time.sleep(10)
        
        # Test health endpoint
        try:
            response = requests.get('http://localhost:8502?health=check', timeout=5)
            if response.status_code == 200:
                print("✓ App runs locally and health check passes")
                success = True
            else:
                print(f"❌ Health check failed: {response.status_code}")
                success = False
        except requests.RequestException as e:
            print(f"❌ Failed to connect to app: {e}")
            success = False
        
        # Cleanup
        process.terminate()
        process.wait()
        return success
        
    except Exception as e:
        print(f"❌ Failed to start app: {e}")
        return False

def main():
    """Run all tests"""
    print("🧪 Testing Flight Price Predictor App\n")
    
    tests = [
        ("File Check", test_files),
        ("Import Check", test_imports),
        ("Syntax Check", test_app_syntax),
        ("Local Run", test_local_run)
    ]
    
    results = []
    for name, test_func in tests:
        print(f"Running {name}...")
        result = test_func()
        results.append(result)
        print()
    
    # Summary
    passed = sum(results)
    total = len(results)
    
    print(f"📊 Test Results: {passed}/{total} passed")
    
    if passed == total:
        print("🎉 All tests passed! Ready for deployment.")
        return 0
    else:
        print("❌ Some tests failed. Please fix issues before deploying.")
        return 1

if __name__ == "__main__":
    sys.exit(main())