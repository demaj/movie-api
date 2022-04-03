import datetime

# Months
JANUARY = 1
FEBRUARY = 2
MARCH = 3
APRIL = 4
MAY = 5
JUNE = 6
JULY = 7
AUGUST = 8
SEPTEMBER = 9
OCTOBER = 10
NOVEMBER = 11
DECEMBER = 12

# Months list
MONTH_CHOICES = [
    (JANUARY, "January"),
    (FEBRUARY, "February"),
    (MARCH, "March"),
    (APRIL, "April"),
    (MAY, "May"),
    (JUNE, "June"),
    (JULY, "July"),
    (AUGUST, "August"),
    (SEPTEMBER, "September"),
    (OCTOBER, "October"),
    (NOVEMBER, "November"),
    (DECEMBER, "December"),
]


def current_year():
    return datetime.date.today().year


def year_choices():
    return [(r, r) for r in range(1984, current_year() + 1)]
