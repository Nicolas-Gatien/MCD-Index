# syntax=docker/dockerfile:1
FROM alpine:3.12

RUN apt-get update 
RUN apt-get install -y python3 python3-pip
RUN apt-get clean

RUN pip install -r requirements.txt

COPY . /

EXPOSE 7878

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "7878"]