from typing import Union

import uvicorn
from api import base_data
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel


app = FastAPI()
if not base_data.get("success"):
    raise Exception("Unable to retrieve information from ExchangeAPI")


class UserInput(BaseModel):
    """Declaring data model as a class"""
    amount: Union[float, int] = 1
    from_currency: str
    to_currency: str


@app.get("/")
def read_root():
    """This function redirects root page to docs."""
    return RedirectResponse("/docs")


@app.post("/currency-convert/")
def read_item(item: UserInput):
    rates = base_data.get("rates")
    if item.to_currency not in rates or item.from_currency not in rates:
        raise HTTPException(400, detail=f"Invalid currency")
    converted = rates.get(item.to_currency) / rates.get(item.from_currency)
    rounded = float(round(converted, 4))
    return item.amount * rounded


if __name__ == '__main__':
    uvicorn.run(app=app)
