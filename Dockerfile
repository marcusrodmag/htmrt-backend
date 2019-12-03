# Python image to use.
FROM python:3.7-alpine3.8

# Set the working directory to /app
WORKDIR /app

# copy the requirements file used for dependencies
COPY src/requirements.txt .

# Install any needed packages specified in requirements.txt
RUN apk add --virtual .build-deps gcc musl-dev && \
    pip install --trusted-host pypi.python.org -r requirements.txt

# Copy the rest of the working directory contents into the container at /app
COPY src/ .

ENTRYPOINT ["gunicorn", "setup:app", "--workers=2", "--limit-request-line", "0", "-b", "0.0.0.0:8080", "--access-logfile", "-"]
