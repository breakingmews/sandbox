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

## Defaults
- model: `tiny` (lowest quality)
- input: `./data/audio`
- output: `./data/transcription`

## Development 
Transcribe with default input and output:

```sh
pipenv run transcribe
```

Transcribe specifying input and output directories:

```sh
pipenv run transcribe --model=base /input /output
```

## Run in Docker
```sh
docker build -t transcriber .
```

Run with default settings
```sh
docker run -d -t --rm \
  --name transcriber \
  -p 8000:8000 \
  --mount type=bind,source="$(pwd)"/logs,target=/app/logs \
  --mount type=bind,source="$(pwd)"/data,target=/app/data \
  transcriber 
```

or specify model size, input and output directories

```sh
docker run -d -t --rm \
  --name transcriber \
  -p 8000:8000 \
  --mount type=bind,source="$(pwd)"/logs,target=/app/logs \
  --mount type=bind,source="$(pwd)"/data,target=/app/data \
  transcriber pipenv run transcribe --model=large /input /output
```


## Run with Docker Compose
Build and start the services:

```sh
docker compose up -d
```

or
```sh
docker compose run -d app pipenv run transcribe --model=large /input /output
```


## Logging
Logs are stored in the /app/logs directory inside the container. You can mount a host directory to this path to persist logs.

```sh
tail -f logs/log
```