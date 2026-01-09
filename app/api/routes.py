from fastapi import APIRouter, Query

from app.services.gorilla import generate_routine

router = APIRouter()


@router.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}


@router.get("/gorilla")
async def gorilla_dance(
    style: str = Query("hype", description="One of: hype, chill"),
    repeats: int = Query(2, ge=1, le=5, description="How many times to loop frames"),
    reverse: bool = Query(False),
) -> dict[str, object]:
    routine = generate_routine(style, repeats, reverse=reverse)
    routine["style_requested"] = style
    routine["repeats_requested"] = repeats
    return routine
