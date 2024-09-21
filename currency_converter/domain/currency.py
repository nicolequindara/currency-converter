from pydantic import BaseModel
from decimal import Decimal

class ConversionRate(BaseModel):
    """
    A currency conversion rate

    Args:
        BaseModel (_type_): _description_
    """
    country_code: str
    currency: str
    conversion_rate: Decimal