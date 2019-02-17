#!/bin/bash

python createDB.py

/usr/local/bin/gunicorn --config /app/gunicorn.conf app:app