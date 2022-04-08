import datetime


def current_year():
    return datetime.date.today().year


def year_choices():
    return [(r, r) for r in range(1984, current_year() + 1)]
