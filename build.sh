#!/bin/bash

# Set up environment variables from .env
if [ -f .env ]; then
    export $(cat .env | grep -v '#' | xargs)
fi

# Install dependencies
echo "Installing requirements..."
pip install -r requirements.txt

# Run migrations if necessary
echo "Running database migrations..."
alembic upgrade head
#!/bin/bash

# Set up environment variables from .env
if [ -f .env ]; then
    export $(cat .env | grep -v '#' | xargs)
fi

# Install dependencies
echo "Installing requirements..."
pip install -r requirements.txt

# Run migrations if necessary
echo "Running database migrations..."
alembic upgrade head
