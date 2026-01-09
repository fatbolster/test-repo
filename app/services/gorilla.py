HYPE_FRAMES = [
    " (>'-')> ",
    " <('-'<) ",
    " ^('-')^ ",
]

CHILL_FRAMES = [
    " ( -_- ) ",
    " /|   |\\ ",
    "  / \\   ",
]

DEFAULT_STYLE = "hype"

FRAME_MAP = {
    "hype": HYPE_FRAMES,
    "chill": CHILL_FRAMES,
}


def generate_routine(style: str, repeats: int, reverse: bool = False) -> dict[str, object]:
    normalized_style = style.lower()
    frames_source = FRAME_MAP.get(normalized_style, FRAME_MAP[DEFAULT_STYLE])
    applied_style = normalized_style if normalized_style in FRAME_MAP else DEFAULT_STYLE
    applied_repeats = max(1, min(repeats, 5))

    frames: list[str] = []
    for _ in range(applied_repeats):
        frames.extend(frames_source)

    if reverse:
        frames = list(reversed(frames))

    return {
        "frames": frames,
        "style_applied": applied_style,
        "applied_repeats": applied_repeats,
        "reverse_applied": reverse,
        "unique_frames": len(set(frames_source)),
        "total_frames": len(frames),
    }
