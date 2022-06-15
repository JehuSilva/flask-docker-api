# Directory Flask Application

## Table of Contents <a name = "contents"></a>

- [Table of Contents](#contents)
- [Introduction](#introduction)
- [Technologies](#technologies)
- [Data Structures](#data-structures)
- [Environment variables](#env-vars)
- [Run locally](#run-locally)
- [Deployment](#deployment)

## Introduction
This is an application writen Python using the Flask framework and Docker that manages a directory database. It provides a simple interface for adding, updating, removing, and listing an employees directory.

The challenge that this application tries to solve is to create a management model for the dataset found in this [file](services/python_server/dataset/sample_data.csv).
## Technologies <a name = "technologies"></a>

In the development of this application the following technologies were used:

- [Python](https://www.python.org/): The programming language used in this application.
- [Flask](https://flask.palletsprojects.com/en/2.1.x/): The python web framework to manage the api.
- [Docker](https://www.docker.com/): The containerization technology used in this application.
- [PostgreSQL](https://www.postgresql.org/): The database technology for storing the directory information.


## Data Structures <a name= "data-structure"></a>

The model E-R diagram below shows the data structure designed for database of this application.

<img src="https://raw.githubusercontent.com/JehuSilva/register_api/develop/database/ER_diagram.svg" width="80%" height="40%">

## Environment Variables <a name = "env-vars"></a>

To run this application you must set the following environment variables:

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `FLASK_ENV` | `string` | **Required**. The environment variable that determines whether the application is in development or production mode. |
| `FLASK_APP` | `string` | **Required**. The environment variable that determines which application is run. |
| `POSTGRES_HOST` | `string` | **Required**. Hostname of the database. |
| `POSTGRES_PASSWORD` | `string` | **Required**. Password of the database. |
| `POSTGRES_USER` | `string` | **Required**. Username of the database. |
| `POSTGRES_DB` | `string` | **Required**. Name of the database. |
| `POSTGRES_PORT` | `int` | **Required**. Port of the database. |


By default, you can create you `.env` file in the root directory of the project with the following contents:
```bash
export FLASK_ENV="development"
export FLASK_APP="app/__init__.py"
export POSTGRES_HOST="db"
export POSTGRES_PASSWORD="postgres"
export POSTGRES_USER="postgres"
export POSTGRES_DB="postgres"
export POSTGRES_PORT=5432
```

Then, expose the environment variables in your terminal by running the following command:
```bash
source .env
```


## Run locally <a name = "run-locally"></a>
Once you have set the [environment variables](#env-vars), you can run the application locally by running the following docker command:

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
## Deployment <a name = "deployment"></a>
### Development

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
