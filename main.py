from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, List


class Currency(BaseModel):
    code : str
    name : str
    rate : float

app = FastAPI()

#임시 데이터
fake_currency_db = [
    {"code": "USD", "name": "미국 달러", "rate": 1350.50},
    {"code": "EUR", "name": "유로", "rate": 1460.20},
    {"code": "JPY", "name": "일본 엔", "rate": 9.15}
]

#GET / 요청시
@app.get("/")
async def read_root():
    return{"message" : "Welcome FastAPI"}


#GET /api/v1/currencies 요청시
@app.get("/api/v1/currencies", response_model=List[Currency])
async def get_currencies():
    return fake_currency_db