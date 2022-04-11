build:
	@docker-compose -f compose/local.yml build

run:
	@docker-compose -f compose/local.yml up -d

down:
	@docker-compose -f compose/local.yml down
