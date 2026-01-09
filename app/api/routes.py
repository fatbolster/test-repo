from fastapi import APIRouter, Query

from app.services.gorilla import render_dance

router = APIRouter()


@router.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}


@router.get("/gorilla")
async def gorilla_dance(
    sets: int = Query(1, ge=1, le=3),
    hype: bool = Query(True),
    closing: bool = Query(True),
) -> dict[str, object]:
    frames = render_dance(sets, hype=hype, closing=closing)
    applied_sets = max(1, min(sets, 3))
    return {
        "frames": frames,
        "sets_requested": sets,
        "sets_applied": applied_sets,
        "hype_added": hype,
        "closing_added": closing,
        "total_frames": len(frames),
    }
