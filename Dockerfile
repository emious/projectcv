FROM python:3.8-slim
MAINTAINER "Emran"
ENV PYTHONUNBUFFERED 1
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . /projectcv
WORKDIR /projectcv
ENV PYTHONPATH "${PYTHONPATH}:/projectcv/"
