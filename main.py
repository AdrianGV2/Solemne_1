import os
from fastapi import FastAPI
from datetime import datetime, timedelta, timezone

app = FastAPI()

UTC_OFFSET = int(os.getenv("TIMEZONE_OFFSET", -4))

@app.get("/time")
async def get_time():
    tz = timezone(timedelta(hours=UTC_OFFSET))
    current_time = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
    
    return {
        "time": current_time,
        "timezone_offset": f"UTC{UTC_OFFSET:+d}",
        "location_hint": "Chile (Default)" if UTC_OFFSET == -4 else "Custom"
    }
