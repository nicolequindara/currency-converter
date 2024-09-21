import csv
from decimal import Decimal
from currency_converter.domain import ConversionRate

FILENAME = "currency_converter/repositories/Conversion Rates.csv"

class ConversionRateRepository:
    def __init__(self):
        self.rate_map = None

    def get_all(self, force_refresh_cache: bool = False) -> dict[str, ConversionRate]:
        """
        Retrieve currency information
        Country Code, Currency, Conversion Rate from USD

        Args:
            force_refresh_cache (str): if true, read rates from CSV; otherwise use cached value

        Returns:
            dictionary of country code to ConversionRate
        """
        if force_refresh_cache or not self.rate_map:
            print("Retrieving conversion rate information from CSV")
            rate_map = {} # singleton map of country code to ConversionRate
            with open(FILENAME, mode="r") as csvfile:
                rows = csv.reader(csvfile, delimiter=",")
                next(rows) # skip header
                for row in rows:
                    rate_map[row[0]] = ConversionRate(
                        country_code=row[0],
                        currency=row[1],
                        conversion_rate=Decimal(row[2]),
                    )
            self.rate_map = rate_map
        return self.rate_map


    def get(self, country_code: str) -> ConversionRate:
        """Get ConversionRate for a given country code if it exists

        Args:
            country_code

        Returns:
            ConversionRate
        """
        return self.get_all().get(country_code.upper())
