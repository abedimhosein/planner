import jdatetime
from .texts import (
    to_persian_digits,
    to_english_digits,
)


def to_jalali_date(date) -> str:
    date = jdatetime.date.fromgregorian(
        year=date.year,
        month=date.month,
        day=date.day).strftime('%Y-%m-%d')

    return to_persian_digits(date)


def to_jalali_date_time(date) -> str:
    value = jdatetime.datetime.fromgregorian(date=date)
    date = to_persian_digits(value.date().strftime('%Y-%m-%d'))
    time = value.time().strftime('%H:%M')
    return f"در تاریخ {date} و در ساعت {time}"


def to_gregorian_date(date: str, delimiter: str = ' ') -> jdatetime.date:
    date = to_english_digits(date)
    date = [int(i) for i in date.split(delimiter)]
    return jdatetime.date(date[0], date[1], date[2]).togregorian()
