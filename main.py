from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, List
from fastapi import HTTPException

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
async def get_currencies(min_rate: float = 0):
    filtered_currencies = []
    
    for currency in fake_currency_db:
        if currency['rate'] >= min_rate:
            filtered_currencies.append(currency)
    return filtered_currencies

#GET /api/vi/currencies/통화 요청시
@app.get("/api/v1/currencies/{code}", response_model=Currency)
async def get_currency_by_code(code: str):
    target_code = code.upper()
    
    for currency in fake_currency_db:
        if currency["code"] == target_code:
            return currency
        
    raise HTTPException(status_code=404, detail=f"Currency code '{target_code}' not found")
    