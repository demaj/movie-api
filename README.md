# Movie API
A Movie Database API built with Django, Django REST framework, PostgreSQL and Docker

## Getting Started

#### Requirements:
```
- docker
```

#### Startup/Shutdown:
```bash
make start
make stop
make restart
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
```bash
docker compose exec -w /code/app web python manage.py populate_db --path=/code/data/genres.csv --app_name=core --model_name=Genre
docker compose exec -w /code/app web python manage.py populate_db --path=/code/data/movies.csv --app_name=core --model_name=Movie
docker compose exec -w /code/app web python manage.py populate_db --path=/code/data/networks.csv --app_name=core --model_name=Network
```

#### Export DB
```bash
docker compose exec -w /code/app web python manage.py export_db --path=/code/data/genres.csv --app_name=core --model_name=Genre
docker compose exec -w /code/app web python manage.py export_db --path=/code/data/movies.csv --app_name=core --model_name=Movie
docker compose exec -w /code/app web python manage.py export_db --path=/code/data/networks.csv --app_name=core --model_name=Network
```

#### Execute tests
```bash
make test
```

#### Deployment Checklist
```bash
make checklist
```

## To-Do:
- Healthcheck
- JSON Logging
- CorrelationId
- Rate Limiting
- Monitoring

## To-Check:
- [django-SHOP](https://django-shop.readthedocs.io/en/latest/index.html)
- [wagtail](https://github.com/wagtail/wagtail)


-c "cd /code/app && python -m gunicorn config.wsgi:application --bind 0.0.0.0:8080 --reload"