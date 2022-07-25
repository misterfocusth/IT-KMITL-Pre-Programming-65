"""Docstring"""


def main():
    """Main Function"""
    balance = int(input())
    water_qty = int(input())
    snack__1_qty = int(input())
    snack__2_qty = int(input())
    snack__3_qty = int(input())

    balance_temp = balance - water_qty
    mod_balance_temp = balance_temp % 3

    snack_1, snack_2, snack_3 = 0, 0, 0

    if mod_balance_temp == 0:
        snack_1 = 10 * snack__1_qty
    elif mod_balance_temp == 1:
        snack_1 = 15 * snack__1_qty
    elif mod_balance_temp == 2:
        snack_1 = 20 * snack__1_qty

    balance_temp -= snack_1
    mod_balance_temp = balance_temp % 3

    if mod_balance_temp == 0:
        snack_2 = 12 * snack__2_qty
    elif mod_balance_temp == 1:
        snack_2 = 15 * snack__2_qty
    elif mod_balance_temp == 2:
        snack_2 = 18 * snack__2_qty

    balance_temp -= snack_2
    mod_balance_temp = balance_temp % 3

    if mod_balance_temp == 0:
        snack_3 = 5 * snack__3_qty
    elif mod_balance_temp == 1:
        snack_3 = 7 * snack__3_qty
    elif mod_balance_temp == 2:
        snack_3 = 9 * snack__3_qty

    balance_temp -= snack_3

    if balance_temp < 0:
        print("Now you have %d left." % int(balance))
        print("You don't have enough money!")
    else:
        print("Now you have %d left." % int(balance_temp))
        print("Here's your order!")
        print("Water: %d baht" % water_qty)
        print("Snack number 1: %d baht" % snack_1)
        print("Snack number 2: %d baht" % snack_2)
        print("Snack number 3: %d baht" % snack_3)


main()
