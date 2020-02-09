#!/usr/bin/env python3

import argparse
import sys
import traceback

import hikvision_password


def main():
    parser = argparse.ArgumentParser(
        description="This tool will generate a password reset code which you may use to reset a forgotten admin password for a Hikvision camera")
    parser.add_argument("--serial", "-s", type=str, help="Camera serial number")
    parser.add_argument("--year", "-y", type=int, help="Year displayed on screen")
    parser.add_argument("--month", "-m", type=int, help="Month displayed on screen")
    parser.add_argument("--day", "-d", type=int, help="Day displayed on screen")

    if len(sys.argv)==1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()

    if hikvision_password.validate_serial_number(args.serial) is False:
        raise ValueError("Invalid serial number")

    if hikvision_password.validate_year(args.year) is False:
        raise ValueError("Invalid year")

    if hikvision_password.validate_month(args.month) is False:
        raise ValueError("Invalid month")

    if hikvision_password.validate_day(args.day) is False:
        raise ValueError("Invalid day")

    reset_code = hikvision_password.generate_password_reset_code(
        args.serial, args.year, args.month, args.day)

    print(f"Your password reset code is \"{reset_code}\"")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Aborted by user request")
    except Exception:
        traceback.print_exc()
