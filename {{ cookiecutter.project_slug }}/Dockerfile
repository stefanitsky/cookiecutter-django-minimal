FROM python:3.8
ENV PYTHONUNBUFFERED 1

# Allows docker to cache installed dependencies between builds
COPY ./requirements /requirements
RUN pip install -r /requirements/base.txt

# Adds our application code to the image
COPY . code
WORKDIR code

EXPOSE 8000
