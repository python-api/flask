.PHONY: build-dev
build-dev:
	@if [ ! -f docker/development/.env ]; then \
		cp .env.example docker/development/.env; \
	fi
	docker compose -f docker/development/docker-compose.yaml build

.PHONY: up-dev
up-dev:
	@if [ ! -f docker/development/.env ]; then \
		cp .env.example docker/development/.env; \
	fi
	docker compose -f docker/development/docker-compose.yaml up -d

.PHONY: down-dev
down-dev:
	docker compose -f docker/development/docker-compose.yaml down
