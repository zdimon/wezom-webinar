FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /docker-img
WORKDIR /docker-img
COPY requirements.txt /docker-img/
RUN pip install -r requirements.txt
COPY . /docker-img/