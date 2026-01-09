GORILLA_FRAMES = [
    """
  ,~~.   
 (•_• )  
 /(  )\\ 
  |  | \\ 
  /  \\   
""".strip("\n"),
    """
  ,~~.   
 ( •_•)  
 /(  )\\ 
 /  |  | 
   /  \\  
""".strip("\n"),
    """
  ,~~.   
 (•_• )  
 /(  )\\ 
 |  |  / 
  \\  /   
""".strip("\n"),
    """
  ,~~.   
 (•‿• )  
 /(  )\\ 
 /  |  \\ 
   /  \\  
""".strip("\n"),
]


def render_dance(sets: int, hype: bool = True, closing: bool = True) -> list[str]:
    max_sets = 3
    applied_sets = max(1, min(sets, max_sets))
    frames: list[str] = []
    if hype:
        frames.append("DJ yells: Make some noise for the gorilla!")
    for _ in range(applied_sets):
        frames.extend(GORILLA_FRAMES)
    if closing:
        frames.append("Confetti cannons fire as the gorilla moonwalks off.")
    return frames
