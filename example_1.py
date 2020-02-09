#!/usr/bin/env python3

import traceback

import hikvision_password


def main():
    print("This tool will generate a password reset code which you may use to reset a forgotten admin password for a Hikvision camera")

    while True:
        serial_number = input("Enter camera serial number: ")
        if hikvision_password.validate_serial_number(serial_number):
            break
        else:
            print("Invalid serial number. Press Ctrl+C to abort.")
            continue

    while True:
        year = input("Enter year displayed on screen: ")
        if hikvision_password.validate_year(year):
            break
        else:
            print("Invalid year. Press Ctrl+C to abort.")
            continue

    while True:
        month = input("Enter month displayed on screen: ")
        if hikvision_password.validate_month(month):
            break
        else:
            print("Invalid month. Press Ctrl+C to abort.")
            continue

    while True:
        day = input("Enter day displayed on screen: ")
        if hikvision_password.validate_day(day):
            break
        else:
            print("Invalid day. Press Ctrl+C to abort.")
            continue

    reset_code = hikvision_password.generate_password_reset_code(
        serial_number, year, month, day)

    print(f"Your password reset code is \"{reset_code}\"")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Aborted by user request")
    except Exception:
        traceback.print_exc()
