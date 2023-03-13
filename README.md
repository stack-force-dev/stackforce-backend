# Stack Force Backend


## Technologies
* Python
* FastAPI
* PSQL

## Environment
    SECRET_KEY=<your key>
    DATABASE_URL=postgresql://<user>:<password>@<host>:<port>/<dbname>

    ADMIN_USERNAME=<some string>
    ADMIN_PASSWORD=<some string>

## Launch
    docker-compose -f docker-compose.yml up -d

## Logs
    docker logs --follow sf_server

## Shell
    docker exec -it sf_server bash

## Migrate
    alembic upgrade heads

#### P.S. You may configure Postgres in docker-compose file.
