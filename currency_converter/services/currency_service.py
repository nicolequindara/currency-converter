from decimal import Decimal
from typing import List, Optional
from currency_converter.domain import ConversionRate
from currency_converter.repositories import ConversionRateRepository


class CurrencyService:
    def __init__(
        self, conversion_rate_repository: Optional[ConversionRateRepository] = None
    ):
        self.conversion_rate_repository = (
            conversion_rate_repository or ConversionRateRepository()
        )

    def get_all(self) -> List[ConversionRate]:
        """
        Get all supported conversion rates

        Returns:
            List of ConversionRate
        """
        return self.conversion_rate_repository.get_all().values()

    def get(self, country_code: str) -> ConversionRate:
        """
        Get conversion rate for country code

        Args:
            country_code (str)

        Raises:
            ValueError if country code not supported

        Returns:
            ConversionRate for country code
        """
        rate = self.conversion_rate_repository.get_all().get(country_code.upper())
        if not rate:
            raise ValueError(f"Unsupported country code {country_code.upper()}")

        return rate

    def convert(
        self, from_country_code: str, to_country_code: str, amount: Decimal
    ) -> Decimal:
        """
        Convert amount from a currency to another currency

        Args:
            from_country_code (str)
            to_country_code (str)
            amount (Decimal)

        Raises:
            ValueError if either country code is not supported

        Returns:
            Decimal: converted amount
        """
        try:
            from_rate = self.get(from_country_code).conversion_rate
        except AttributeError as exc:
            raise ValueError(
                f"Unsupported country code {from_country_code.upper()}"
            ) from exc

        try:
            to_rate = self.get(to_country_code).conversion_rate
        except AttributeError as exc:
            raise ValueError(
                f"Unsupported country code {to_country_code.upper()}"
            ) from exc

        return round(amount * (to_rate / from_rate), 2)
