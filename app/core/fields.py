from django.db import models

COUNTRIES = (
    ("AU", "Australia"),
    ("ZA", "South Africa"),
    ("GH", "Ghana"),
    ("NZ", "New Zealand"),
)

CURRENCIES = (
    ("USD", "United States Dollar"),
    ("GBP", "Great Britain Pound"),
    ("EUR", "EURO"),
    ("NZD", "New Zealand Dollar"),
    ("AUD", "Australian Dollar"),
)


class CountryField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("max_length", 2)
        kwargs.setdefault("choices", COUNTRIES)

        super(CountryField, self).__init__(*args, **kwargs)

    def get_internal_type(self):
        return "CharField"


class CurrencyField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("max_length", 3)
        kwargs.setdefault("choices", CURRENCIES)

        super(CurrencyField, self).__init__(*args, **kwargs)

    def get_internal_type(self):
        return "CharField"
