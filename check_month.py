
# Imports
import view_month as month


def check_month():
    while True:
        month_selected = int(input("\nSelect month to check(1-12), or (99) to exit: "))
        if month_selected == 1:
            month.enero()
        elif month_selected == 2:
            month.febrero()
        elif month_selected == 3:
            month.marzo()
        elif month_selected == 4:
            month.abril()
        elif month_selected == 5:
            month.mayo()
        elif month_selected == 6:
            month.junio()
        elif month_selected == 7:
            month.julio()
        elif month_selected == 8:
            month.agosto()
        elif month_selected == 9:
            month.septiembre()
        elif month_selected == 10:
            month.octubre()
        elif month_selected == 11:
            month.noviembre()
        elif month_selected == 12:
            month.diciembre()
        elif month_selected == 99:
            break
        else:
            print("Unrecognized selection. Try again.")

if __name__ == "__main__":
    check_month()
