#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# Function to print an error message and exit
function error_exit {
    echo "$1" 1>&2
    exit 1
}

# Create and activate virtual environment
echo "Creating virtual environment..."
python3 -m venv fake_env || error_exit "Failed to create virtual environment."

echo "Activating virtual environment..."
source fake_env/bin/activate || error_exit "Failed to activate virtual environment."

# Install dependencies
echo "Installing dependencies..."
pip install --upgrade pip || error_exit "Failed to upgrade pip."
pip install -r requirements.txt || error_exit "Failed to install dependencies from requirements.txt."

# Run migrations
echo "Running migrations..."
python manage.py makemigrations || error_exit "Failed to make migrations."
python manage.py migrate || error_exit "Failed to apply migrations."

# Generate dummy data
echo "Generating dummy data..."
python manage.py create_dummy_data || error_exit "Failed to generate dummy data."

# Run the Django development server
echo "Starting the development server..."
python manage.py runserver 8006|| error_exit "Failed to start the development server."

# Success message
echo "Setup complete. The project is ready to use and the development server is running."
