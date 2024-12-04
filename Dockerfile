# syntax=docker/dockerfile:1
FROM alpine:3.20.3

RUN apk add --update py-pip

COPY . /

RUN pip install -r requirements.txt --break-system-packages

EXPOSE 3000

CMD ["gunicorn", "--bind", "0.0.0.0:3000", "--timeout", "180", "--log-level", "info", "--access-logfile", "-", " --error-logfile", "-", "wsgi:app"]