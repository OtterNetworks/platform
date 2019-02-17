#!/bin/bash

# Create the database
python createDB.py

# Run the latest migrations
flask db upgrade

# Start the server
/usr/local/bin/gunicorn --config /app/gunicorn.conf app:app
