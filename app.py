from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

class ConvertRequest(BaseModel):
    from_currency: str
    to_currency: str
    amount: float

exchange_rates = {
    "USD":1.0,
    "EUR":0.92,
    "INR":83.0,
    "JPY":151.0,
    "GBP":0.78,
    "AUD":1.52
}

@app.get("/api/currencies")
def get_currencies():
    return {"currencies": list(exchange_rates.keys())}

@app.post("/api/convert")
def convert_currency(req: ConvertRequest):
    if req.from_currency not in exchange_rates or req.to_currency not in exchange_rates:
        return {"error":"Invalid currency"}

    usd_value = req.amount / exchange_rates[req.from_currency]
    converted_amount = usd_value * exchange_rates[req.to_currency]

    return {
        "from_currency": req.from_currency,
        "to_currency": req.to_currency,
        "amount": req.amount,
        "converted_amount": round(converted_amount, 4)
    }

@app.get("/")
def root():
    return FileResponse("static/index.html")

app.mount("/static", StaticFiles(directory="static"), name="static")

