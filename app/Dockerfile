FROM alpine:3.18

RUN apk add  --no-cache --update python3 py3-pip \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache mariadb-dev

WORKDIR /app

COPY . /app

RUN pip3 --no-cache-dir install -r requerimientos.txt

CMD ["python3", "Universidad.py"]