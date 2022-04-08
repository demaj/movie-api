from django.db import models

CURRENCIES = (
    ("USD", "United States Dollar"),
    ("GBP", "Great Britain Pound"),
    ("EUR", "EURO"),
    ("NZD", "New Zealand Dollar"),
    ("AUD", "Australian Dollar"),
)


class AbstractBaseField(models.CharField):
    class Meta:
        abstract = True

    def get_internal_type(self):
        return "CharField"


class LanguageField(AbstractBaseField):
    def __init__(self, *args, **kwargs):
        from core.utils.languages import LANGUAGES

        kwargs.setdefault("max_length", 2)
        kwargs.setdefault("choices", LANGUAGES)

        super(LanguageField, self).__init__(*args, **kwargs)


class CountryField(AbstractBaseField):
    def __init__(self, *args, **kwargs):
        from core.utils.countries import COUNTRIES

        kwargs.setdefault("max_length", 2)
        kwargs.setdefault("choices", COUNTRIES)

        super(CountryField, self).__init__(*args, **kwargs)


class CurrencyField(AbstractBaseField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("max_length", 3)
        kwargs.setdefault("choices", CURRENCIES)

        super(CurrencyField, self).__init__(*args, **kwargs)
