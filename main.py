import os
from fastapi import FastAPI
from datetime import datetime, timedelta, timezone

app = FastAPI()

# Definimos el ajuste UTC mediante una variable de entorno o una constante por defecto (-4 para Chile) [1]
UTC_OFFSET = int(os.getenv("TIMEZONE_OFFSET", -4))

@app.get("/time")
async def get_time():
    # Creamos un objeto de zona horaria basado en el desplazamiento (offset)
    tz = timezone(timedelta(hours=UTC_OFFSET))
    
    # Obtenemos la hora actual con esa zona horaria específica
    current_time = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
    
    return {
        "time": current_time,
        "timezone_offset": f"UTC{UTC_OFFSET:+d}",
        "location_hint": "Chile (Default)" if UTC_OFFSET == -4 else "Custom"
    }
