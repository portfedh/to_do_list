# Imports
import datetime as dt


def current_month_number():
    """ Will display the current month as a number from 1-12."""
    today = dt.datetime.now()
    return today.month


if __name__ == "__main__":

    print("Function executed directly.")
    current_month_number = current_month_number()
    print("Current month number: ", current_month_number)
