# Processor Microservice
from fastapi import FastAPI
import requests

app = FastAPI()
SERVICE_1_URL = "http://127.0.0.1:8000/generate"

@app.get("/process")
def process_data():
    response = requests.get(SERVICE_1_URL)
    return {"message": f"Processed: {response.json()['message']}"}
