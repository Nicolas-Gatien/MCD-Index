# syntax=docker/dockerfile:1
FROM alpine:3.20.3

RUN apk add --update py-pip

COPY . /

RUN pip install -r requirements.txt --break-system-packages


EXPOSE 7878

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "7878"]