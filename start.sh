#!/bin/bash

# Apply database migrations
docker-compose run web python manage.py migrate

# Collect static files
docker-compose run web python manage.py collectstatic --noinput

# Start all services
docker-compose up --build
