# syntax=docker/dockerfile:1
# Python base
FROM python:3.9-slim-buster

# Set-up project directory
WORKDIR /usr/src/app/

# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update && apt-get install -y netcat

# Upgrade pip
RUN pip install --upgrade pip

# Copy requirements.txt
COPY requirements.txt /usr/src/app/

# Install python packages
RUN pip install -r requirements.txt

# Copy source code
COPY . /usr/src/app/
