#!/bin/bash
set -e

# Check that a virtual environment name has been provided
if [ -z "$1" ]; then
  echo "Usage: $0 <virtualenv_name>. No virtual environment name provided, so defaulting to `.venv`"
  VENV=".venv"
fi

if [ -d "$1" ]; then
  echo "Virtual environment $1 already exists"
  exit 1
else
  echo "Creating virtual environment $1"
  VENV="$1"
fi

# create and activate virtual environment
python3 -m venv $VENV
source $VENV/bin/activate

# update pip
pip install --upgrade pip