"""This is Docstring"""


def main():
    """NMI KM"""
    nautical_mile = float(input())
    msec = int(input())
    speed = (nautical_mile * 1852) / (msec * 0.001)
    print("อัตราเร็วเท่ากับ : %.3f เมตรต่อวินาที" % speed)


main()
