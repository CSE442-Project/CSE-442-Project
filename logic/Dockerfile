FROM python:3.7
MAINTAINER Vito Galvez "vitogalv@buffalo.edu"
ENV APT_KEY_DONT_WARN_ON_DANGEROUS_USAGE=DontWarn
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

RUN apt-get update
RUN apt-get install netcat-traditional
RUN apt-get install netcat

ENTRYPOINT ["./entrypoint.sh"]
