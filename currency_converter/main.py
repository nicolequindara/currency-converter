from decimal import Decimal
from typing import List
from fastapi import FastAPI, HTTPException

from currency_converter.domain import ConversionRate
from currency_converter.dto import ConvertCurrencyPayload
from currency_converter.services import CurrencyService
from currency_converter.repositories import ConversionRateRepository


app = FastAPI()
service = CurrencyService(ConversionRateRepository())


@app.get("/conversion_rates/")
def get_all() -> List[ConversionRate]:
    """
    List all supported conversion rates

    Returns:
        List of conversion rates (country code, currency, conversion rate)

    """
    return service.get_all()

@app.get("/conversion_rates/{country_code}")
def get(country_code: str) -> ConversionRate:
    """
    Get conversion rate (country code, currency, conversion rate) for country code if supported

    Returns:
        200 ConversionRate
        400 if country code not supported
    """
    try:
        return service.get(country_code)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))

@app.post("/convert")
def convert_currency(payload: ConvertCurrencyPayload) -> Decimal:
    """
    Convert amount from a currency to another currency

    Returns:
        200 converted amount
        400 if country code(s) not supported
    """
    try:
        converted_amount = service.convert(payload.from_country_code, payload.to_country_code, payload.amount)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))
    
    return converted_amount

