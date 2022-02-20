IMAGE ?= pi-screen-remote:latest

docker-build:
	poetry export --format=requirements.txt --without-hashes --output=requirements.txt
	docker build -t ${IMAGE} .

docker-run:
	docker run --device /dev/mem --cap-add sys_rawio -p 8000:8000 ${IMAGE}

run:
	python3 server.py

