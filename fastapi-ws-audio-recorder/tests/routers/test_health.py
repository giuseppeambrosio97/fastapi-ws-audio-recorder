from fastapi import status
from fastapi.testclient import TestClient

from fastapi_ws_audio_recorder.app import app

client = TestClient(app)

def test_router_health():
    with TestClient(app) as client:
        response = client.get("/health")
        assert response.status_code == status.HTTP_200_OK
