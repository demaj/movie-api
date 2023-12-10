# Movie API
A Movie Database API built with Django, Django REST framework, PostgreSQL and Docker

## Getting Started

#### Requirements:
- docker

#### Startup/Shutdown:
```bash
make start
make stop
```

#### Make migrations:
```bash
make migrations
make migrate
```

#### Create superuser
```bash
make superuser
```

#### Populate DB
Exec:
```commandline
docker-compose exec -w /code/app web python manage.py populate_db --path=/code/data/genres.csv --app_name=core --model_name=Genre
docker-compose exec -w /code/app web python manage.py populate_db --path=/code/data/movies.csv --app_name=core --model_name=Movie
docker-compose exec -w /code/app web python manage.py populate_db --path=/code/data/networks.csv --app_name=core --model_name=Network
```

#### Execute tests
```bash
make test
```
