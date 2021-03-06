# Simple backend service based on Flask and Docker

## Table of Contents <a name = "contents"></a>

- [Table of Contents](#contents)
- [Introduction](#introduction)
- [Technologies](#technologies)
- [Data Structure](#data-structure)
- [Environment variables](#env-vars)
- [Run locally](#development)
- [Deploy](#deploy)
  - [CI/CD](#ci-cd)
  - [Manual deployment](#manual-deployment)
- [Use](#use)
- [Api Documentation](#api-documentation)

## Introduction
This is an application writen Python using the Flask framework and Docker that manages a database. It provides a simple interface for adding, updating, removing, and listing records for a PostgreSQL schema in a simple way.

The challenge that this application solves is to create a model and backend service for the dataset found in this [file](examples/dataset/sample_data.csv). This was solved by designing an optimized schema to store the rows of the dataset and an API to register and read information in a simple way.
## Technologies <a name = "technologies"></a>

In the development of this application the following technologies were used:

- [Python](https://www.python.org/): The programming language used in this application.
- [Flask](https://flask.palletsprojects.com/en/2.1.x/): The python web framework to manage the api.
- [Docker](https://www.docker.com/): The containerization technology used in this application.
- [PostgreSQL](https://www.postgresql.org/): The database technology for storing the directory information.
- [Nginx](https://www.nginx.com/): The web server technology used in this application.


## Data Structures <a name= "data-structure"></a>

The model E-R diagram below shows the data structure designed for database of this application

<img src="database/ER_diagram.svg" width="80%" height="40%">

and the script to build the database if found in the [database/create_db.sql](database/create_db.sql) file.



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
Once you have set the default [environment variables](#env-vars), you can run the application locally by running the following docker commands:

1. Build the application
```bash
docker-compose up -d --build
```

After running the command, you can access the application by visiting [http://localhost:5000/](http://localhost:5000/) and you will see a hello message
```json
{
  "message": "Welcome to the flask server. This application is a test for Xal Digital"
}
```

The logs could be displayed by running the next command:

```bash
docker-compose logs -f
```

and you can stop the application by running the following command:

```bash
docker-compose down -v
```


## Deployment <a name = "deploy"></a>

First at all, for the deployment you must set the variable `FLASK_ENV` to `production`.
Then, you can follow one of the following methods to deploy the application.
### CI/CD <a name = "ci-cd"></a>

CI/CD pipeline based on [github actions](https://github.com/features/actions) was implemented for the application deployment on an EC2 machine.

To execute this pipeline in the github repository we need to set new environment variables that were used to connect to the instance where our application will live.

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `SSH_PRIVATE_KEY` | `string` | **Required**. This will be your `.pem` file which you will use to login to the instance |
| `REMOTE_HOST` | `string` | **Required**. Public DNS record of the instance, it will look something like this *ec2-xx-xxx-xxx-xxx.us-west-2.compute.amazonaws.com* |
| `REMOTE_USER` | `string` | **Required**. Will be the username of the EC2 instance, usually *ubuntu*. |
| `TARGET` | `string` | **Required**.  Is where you want to deploy your code. |

These new variables along with the application's variables for the production environment are set in the repository configuration in the environment variables section. For more information on how to set the variables please visit [this link](https://docs.github.com/es/actions/learn-github-actions/environment-variables) where you will find more information about it. 

Once you have all set, you can just commit your changes to the `master` branch of this repository 

### Manual deployment <a name = "manual-deployment"></a>
For manual deployment, you should go to your instance and run the following commands manually:

1. Build the application
```bash
docker-compose -f docker-compose.prod.yml up -d --build
```

After running the command, you can access the application by visiting [http://localhost:5000/](http://localhost:5000/) and you will see a hello message
```json
{
  "message": "Welcome to the flask server. This application is a test for Xal Digital"
}
```
2. Build the database
```bash
docker-compose -f docker-compose.prod.yml exec web python manage.py migrate
```
This commands execute the queries for create the schema and tables of the model. 

---
**NOTE**

This command is just for the first time you are going to deploy your application. Keep in mind that it deletes the entire schema including the data. 

---

Once the database is created, you can now use the api endpoints.


The logs could be displayed by running the next command:
```
docker-compose -f docker-compose.prod.yml logs -f
```
and you can stop the application by running the following command:
```
docker-compose -f docker-compose.prod.yml down -v 
```

## Use <a name = "use"></a>

Once your application is running, you can find a example application written in Python that shows how you can use the api programmatically, This application is found in the [examples/](examples/) folder. The [script](examples/main.py) reads the [sample_data.csv](examples/dataset/sample_data.csv) file and inserts the data into the database using the api.

To run the application, go to the [folder](examples/) and follow the next steps:


1. Set the environment variable `APP_HOST` to `http://localhost:5000/` if you are running the application locally. Otherwise, set the environment variable `APP_HOST` to the public DNS record of the instance.
```bash
export APP_HOST="http://localhost:5000/"
```

2. Create and activate a python virtual environment with [venv](https://docs.python.org/3/library/venv.html)
```bash
pyton3 -m venv venv
source venv/bin/activate
```

3. Install the dependencies
```bash
pip install -r requirements.txt
```

4. Run the application
```bash
python main.py
```

It will make some post requests to the api and you will see the logs.

## Api Documentation <a name = "api-documentation"></a>

You can find the documentation for the api in the [docs/api_documentation.md](docs/api_documentation.md) file.