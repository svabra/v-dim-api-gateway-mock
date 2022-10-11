#FROM python:3.9.13
FROM alpine:edge

WORKDIR /

# dont write pyc files
ENV PYTHONDONTWRITEBYTECODE 1
# dont buffer to stdout/stderr
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

# dependencies
RUN apk add python3
RUN apk add py3-pip
RUN apk update
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --no-cache-dir --upgrade -r /requirements.txt
RUN python3 -m pip install fastapi
RUN python3 -m pip install hypercorn

COPY ./ /

WORKDIR /
EXPOSE 8080
CMD ["hypercorn", "main:app", "--bind", "0.0.0.0:8080"]