# Aggregator Microservice
from fastapi import FastAPI
import requests

app = FastAPI()
SERVICE_2_URL = "http://127.0.0.1:8001/process"

@app.get("/aggregate")
def aggregate_data():
    response = requests.get(SERVICE_2_URL)
    return {"message": f"Aggregated: {response.json()['message']}"}
