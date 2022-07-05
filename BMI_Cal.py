"""This is Docstring"""


def main():
    """BMI Calculation"""
    name = input()
    weight = int(input())
    height = int(input()) / 100
    bmi = weight / height ** 2
    print("Name: %s" % name)
    print("Weight: %d kg." % weight)
    print("Height: %.2f m." % height)
    print("BMI: %.2f" % bmi)


main()
