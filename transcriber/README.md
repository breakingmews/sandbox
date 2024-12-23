# Prerequisites
- Ffmpeg
- Pipenv

```sh
sudo apt update && sudo apt install ffmpeg
pip install pipenv
```

# Usage

## Easiest ☕ 

1. Copy all audio files to `transcriber/data/audio/`. Recursive traversing of directories supported.
2. Run with [docker compose](#run-with-docker-compose)

## Default directories
- input: `./data/audio`
- output: `./data/transcription`

## Development 
Transcribe with default input and output:

```sh
pipenv run transcribe
```

Transcribe specifying input and output directories:

```sh
pipenv run transcribe /input /output
```

## Run in Docker
```sh
docker build -t transcriber .
```

Run with default directories
```sh
docker run -t --rm \
  --name transcriber \
  -p 8000:8000 \
  --mount type=bind,source="$(pwd)"/logs,target=/app/logs \
  --mount type=bind,source="$(pwd)"/data,target=/app/data \
  transcriber 
```

or specify input and output directories

```sh
docker run -t --rm \
  --name transcriber \
  -p 8000:8000 \
  --mount type=bind,source="$(pwd)"/logs,target=/app/logs \
  --mount type=bind,source="$(pwd)"/data,target=/app/data \
  transcriber pipenv run transcribe /input /output
```


## Run with Docker Compose
Build and start the services:

```sh
docker compose up
```

or
```sh
docker compose run app pipenv run transcribe /input /output
```


## Logging
Logs are stored in the /app/logs directory inside the container. You can mount a host directory to this path to persist logs.