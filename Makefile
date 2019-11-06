DOCKER = /usr/bin/docker
BUILD_ARG = $(if $(filter  $(NOCACHE), 1),--no-cache)
BUILD_ARG_BASE = $(if $(filter  $(NOCACHEBASE), 1),--no-cache)
DEFAULT_ENVIRONMENT = development
ENVIRONMENT_TO_BUILD := $(if $(ENVIRONMENT),$(ENVIRONMENT),$(DEFAULT_ENVIRONMENT))
DOCKERFILE_PATH = $(if $(filter  $(ENVIRONMENT_TO_BUILD), production),images/python/production/Dockerfile,images/python/development/Dockerfile)

development: development_image
clean: develop_volumes_down
develop_stop: develop_shutdown develop_volumes_down
develop_up: develop_start

develop_start:
	docker-compose up -d
develop_shutdown:
	docker-compose stop
develop_volumes_down:
	docker-compose down --volumes
development_image:
	$(DOCKER) build $(BUILD_ARG_BASE) -f images/development/python/base/Dockerfile -t development-reqliable-queue-worker-base .
	$(DOCKER) build $(BUILD_ARG) -f images/development/python/base/Dockerfile -t development-reqliable-queue-worker .
