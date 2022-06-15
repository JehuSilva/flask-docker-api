# Directory Flask Application

## Table of Contents <a name = "contents"></a>

- [Table of Contents](#contents)
- [Introduction](#introduction)
- [Technologies](#technologies)
- [Data Structure](#data-structure)
- [Environment variables](#env-vars)
- [Development Environment](#development)
- [Production environment](#production)
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
- [Gnginx](https://www.nginx.com/): The web server technology used in this application.


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


## Development Environment <a name = "development"></a>
Once you have set the default [environment variables](#env-vars), you can run the application locally by running the following docker command:
```
docker-compose up -d --build
```
After running the command, you can access the application by visiting [http://localhost:5000/](http://localhost:5000/). You will see the following hello message:
```json
{
  "message": "hello from flask server**"
}
```

The logs could be viewed by running the following command:
```
docker-compose logs -f
```

and you can stop the application by running the following command:
```
docker-compose down -v
```

## Production environment <a name = "production"></a>

For the production environment, you must set the variable `FLASK_ENV` to `production` and then run the following command:

```bash
docker-compose -f docker-compose.prod.yml up -d --build
```

After running the command, you can access the application by visiting [http://localhost:5000/](http://localhost:5000/). You will see the following hello message:
```json
{
  "message": "hello from flask server**"
}
```
After figuring out the server is running, create the database and tables by running the following command:

```bash
docker-compose -f docker-compose.prod.yml exec web python manage.py migrate
```
Once the database is created, you can now use the api endpoints.


If you want to see the logs of the application, you can run the following command:
```
docker-compose -f docker-compose.prod.yml logs -f
```
and you can kill the application by runniong the following command:
```
docker-compose -f docker-compose.prod.yml down -v 
```
