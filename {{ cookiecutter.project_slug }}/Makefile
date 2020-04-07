.PHONY: clean-test help
.DEFAULT_GOAL := help

define BROWSER_PYSCRIPT
import os, webbrowser, sys

from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"
COMPOSE_DEVELOPMENT_FILES := docker-compose.yml docker-compose.development.yml
COMPOSE_PRODUCTION_FILES := docker-compose.yml docker-compose.production.yml

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean-test: ## remove test and coverage artifacts
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

lint: ## check style with flake8
	flake8 yandex_market_language tests

test: ## run tests quickly with the default Python
	pytest

coverage: ## check code coverage quickly with the default Python
	coverage run --source yandex_market_language -m pytest
	coverage report -m
	coverage html
	$(BROWSER) htmlcov/index.html

docker-compose-down:  ## stops containers and removes containers, networks, volumes, and images created by `up`.
	docker-compose down
docker-compose-down-full:  ## same as docker-compose-down, but also removes volumes and not defined containers
	docker-compose down --remove-orphans -v

docker-compose-up:  ## run docker-compose
	docker-compose $(foreach file, $($(COMPOSE_FILES)), -f $(file)) up --build
docker-compose-up-d:  ## run docker-compose with decouple mode
	docker-compose $(foreach file, $($(COMPOSE_FILES)), -f $(file)) up --build -d

development-up: ## run docker-compose development
	make docker-compose-up COMPOSE_FILES=COMPOSE_DEVELOPMENT_FILES
development-up-d: ## run docker-compose development with decouple mode
	make docker-compose-up-d COMPOSE_FILES=COMPOSE_DEVELOPMENT_FILES

production-up:  ## run docker-compose production
	make docker-compose-up COMPOSE_FILES=COMPOSE_PRODUCTION_FILES
production-up-d:  ## run docker-compose production with decouple mode
	make docker-compose-up-d COMPOSE_FILES=COMPOSE_PRODUCTION_FILES
