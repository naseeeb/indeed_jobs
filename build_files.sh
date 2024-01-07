#!/bin/bash

echo "BUILD START"

# Check Python version path
PYTHON_PATH=$(which python3.10)
echo "Python 3.10 Path: $PYTHON_PATH"

# Check Django version
$PYTHON_PATH -m django --version

# Install dependencies
$PYTHON_PATH -m pip install -r requirements.txt

# Run collectstatic
$PYTHON_PATH manage.py collectstatic --noinput --clear

echo "BUILD END"
