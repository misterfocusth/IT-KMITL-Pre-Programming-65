"""This is Docstring"""


def main():
    """เค้กช็อกโกแลต"""
    money = int(input())
    price = int(input())
    quantity = money // price
    change = money - (price * quantity)
    if money < price:
        print("Not enough money;(")
        print("Money left: %d" % money)
    else:
        print("Chocolate Cake: %d" % quantity)
        print("Money left: %d" % change)


main()
