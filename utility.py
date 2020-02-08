#!/usr/bin/env python3

import ctypes
import re
import traceback
from datetime import date


def main():
    """This method will generate a password reset code which you may use to
    reset a forgotten admin password for a Hikvision camera.
    """

    """Valid sarial numbers consist of numbers and uppercase characters, total
    length must not exceed 27 characters"""
    while True:
        serial_number = input("Serial number: ")
        if re.search("^[0-9A-Z]+$", serial_number) and len(serial_number) >= 27:
            break
        else:
            print("Invalid serial number")

    """Make sure that user enter valid year"""
    while True:
        year = input("Year: ")
        if not year.isdigit() or (int(year) < 1900 or int(year) > date.today().year):
            print("Invalid year")
            continue
        else:
            break

    """Make sure that user enters valid month"""
    while True:
        month = input("Month: ")
        if not month.isdigit() or (int(month) < 1 or int(month) > 12):
            print("Invalid month")
            continue
        else:
            break

    """Make sure that the user entered day is in the range of valid days for the
    entered year and month period"""
    while True:
        day = input("Day: ")
        try:
            date(int(year), int(month), int(day))
        except TypeError:
            print("Invalid day")
            continue
        else:
            break

    combined = serial_number + year + month.zfill(2) + day.zfill(2)

    magic_number = 0
    for idx, char in enumerate(combined):
        magic_number += (ord(char) * (idx + 1)) ^ (idx + 1)
    magic_number *= 1751873395
    magic_number = ctypes.c_uint32(magic_number).value # convert to 32 bit unsigned integer

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

    print(f"Your password reset code is \"{serial_code}\"")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Aborted by user request")
    except Exception:
        traceback.print_exc()
