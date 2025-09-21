#!/usr/bin/env python3
"""
HACS Validation Script for Simple Weather Card
Validates that the repository meets HACS requirements
"""

import json
import os
import sys
from pathlib import Path

def validate_hacs_json():
    """Validate hacs.json file"""
    print("Validating hacs.json...")
    
    if not os.path.exists("hacs.json"):
        print("❌ hacs.json not found")
        return False
    
    try:
        with open("hacs.json", "r") as f:
            hacs_config = json.load(f)
        
        required_fields = ["name", "content_in_root", "filename"]
        for field in required_fields:
            if field not in hacs_config:
                print(f"❌ Missing required field: {field}")
                return False
        
        if hacs_config["content_in_root"] is not True:
            print("❌ content_in_root must be true for Lovelace cards")
            return False
        
        if hacs_config["filename"] != "simple-weather-card-bundle.js":
            print("❌ filename must be 'simple-weather-card-bundle.js'")
            return False
        
        print("✅ hacs.json is valid")
        return True
        
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON in hacs.json: {e}")
        return False

def validate_files():
    """Validate required files exist"""
    print("Validating required files...")
    
    required_files = [
        "info.md",
        "README.md",
        "hacs.json",
        "simple-weather-card-bundle.js"
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ Missing required files: {', '.join(missing_files)}")
        return False
    
    print("✅ All required files present")
    return True

def validate_info_md():
    """Validate info.md has required content"""
    print("Validating info.md...")
    
    try:
        with open("info.md", "r") as f:
            content = f.read()
        
        required_sections = [
            "# Simple Weather Card",
            "## Features",
            "## Installation",
            "## Configuration"
        ]
        
        missing_sections = []
        for section in required_sections:
            if section not in content:
                missing_sections.append(section)
        
        if missing_sections:
            print(f"❌ Missing required sections in info.md: {', '.join(missing_sections)}")
            return False
        
        print("✅ info.md is valid")
        return True
        
    except Exception as e:
        print(f"❌ Error reading info.md: {e}")
        return False

def validate_bundle():
    """Validate the bundle file"""
    print("Validating simple-weather-card-bundle.js...")
    
    try:
        with open("simple-weather-card-bundle.js", "r") as f:
            content = f.read()
        
        if len(content) < 1000:  # Basic size check
            print("❌ Bundle file seems too small")
            return False
        
        if "simple-weather-card" not in content:
            print("❌ Bundle doesn't contain expected content")
            return False
        
        print("✅ Bundle file is valid")
        return True
        
    except Exception as e:
        print(f"❌ Error reading bundle file: {e}")
        return False

def main():
    """Main validation function"""
    print("🔍 Validating HACS compatibility...")
    print("=" * 50)
    
    validations = [
        validate_hacs_json,
        validate_files,
        validate_info_md,
        validate_bundle
    ]
    
    all_valid = True
    for validation in validations:
        if not validation():
            all_valid = False
        print()
    
    print("=" * 50)
    if all_valid:
        print("✅ All validations passed! Repository is HACS compatible.")
        sys.exit(0)
    else:
        print("❌ Some validations failed. Please fix the issues above.")
        sys.exit(1)

if __name__ == "__main__":
    main()
