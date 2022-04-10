import check_category
import check_month


selection = input("\nChecking to do list: Sort by category(c) or month(m)?: ")


def to_do_list():
    if selection == "c":
        check_category.check_category()
    elif  selection == "m":
        check_month.check_month()
    else:
        print("Selection not recognized.")


if __name__ == "__main__":
    to_do_list()