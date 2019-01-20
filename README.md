[![Build Status](https://travis-ci.org/brauls/ingredients-service.svg?branch=master)](https://travis-ci.org/brauls/ingredients-service)
[![Coverage Status](https://coveralls.io/repos/github/brauls/ingredients-service/badge.svg?branch=master)](https://coveralls.io/github/brauls/ingredients-service?branch=master)

# ingredients-service
REST service that provides ingredients along with their availability per month

## notes

### run postgres locally using docker
* nice [quickstart video](https://www.youtube.com/watch?v=A8dErdDMqb0)
* [postgres image](https://hub.docker.com/_/postgres/) to use
* [psql docs](https://www.postgresql.org/docs/current/app-psql.html)
* create and start docker container from postgres image
    * `docker run --name ingredients-postgres -e POSTGRES_PASSWORD=*** -d -p 5432:5432 postgres`
* create database and execute queries
    * `docker exec -it ingredients-postgres psql -U postgres`
    * `CREATE DATABASE ingredientsdb;`
    * `\l` to list all databases
    * `\c ingredientsdb` to connect to the database
    * `\q` + `ENTER` to leave the session
    * 