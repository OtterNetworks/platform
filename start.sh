#!/bin/bash

# Create the database
for i in {1..5}
    do python createDB.py && break || sleep 10 
done

# Run the latest migrations
flask db upgrade

# Start the server
/usr/local/bin/gunicorn --config /app/gunicorn.conf app:app
