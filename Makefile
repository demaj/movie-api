.PHONY: start
start:
	@docker compose up -d --build

.PHONY: stop
stop:
	@docker compose down

.PHONY: restart
restart: stop start

.PHONY: shell
shell:
	@docker compose exec -w /code/app web bash

.PHONY: shell-db
shell-db:
	@docker compose exec db bash

.PHONY: migrations
migrations:
	@docker compose exec -w /code/app web python manage.py makemigrations

.PHONY: migrate
migrate:
	@docker compose exec -w /code/app web python manage.py migrate

.PHONY: superuser
superuser:
	@docker compose exec -w /code/app web python manage.py createsuperuser

.PHONY: logs
logs:
	@docker logs -f movie-web

.PHONY: clean
clean:
	@docker system prune --volumes --all --force

.PHONY: test
test:
	@docker compose exec -w /code/app web python manage.py test

.PHONY: freeze
freeze:
	python -m pip freeze > requirements.txt
