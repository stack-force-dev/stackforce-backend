FROM python:3.10.5-slim

LABEL maintainer="Alexey Kudimov"

ENV PYTHONUNBUFFERED=1
ENV TZ='Europe/Moscow'

RUN apt update && apt install -y vim
RUN mkdir /etc/app

WORKDIR /app
RUN pip install --no-cache-dir poetry

COPY pyproject.toml poetry.lock /app/
RUN poetry config virtualenvs.create false &&\
  poetry install --no-interaction --no-ansi

COPY . .