# Docker Flask Application

Application still under development.
## Table of Contents

Under development

## General Information

## Under development

## Technologies

- [Flask](https://flask.palletsprojects.com/en/2.1.x/)
- [Docker](https://www.docker.com/)
- [PostgreSQL](https://www.postgresql.org/)

## Build

### Development

Instructions for setting up the development environment:

Update the file permissions locally:

```bash
chmod +x services/web/entrypoint.sh
```
After that, run the following command to build the image:

```bash
docker-compose up -d --build
docker-compose exec web python manage.py seed_db
docker-compose exec db psql --username=postgres --dbname=postgres
```

If you want to kill the containers and clean the volumes:

```bash
docker-compose down -v
```

