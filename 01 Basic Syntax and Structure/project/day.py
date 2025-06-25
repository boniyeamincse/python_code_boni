# I want to input my birthday and get my age, days, minutes, and seconds lived.

from datetime import datetime
from dateutil.relativedelta import relativedelta
from dateutil.parser import parse

def calculate_age_and_days(birthday_str):
    today = datetime.now()
    birthday = parse(birthday_str)
    age = relativedelta(today, birthday)
    delta = today - birthday
    days = delta.days
    minutes = days * 24 * 60
    seconds = minutes * 60
    return age, days, minutes, seconds

def main():
    print("Welcome to the Birthday Calculator!")
    birthday = input("Please enter your birthday (YYYY-MM-DD): ")
    try:
        age, days, minutes, seconds = calculate_age_and_days(birthday)
        print(f"\nYou are {age.years} years, {age.months} months, and {age.days} days old.")
        print("You have lived for approximately:")
        print(f"- {days} days")
        print(f"- {minutes} minutes")
        print(f"- {seconds} seconds")
        print("\nThank you for using the Birthday Calculator!")
    except Exception as e:
        print("Invalid date format. Please enter your birthday in YYYY-MM-DD format.")

if __name__ == "__main__":
    main()