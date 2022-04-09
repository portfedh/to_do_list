
# Imports
import find_current_month_number as find
import month_list as month


def check_month_activity():
    """ Will check current month and find the activities
    that need to be done during that month."""
    current_month = find.current_month_number()
    if current_month == 1:
        month.enero()
    elif current_month == 2:
        month.febrero()
    elif current_month == 3:
        month.marzo()
    elif current_month == 4:
        month.abril()
    elif current_month == 5:
        month.mayo()
    elif current_month == 6:
        month.junio()
    elif current_month == 7:
        month.julio()
    elif current_month == 8:
        month.agosto()
    elif current_month == 9:
        month.septiembre()
    elif current_month == 10:
        month.octubre()
    elif current_month == 11:
        month.noviembre()
    elif current_month == 12:
        month.diciembre()


if __name__ == "__main__":
    check_month_activity()
