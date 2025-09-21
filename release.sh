#!/bin/bash

# Simple Weather Card Release Script
# This script helps create releases for HACS compatibility

set -e

echo "🚀 Simple Weather Card Release Script"
echo "====================================="

# Check if we're in a git repository
if [ ! -d ".git" ]; then
    echo "❌ Not in a git repository"
    exit 1
fi

# Check if there are uncommitted changes
if [ -n "$(git status --porcelain)" ]; then
    echo "❌ There are uncommitted changes. Please commit or stash them first."
    exit 1
fi

# Get version from package.json
VERSION=$(node -p "require('./package.json').version")
echo "📦 Version: $VERSION"

# Build the project
echo "🔨 Building project..."
npm run build

# Copy built file to root for HACS
echo "📋 Copying built file to root..."
cp dist/simple-weather-card-bundle.js simple-weather-card-bundle.js

# Validate HACS compatibility
echo "✅ Validating HACS compatibility..."
python3 validate_hacs.py

# Create git tag
echo "🏷️  Creating git tag v$VERSION..."
git tag "v$VERSION"

echo ""
echo "✅ Release preparation complete!"
echo ""
echo "Next steps:"
echo "1. Push the tag: git push origin v$VERSION"
echo "2. GitHub Actions will automatically create the release"
echo "3. The release will include all necessary files for HACS"
echo ""
echo "Files included in release:"
echo "- simple-weather-card-bundle.js"
echo "- info.md"
echo "- hacs.json"
echo "- README.md"
echo "- CHANGELOG.md"
