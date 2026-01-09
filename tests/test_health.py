from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health() -> None:
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_gorilla_default_routine() -> None:
    response = client.get("/api/gorilla")
    assert response.status_code == 200
    data = response.json()
    assert data["style_requested"] == "hype"
    assert data["style_applied"] == "hype"
    assert data["repeats_requested"] == 2
    assert data["applied_repeats"] == 2
    assert data["reverse_applied"] is False
    assert data["total_frames"] == 6  # 2 repeats * 3 frames
    assert data["unique_frames"] == 3
    assert data["description"].startswith("Hype routine x2")


def test_gorilla_chill_reverse_and_cap() -> None:
    response = client.get("/api/gorilla?style=chill&repeats=9&reverse=true")
    assert response.status_code == 200
    data = response.json()
    assert data["style_requested"] == "chill"
    assert data["style_applied"] == "chill"
    assert data["repeats_requested"] == 9
    assert data["applied_repeats"] == 5  # capped
    assert data["reverse_applied"] is True
    assert data["total_frames"] == 15  # 5 repeats * 3 frames
    assert data["frames"][0].strip()  # ensure frames exist even when reversed
    assert data["description"].endswith("reversed")
