NAME		= notaire-fr-scrapper
RUNNING		= running-notaire-fr-scrapper

# Directory
OUTPUT		= ./output

# Docker ID
CONTAINER	= $(shell docker ps --quiet)
IMAGE		= $(shell docker images --quiet)

all:
	@mkdir -p ${OUTPUT}
	docker build -t ${NAME} .
	docker run -it -v ${OUTPUT}:/usr/bin/app/output --rm --name ${RUNNING} ${NAME}

clean:
ifneq ($(strip ${CONTAINER}),)
	docker stop ${RUNNING}
	docker container rm -f ${CONTAINER}
endif

fclean: clean
ifneq ($(strip ${IMAGE}),)
	docker image rm -f ${IMAGE}
endif

re:
	make fclean
	make all

.PHONY: all clean fclean re
