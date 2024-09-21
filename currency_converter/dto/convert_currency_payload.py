from decimal import Decimal
from pydantic import BaseModel

class ConvertCurrency(BaseModel):
    """
    Request payload for POST /convert_currency endpoint
    """
    from_country_code: str
    to_country_code: str
    amount: Decimal

class ConvertCurrencyResponse(BaseModel):
    """
    Response payload for POST /convert_currency endpoint
    """
    amount: Decimal
    currency: str