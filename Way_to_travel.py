"""This is Docstring"""


def main():
    """Way To Travel"""
    weather = input()
    priority = input()
    distant = int(input())
    result = ""
    if weather == "rainy" and priority == "not important":
        result = "Not go"
    elif distant < 0:
        result = "Error"
    if distant < 1:
        result = "Walk"
    elif distant < 20:
        result = "Motorcycle"
    elif distant < 300:
        result = "Car"
    else:
        result = "Private jet"
    print(result)


main()
