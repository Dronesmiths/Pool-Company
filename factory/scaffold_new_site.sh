#!/bin/bash

# Workflow-Factory V3 Scaffolder
# Usage: ./factory/scaffold_new_site.sh

# 1. Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}=== Workflow Factory V3 Scaffolder ===${NC}"

# 2. Input
read -p "Enter New Project Name (e.g. 'Diaz_Landscaping'): " PROJECT_NAME
if [ -z "$PROJECT_NAME" ]; then
    echo "Project Name is required."
    exit 1
fi

# 3. Path Setup
# Standardized to run from the root of the "Gold Master" project
FACTORY_ROOT=$(dirname "$0")
SOURCE_ROOT=$(pwd)
PARENT_DIR="$(dirname "$SOURCE_ROOT")"
NEW_PROJECT_PATH="$PARENT_DIR/$PROJECT_NAME"

echo -e "Creating new project at: ${GREEN}$NEW_PROJECT_PATH${NC}"

if [ -d "$NEW_PROJECT_PATH" ]; then
    echo "Directory already exists. Aborting."
    exit 1
fi

# 4. Create and Copy
mkdir -p "$NEW_PROJECT_PATH"

# Copy the "Public" site (the Gold Master state)
echo "Copying Gold Master site files..."
cp -r "$SOURCE_ROOT/about" "$SOURCE_ROOT/blog" "$SOURCE_ROOT/contact" "$SOURCE_ROOT/css" "$SOURCE_ROOT/images" "$SOURCE_ROOT/js" "$SOURCE_ROOT/privacy" "$SOURCE_ROOT/services" "$SOURCE_ROOT/terms" "$NEW_PROJECT_PATH/"
cp "$SOURCE_ROOT/index.html" "$SOURCE_ROOT/robots.txt" "$SOURCE_ROOT/sitemap.xml" "$SOURCE_ROOT/.gitignore" "$NEW_PROJECT_PATH/"

# Copy the "Factory" engine (The "Brain")
echo "Cloning Factory Engine..."
cp -r "$SOURCE_ROOT/factory" "$NEW_PROJECT_PATH/"

# 5. Initialize New Repo
cd "$NEW_PROJECT_PATH"
echo "Initializing new Git repository..."
git init
git checkout -b main

echo -e "${GREEN}=== Scaffolding Complete ===${NC}"
echo "1. Go to directory: cd $NEW_PROJECT_PATH"
echo "2. Edit Config: nano factory/factory_config.json"
echo "3. Review Plan: code factory/DEPLOYMENT_ORDER.md"
echo "4. Run Audit: python3 factory/scripts/preflight_audit.py"
