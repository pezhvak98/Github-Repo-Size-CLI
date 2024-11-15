#!/bin/bash

# Project metadata
PROJECT_NAME="github-repo-size-cli"
VERSION="1.0.0"

# Terminal colors
GREEN="\033[1;32m"
RED="\033[1;31m"
RESET="\033[0m"

# Function to display messages
function echo_message() {
    echo -e "[${PROJECT_NAME}] $1"
}

# Function to handle errors
function handle_error() {
    echo -e "${RED}[ERROR] $1${RESET}"
    exit 1
}

# Check if the script is run with sufficient privileges
if [ "$EUID" -ne 0 ]; then
    handle_error "Please run the script as root (use sudo)."
fi

# Update package lists
echo_message "Updating package lists..."
sudo apt-get update || handle_error "Failed to update package lists. Check your internet connection."

# Ensure Python 3 and pip are installed
if ! command -v python3 &>/dev/null; then
    echo_message "Python3 is not installed. Installing..."
    sudo apt-get install -y python3 python3-pip || handle_error "Failed to install Python3 and pip."
else
    echo_message "Python3 is already installed."
fi

# Verify the existence of setup.py
if [ ! -f setup.py ]; then
    handle_error "'setup.py' not found in the current directory. Ensure the script is run from the project root."
fi

# Install Python dependencies (from setup.py or requirements.txt)
echo_message "Installing the Python package..."
if ! python3 setup.py install; then
    handle_error "Failed to install the Python package. Ensure 'setup.py' is correctly configured."
fi

# Verify the executable script exists
EXECUTABLE_SCRIPT="github_repo_size.py"
SYMLINK_PATH="/usr/local/bin/grs"
if [ ! -f "${EXECUTABLE_SCRIPT}" ]; then
    handle_error "Executable script '${EXECUTABLE_SCRIPT}' not found. Please check your project structure."
fi

# Create or update the symlink for the CLI tool
echo_message "Creating symlink for the CLI tool..."
if ! ln -sf "$(pwd)/${EXECUTABLE_SCRIPT}" "${SYMLINK_PATH}"; then
    handle_error "Failed to create symlink. Ensure you have sufficient permissions."
fi

# Final success message
echo -e "${GREEN}[${PROJECT_NAME}] Installation completed successfully!${RESET}"
echo_message "You can now run the tool using the command: grs"
