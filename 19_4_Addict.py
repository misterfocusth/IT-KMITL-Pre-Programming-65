"""This is Docstring"""


def main():
    """4 addict"""
    number_x = float(input())
    message = input() * (int(number_x // 44))
    result = ((((number_x+4)**(1/4))+number_x/4) / ((4*number_x) - 4)) * 44
    print(message)
    print("%.4f" % result)


main()
