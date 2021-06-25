# Boilerplate code to copy and get a repo started from
Includes working build of python 3.9 in a Docker image and basic extras 
like:
- Global logging setup in a useful format
- Outline for reading in command line arguments already setup
- Poetry
- Dockerfile that will do a basic build and run
- Makefile for quick commands

### General Flow
- Add description of general flow

## Design Decisions
- Add any design decisions

##  Assumptions
- Add any assumptions made

## Running The Code
### Supported Flags
- h - Help
- d - Output debug logs
- s - Shell mode for running the app.py file directly, not using Docker

### Build Docker container locally
Make command to build:

`make build`

- Can also force a rebuild and not use cached layers with:

`make build-no-cache`

### Run Docker container locally
Make command that will run the code:

`make run input_file=absolute/path other_file=absolute/path`


### Run code directly outside of Docker container
To run the code, `cd` to the location where this repo is locally. Then 
from the top folder `cd` to the `src` folder. Since we're using Poetry to
manage the environment we will need to run an install first time:

`poetry install`

See the Poetry section if Poetry is not installed.

The program must be called in poetry's managed environment. You can call
the app.py file directly. It will need the -s, shell, option to run this
way.

Example:

`poetry run python app.py -s absolute/path/to/input absolute/path/to/other_file`

### Run in debug mode

`make debug input_file=absolute/path other_file=absolute/path`
- Will show debug logs

### Run Docker to get a shell into container
`make shell input_file=absolute/path other_file=absolute/path`

### Poetry
[Poetry](https://python-poetry.org/) is a python package and environment
manager. Their installation docs are here: [https://python-poetry.org/docs/#installation](https://python-poetry.org/docs/#installation)

The TL;DR for installing is one of these three options:
- `curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -`
- `pipx install poetry`
- `pip install --user poetry` (not recommended as per their docs)



## TODO
- Add pre-commit
- Add black -- add this when done: [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
- Add add pytest structure
- Lucid chart and link