FROM python:3.9-slim-buster
RUN sed -i '/jessie-updates/d' /etc/apt/sources.list
RUN apt-get update && \
    apt-get -y install gcc libmariadb-dev
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN apt install ibtk8.6 -y
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
