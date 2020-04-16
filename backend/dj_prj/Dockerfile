FROM python:3
ENV PYTHONUNBUFFERED 1
#RUN mkdir /app

ADD requirements.txt requirements.txt
# COPY requirements.txt /app
RUN pip install -r requirements.txt
WORKDIR /backend/dj_prj
# COPY . /app/

