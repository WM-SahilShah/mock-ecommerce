#!/bin/bash

# Set up environment variables from .env
if [ -f .env ]; then
    export $(cat .env | grep -v '#' | xargs)
fi

# Check for virtual environment
if [ ! -d "venv" ]; then
    echo "Virtual environment not found. Creating one..."
    python3 -m venv venv
fi

# Install dependencies
echo "Installing requirements..."
# pip install -r requirements.txt

# Run migrations if necessary
echo "Running database migrations..."
alembic upgrade head
