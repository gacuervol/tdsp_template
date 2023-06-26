from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List
import joblib

class ApiInput(BaseModel):
    features_7: List[float]

class ApiOutput(BaseModel):
    heatflow: List[float]

app = FastAPI()
model = joblib.load("model.joblib") # cargamos el modelo.

@app.get("/", response_class=HTMLResponse)
async def read_items():
    with open('mensaje.html', 'r') as file:
        html_content = file.read()
    return HTMLResponse(content=html_content, status_code=200)
@app.post("/predict") # creamos api que permita requests de tipo post.
async def create_user(data: ApiInput) -> ApiOutput:
    predictions = model.predict([data.features_7]).flatten().tolist() # generamos la predicción
    preds = ApiOutput(heatflow=predictions) # estructuramos la salida del API.
    return preds # retornamos los resultados