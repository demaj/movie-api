# Movie API
A Movie DB API built with Django, and DRF

## Getting Started

#### Requirements:

- docker
- docker-compose

#### Startup:
```commandline
docker-compose up -d --build
```

#### Make migrations:
```commandline
docker-compose exec web python /code/app/manage.py makemigrations
docker-compose exec web python /code/app/manage.py migrate
```

#### Populate DB

Exec:
```commandline
docker-compose exec web python /code/app/manage.py populate_db --path=/code/data/genres.csv --app_name=datadump --model_name=Genre
docker-compose exec web python /code/app/manage.py populate_db --path=/code/data/movies.csv --app_name=datadump --model_name=Movie
```

#### Execute tests
```commandline
./tests-run.sh
```
