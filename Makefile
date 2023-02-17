BASE_PROJECT_NAME := myproject
PROJECT_NAME := mymodule
DOCKER_IMAGE_TAG := $(BASE_PROJECT_NAME)/$(PROJECT_NAME)
DOCKER_CONTAINER_NAME := $(BASE_PROJECT_NAME)-$(PROJECT_NAME)

install-requirements: ## pip install requirements for app
	poetry install --no-root

install-dev-requirements: ## pip install requirements for tests
	poetry install --with dev

install-test-requirements: ## pip install requirements for tests
	poetry install --with test

install-all: ## pip install requirements for app and tests
	poetry install

test: ## run tests
	PYTHONPATH=. python -m pytest -sv ./matcher/tests

test-cov: ## run tests with coverage reports (for Jenkins)
	PYTHONPATH=. python -m pytest mymodule\
		-o junit_family=xunit2 -o cache_dir=/tmp \
		--cov-report xml:./reports/coverage.xml --junitxml=./reports/junit-result.xml \
		-sv ./mymodule/tests

run:  ## Run on host
	python -m mymodule.cli match---help

docker-build: ## run docker build to create docker image
	docker build . -t $(DOCKER_IMAGE_TAG)

docker-run-dev: ## run docker image in dev mode (with network=host and using the local .env)
	docker run --rm --net=host --name $(DOCKER_CONTAINER_NAME) -t $(DOCKER_IMAGE_TAG) .

docker-run-test: ## run tests on docker image in dev mode (with network=host and using the local .env)
	docker run --rm --net=host --env-file=.env --name $(DOCKER_CONTAINER_NAME) -t $(DOCKER_IMAGE_TAG) \
	python -m pytest -sv ./mymodule/tests

docker-clean: ## remove docker image
	docker rmi $(DOCKER_IMAGE_TAG) || exit 0

help:  ## This help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
