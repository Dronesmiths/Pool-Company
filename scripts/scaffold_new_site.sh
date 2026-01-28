#!/bin/bash

# Scaffold New Site Script
# Usage: ./scripts/scaffold_new_site.sh

# 1. Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}=== Workflow Factory Scaffolder ===${NC}"

# 2. Input
read -p "Enter New Project Name (e.g. 'Diaz_Landscaping'): " PROJECT_NAME
if [ -z "$PROJECT_NAME" ]; then
    echo "Project Name is required."
    exit 1
fi

# 3. Path Setup
CURRENT_DIR=$(pwd)
PARENT_DIR="$(dirname "$CURRENT_DIR")"
NEW_PROJECT_PATH="$PARENT_DIR/$PROJECT_NAME"

echo -e "creating new project at: ${GREEN}$NEW_PROJECT_PATH${NC}"

if [ -d "$NEW_PROJECT_PATH" ]; then
    echo "Directory already exists. Aborting."
    exit 1
fi

# 4. Create and Copy
mkdir -p "$NEW_PROJECT_PATH"

# Copy Strategy Files (excluding .git, scripts, and this script itself to avoid recursion issues if structure changes)
# Taking all markdown files and the folders
echo "Copying factory resources..."
cp *.md "$NEW_PROJECT_PATH/" 2>/dev/null
cp factory_config.json "$NEW_PROJECT_PATH/"
cp -r scripts "$NEW_PROJECT_PATH/"
cp -r github_templates "$NEW_PROJECT_PATH/.github" 2>/dev/null

# 5. Initialize New Repo
cd "$NEW_PROJECT_PATH"
echo "Initializing new Git repository..."
git init
git checkout -b main

# 6. Initialize Config
echo "Resetting Config..."
# We leave the factory_config.json as is, user must edit it.

echo -e "${GREEN}=== Scaffolding Complete ===${NC}"
echo "1. Go to directory: cd $NEW_PROJECT_PATH"
echo "2. Edit Configuration: nano factory_config.json"
echo "3. Review Plan: code DEPLOYMENT_ORDER.md"
