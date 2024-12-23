FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    && apt install -y ffmpeg \
    && apt-get install -y curl \
    && pip3 install pipenv \
    && rm -rf /var/lib/apt/lists/*

COPY ./data/ /app/data

RUN mkdir -p /app/logs

COPY ./Pipfile ./Pipfile.lock /app/

RUN pipenv install

COPY ./app /app/app

CMD ["pipenv", "run", "transcribe"]