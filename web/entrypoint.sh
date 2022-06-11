#!/bin/sh

# Development steps definition
if [ "$FLASK_ENV" = "development" ]
then
    # It drops all existing tables and then creates the tables from the models, 
    #every time the container is run
    echo "Creating the database tables..."
    python manage.py create_db
    echo "Tables created"
fi

exec "$@"