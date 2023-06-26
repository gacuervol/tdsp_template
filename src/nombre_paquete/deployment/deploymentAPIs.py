from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import joblib

app = FastAPI()
model = joblib.load("model.joblib") # cargamos el modelo.

@app.get("/", response_class=HTMLResponse)
async def read_items():
    with open('mensaje.html', 'r') as file:
        html_content = file.read()
    return HTMLResponse(content=html_content, status_code=200)