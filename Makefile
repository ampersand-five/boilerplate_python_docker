IMAGE_NAME = boilerplate_python_docker
VERSION = latest

build ::
	docker build -t $(IMAGE_NAME):$(VERSION) .

build-no-cache ::
	docker build --no-cache -t $(IMAGE_NAME):$(VERSION) .

run ::
	docker run --rm \
	# If we have local machine files we want to copy into the docker container, then this is how
	--mount type=bind,source=$(input_file),target=/src/input_file.txt \
	--mount type=bind,source=$(other_file),target=/src/other_file.txt \
	$(IMAGE_NAME)

debug ::
	make build
	docker run --rm \
	--mount type=bind,source=$(input_file),target=/src/input_file.txt \
	--mount type=bind,source=$(other_file),target=/src/other_file.txt \
	$(IMAGE_NAME) \
	# -d is just a -debug flag in the code here, it doesn't have to exist
	-d

# This will run the docker container and return a usable shell to it
get-shell ::
	docker run -it \
	--mount type=bind,source=$(input_file),target=/src/input_file.txt \
	--mount type=bind,source=$(other_file),target=/src/other_file.txt \
	$(IMAGE_NAME) \
	sh