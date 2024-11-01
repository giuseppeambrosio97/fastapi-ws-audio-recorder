# fastapi-ws-audio-recorder

This repository demonstrates a simple audio recording system using FastAPI and WebSockets. Audio data is recorded in a client-side HTML page, streamed to the server through a WebSocket connection, and then saved as a WAV file.

## Features

- Record audio on the client side and send it to the server in real-time using WebSockets.
- Server receives audio in chunks, compiles them into a single file, and saves it in WAV format.
- Easy setup with a FastAPI backend and a simple HTML frontend.
- Optionally, use a Visual Studio Code dev container to run without system dependencies.

## Prerequisites

- Python 3.11
- FFmpeg required for **pydub** to handle audio processing
- Live Server Extension in your browser or an equivalent to serve the html file

## Getting Started

1. Start FastAPI Server

```bash
poetry env use <path-path-to-a-local-python-version>
poetry install
source .venv/bin/activate
python -m fastapi_ws_audio_recorder
```

The WebSocket endpoint is available at ws://localhost:8000/ws/audio.

2. Start the Client

Open client/index.html with a live server (or use an HTTP server like the Live Server extension in VSCode).

3. Record and Send Audio with the Client

## Running in VSCode Dev Container

To avoid installing system dependencies like FFmpeg, you can run the project inside a VSCode dev container:

1. Open the project in VSCode
2. Open the command palette and search for ">Dev Containers: Reopen in Container"
