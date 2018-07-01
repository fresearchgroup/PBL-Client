FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir /PBL-client
WORKDIR /PBL-client
COPY  . /PBL-client
RUN pip install -r requirements.txt