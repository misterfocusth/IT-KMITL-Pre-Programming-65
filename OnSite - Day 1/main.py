"""Docstring"""


def main():
    """Main Function"""
    gpa = float(input())

    if gpa < 1.00:
        return print("I'm so sad.")
    elif gpa < 2.00:
        return print("%.2f" % float(2*2 - gpa))
    else:
        return print("I'm so happy.")


main()
