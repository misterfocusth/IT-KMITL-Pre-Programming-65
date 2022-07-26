"""Docstring"""


def main():
    """Main Function"""
    length = int(input())
    if length <= 0:
        return print("No Tape Measure")
    total = 0
    while True:
        new_num = input()
        if new_num == "No more!":
            break
        elif int(new_num) > length:
            pass
        if new_num.isnumeric() and int(new_num) <= length:
            total += int(new_num)
    if total == 0:
        print("Not Found Number")
    else:
        print("Sum of Found Number = %d" % total)


main()
