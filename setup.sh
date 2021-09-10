#!/bin/bash

python3 -m venv venv  # Create a venv folder for the virtual environment
. venv/bin/activate  # Run the virtual environment
pip3 install -r ./requirements.txt  # Install the prerequisites
