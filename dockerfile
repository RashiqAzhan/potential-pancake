# syntax=docker/dockerfile:1

# Pull base image
FROM python:3.9.6

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install pipenv
COPY Pipfile Pipfile.lock /code/
RUN pipenv install --system

# Copy project into docker container
COPY . /code/
