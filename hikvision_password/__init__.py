#!/usr/bin/env python3

import re
from datetime import date
from typing import Union

SERIAL_RE = re.compile("^[0-9A-Z]+$")


def validate_serial_number(serial_number: str) -> bool:
    if isinstance(serial_number, str):
        return re.search(SERIAL_RE, serial_number) and len(serial_number) == 27
    else:
        return False


def validate_year(year: Union[str, int]) -> bool:
    if isinstance(year, str):
        return int(year) >= 1900 and int(year) <= date.today().year
    elif isinstance(year, int):
        return year >= 1900 and year <= date.today().year
    else:
        return False


def validate_month(month: Union[str, int]) -> bool:
    if isinstance(month, str):
        return int(month) >= 1 and int(month) <= 12
    elif isinstance(month, int):
        return month >= 1 and month <= 12
    else:
        return False


def validate_day(day: Union[str, int]) -> bool:
    if isinstance(day, str):
        return int(day) >= 1 and int(day) <= 31
    elif isinstance(day, int):
        return day >= 1 and day <= 31
    else:
        return False


def generate_password_reset_code(serial_number: str, year: Union[str, int], month: Union[str, int], day: Union[str, int]) -> str:
    combined = serial_number + \
        str(year) + str(month).zfill(2) + str(day).zfill(2)

    magic_number = sum(ord(char) * idx ^ idx for idx,
                       char in enumerate(combined, 1))
    magic_number *= 1751873395
    magic_number = (magic_number % 0x100000000) >> 0

    serial_code = ""
    for idx, char in enumerate(str(magic_number)):
        char_code = ord(char)
        if char_code < 51:
            serial_code += chr(char_code + 33)
        elif char_code < 53:
            serial_code += chr(char_code + 62)
        elif char_code < 55:
            serial_code += chr(char_code + 47)
        elif char_code < 57:
            serial_code += chr(char_code + 66)
        else:
            serial_code += chr(char_code)

    return serial_code
