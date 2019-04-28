[![Build Status](https://travis-ci.org/brauls/ingredients-service.svg?branch=master)](https://travis-ci.org/brauls/ingredients-service)
[![Coverage Status](https://coveralls.io/repos/github/brauls/ingredients-service/badge.svg?branch=master)](https://coveralls.io/github/brauls/ingredients-service?branch=master)

# ingredients-service
REST service that provides ingredients along with their availability per month

## development

### prerequisites

* at least python 3.6
* [pipenv](https://docs.pipenv.org/en/latest/)
* [docker](https://www.docker.com/products/docker-desktop)
* a running docker container with the postgres development database
    * `docker run --name ingredients-postgres -e POSTGRES_PASSWORD=*** -d -p 5432:5432 postgres`
    * the password for the development database has to conform to the one specified in [`config.py`](/app/config.py)
    * initially create the database by `docker exec -it ingredients-postgres psql -U postgres` and then `CREATE DATABASE ingredientsdb;`

### database migration

* this project uses [flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/) for managing database revisions
* the migration repository was originally created using the command `pipenv run flask db init`
* workflow for future model changes
    * after some model changes in code perform `pipenv run flask db migrate -m "comment"`
    * manually check the created revision file in code
    * upgrade an existing database with `pipenv run flask db upgrade`

### running the service in dev mode

* `pipenv run flask run`

### running tests

* run all tests: `pipenv run pytest test/`
* run a specific test module: `pipenv run pytest test/template_test/api_overview_test.py`
* run a specific test by name: `pipenv run pytest -k "test_api_overview_status_and_content_type"`

## release process

* when pushing new changes to `origin/master` [Travis CI](https://travis-ci.org/) automatically checks out those changes, runs all tests and creates a coverage report for displaying the code coverage at [Coveralls](https://coveralls.io/)
* in case the [Travis CI](https://travis-ci.org/) Job succeeds the service is deployed automatically to the Staging stage of a [Heroku](https://www.heroku.com/) pipeline and the database migration is performed
* if the service is ready for production it can manually be promoted through the Pipeline view of [Heroku](https://www.heroku.com/)
* alongside that the promoted version should be tagged in the git repository