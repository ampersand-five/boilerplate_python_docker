FROM python:3.9

# Install pipx
RUN pip install pipx

# Install poetry
RUN pipx install poetry

# Copy pyproject and lock file so that it doesn't have to lock again
COPY src/poetry.lock src/pyproject.toml /src/ 

# Set working directory inside docker container
WORKDIR /src

# Install dependencies in container with Poetry 
# - tell poetry to not create a virtual env because it's already in a docker continer
# - no interaction or output becuase it should run on it's own
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Copy source code into docker container -- does this re-copy and make two versions of the poetry.lock files?
COPY src/ /src/

# Tell Docker what to run when started. Any cmd line arguments passed will be appended by docker to
#   this command`
ENTRYPOINT ["python", "app.py"]