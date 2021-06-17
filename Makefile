IMAGE_NAME = boilerplate_python_docker
VERSION = latest

build ::
	docker build -t $(IMAGE_NAME):$(VERSION) .

run ::
	docker run --rm $(IMAGE_NAME) input.txt output.txt

debug ::
	make build
	docker run --rm $(IMAGE_NAME) -d input.txt output.txt