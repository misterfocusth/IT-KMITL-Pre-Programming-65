"""This is Docstring"""


def main():
    """Sum Money"""
    person_1 = input()
    person_2 = input()
    money_1 = float(input())
    money_2 = float(input())
    major = input()
    separator = input()
    sum_money = str(money_1 + money_2)
    print("%s %s%s%s%s%s" % (person_1, person_2,
                             separator, sum_money, separator, major))


main()
