from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)

chicken = "what"

def test_health() -> None:
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_gorilla_default_sets() -> None:
    response = client.get("/api/gorilla")
    assert response.status_code == 200
    data = response.json()
    assert data["sets_requested"] == 1
    assert data["sets_applied"] == 1
    assert data["closing_added"] is True
    assert data["total_frames"] == 6  # hype + 4 frames + closing
    assert data["frames"][0].startswith("DJ yells")
    assert data["frames"][-1].startswith("Confetti")


def test_gorilla_sets_cap_and_toggle_flair() -> None:
    response = client.get("/api/gorilla?sets=9&hype=false&closing=false")
    assert response.status_code == 200
    data = response.json()
    assert data["sets_requested"] == 9
    assert data["sets_applied"] == 3
    assert data["hype_added"] is False
    assert data["closing_added"] is False
    assert data["total_frames"] == 12  # 3 sets * 4 frames
