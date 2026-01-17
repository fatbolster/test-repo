from fastapi import APIRouter, Query
from fastapi.responses import HTMLResponse

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


@router.get("/counter", response_class=HTMLResponse)
async def counter_page() -> str:
    """Display a simple counter page"""
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Counter Page</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                margin: 0;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            }
            .container {
                background: white;
                padding: 40px;
                border-radius: 15px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.3);
                text-align: center;
            }
            h1 {
                color: #333;
                margin-bottom: 30px;
            }
            .counter-display {
                font-size: 72px;
                font-weight: bold;
                color: #667eea;
                margin: 30px 0;
                min-width: 150px;
            }
            .button-group {
                display: flex;
                gap: 15px;
                justify-content: center;
                margin-top: 20px;
            }
            button {
                font-size: 24px;
                padding: 15px 30px;
                border: none;
                border-radius: 8px;
                cursor: pointer;
                transition: all 0.3s ease;
                font-weight: bold;
            }
            .btn-decrement {
                background-color: #ff6b6b;
                color: white;
            }
            .btn-decrement:hover {
                background-color: #ee5a52;
                transform: scale(1.05);
            }
            .btn-increment {
                background-color: #51cf66;
                color: white;
            }
            .btn-increment:hover {
                background-color: #40c057;
                transform: scale(1.05);
            }
            .btn-reset {
                background-color: #868e96;
                color: white;
                font-size: 18px;
                padding: 10px 25px;
            }
            .btn-reset:hover {
                background-color: #495057;
                transform: scale(1.05);
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Counter App</h1>
            <div class="counter-display" id="counter">0</div>
            <div class="button-group">
                <button class="btn-decrement" onclick="decrement()">-</button>
                <button class="btn-increment" onclick="increment()">+</button>
            </div>
            <div class="button-group" style="margin-top: 15px;">
                <button class="btn-reset" onclick="reset()">Reset</button>
            </div>
        </div>
        
        <script>
            let counter = 0;
            const counterDisplay = document.getElementById('counter');
            
            function updateDisplay() {
                counterDisplay.textContent = counter;
            }
            
            function increment() {
                counter++;
                updateDisplay();
            }
            
            function decrement() {
                counter--;
                updateDisplay();
            }
            
            function reset() {
                counter = 0;
                updateDisplay();
            }
        </script>
    </body>
    </html>
    """
    return html_content
