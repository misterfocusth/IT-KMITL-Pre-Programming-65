"""This is Docstring"""


def main():
    """Restaurant"""
    age = int(input())
    quantity = int(input())
    if age >= 60 and quantity == 1:
        print("Free")
    elif age >= 60 and quantity > 1:
        print("Pay %d baht" % ((quantity * 100) - (quantity * 100) * 50/100))
    else:
        print("Pay %d baht" % (quantity * 100))


main()
