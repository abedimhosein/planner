# This docker file is used for local development via docker-compose
# Creating image based on official python3 image
FROM python:3.11.7-alpine3.19

# PYTHONDONTWRITEBYTECODE is an environment variable specific to Python.
# When set to 1, it prevents Python from writing bytecode (.pyc files) to disk.
# Bytecode files are compiled Python files that are generated to improve the startup time of Python scripts.
# Setting this variable to 1 is often recommended in Docker images to avoid unnecessary file writes and to make the image smaller.
# It's particularly useful in scenarios where the generated bytecode is not needed.
ENV PYTHONDONTWRITEBYTECODE 1


# PYTHONUNBUFFERED is another environment variable specific to Python.
# When set to 1, it instructs Python to run in unbuffered mode.
# In unbuffered mode, Python doesn't buffer the output, and it directly writes to the stdout and stderr streams.
# This can be useful in Docker containers to ensure that the logs and output from Python scripts are immediately visible and not delayed due to buffering.
# Running Python in unbuffered mode can be beneficial for containerized applications,
# especially when dealing with logging and debugging, as it provides real-time output.
ENV PYTHONUNBUFFERED 1


# Adding WORKDIR as ENV Variable
ENV PROJ_HOME=/home/app/planner
ENV PROJ_VENV="$PROJ_HOME/venv"
RUN mkdir -p $PROJ_HOME
WORKDIR $PROJ_HOME

# Updating apline-linux repositories and upgrading the existing packages.
RUN apk update && apk upgrade

# Installing some basic and utility packages.
RUN apk add nano 

# Creating virtual environments (venv), activate it and upgrading pip.
RUN python -m venv $PROJ_VENV
RUN source "$PROJ_VENV/bin/activate"
RUN python -m pip install --upgrade pip

# Installing dependencies
COPY ./requirements.txt $PROJ_HOME
RUN pip install -r requirements.txt

# Copy all the project files.
COPY . $PROJ_HOME