#!/usr/bin/env bash
set -x

docker-compose exec web sh -c "cd /code/app && pytest"
