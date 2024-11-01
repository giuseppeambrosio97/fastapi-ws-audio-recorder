import io
import logging
from typing import List

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from pydub import AudioSegment
from uuid import uuid4

from fastapi_ws_audio_recorder import RECORDINGS_LOCATION

logger = logging.getLogger(__name__)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ConnectionManager:
    """Manages WebSocket connections."""

    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_message(self, message: bytes, websocket: WebSocket):
        await websocket.send_bytes(message)

    async def broadcast(self, message: bytes):
        for connection in self.active_connections:
            await connection.send_bytes(message)


manager = ConnectionManager()


@app.websocket("/ws/audio")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)

    audio_file_path = (
        RECORDINGS_LOCATION / f"{uuid4()}_received_audio.wav"
    )
    audio_data_list = []  # List to hold chunks of audio data

    try:
        while True:
            audio_data = await websocket.receive_bytes()
            audio_data_list.append(audio_data)
            logger.info("Received audio data chunk.")

    except WebSocketDisconnect:
        # When disconnected, save the audio data
        manager.disconnect(websocket)
        logger.info("Connection closed. Processing audio data.")

        # Combine received audio chunks
        full_audio_data = b"".join(audio_data_list)

        # Convert raw audio data to WAV format using pydub
        # Assuming the audio is sent in a format that pydub can read (like WebM or Opus)
        audio_segment = AudioSegment.from_file(
            io.BytesIO(full_audio_data), format="webm"
        )  # Adjust format as needed
        audio_segment.export(audio_file_path, format="wav")  # Save as WAV file
        logger.info(f"Audio saved to {audio_file_path}")

    except Exception as e:
        logger.error(f"An error occurred: {e}")
