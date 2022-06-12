# Docker Flask Application

Application still under development.
## Table of Contents

Under development

## General Information

Under development

## Technologies

- [Flask](https://flask.palletsprojects.com/en/2.1.x/)
- [Docker](https://www.docker.com/)
- [PostgreSQL](https://www.postgresql.org/)

## Build

### Prerequisites

To use the application you must to difine you environment variables. You must to create a `.env.dev` in the root directory of the project with the following content:

```bash
FLASK_APP=app/__init__.py
FLASK_ENV=development
DATABASE_URL=postgresql://postgres:postgres@db:5432/postgres
SQL_HOST=db
SQL_PORT=5432
DATABASE=postgres
```

### Development

Instructions for setting up the development environment:

Update the file permissions locally:

```bash
chmod +x services/web/entrypoint.sh
```
After that, run the following command to build the image:

```bash
docker-compose up -d --build
docker-compose exec db psql --username=postgres --dbname=postgres
```

If you want to kill the containers and clean the volumes:

```bash
docker-compose down -v
```

### Production

Instructions for setting up the production environment:


Update the file permissions locally:

```bash
chmod +x services/web/entrypoint.sh
```

After that, run the following command to build the image:

```bash
docker-compose -f docker-compose.prod.yml up -d --build
```

Build the database using the SQLAlchemy ORM:
```bash
docker-compose -f docker-compose.prod.yml exec web python manage.py migrate
```

If you want to kill the containers and clean the volumes:

```bash
docker-compose -f docker-compose.prod.yml down -v
```
