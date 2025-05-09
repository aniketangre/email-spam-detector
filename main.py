from fastapi import FastAPI
from predict import predict

app = FastAPI()

@app.get('/detection/{message}')
async def prediction(message: str) -> str:
    return predict(message)