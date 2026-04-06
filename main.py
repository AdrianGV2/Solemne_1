from fastapi import FastAPI
from datetime import datetime

app = FastAPI()


@app.get("/time")
async def get_time():
    # Formato: Año-Mes-Día Hora:Minuto:Segundo
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"time": current_time}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
