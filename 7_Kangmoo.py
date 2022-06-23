"""This is Docstring"""


def main():
    """น้องน้องควรช่วยพี่ หาพื้นที่ของคางหมู"""
    height = float(input())
    long_1 = float(input())
    long_2 = float(input())
    result = (1/2) * height * (long_1 + long_2)
    print("Trapezoidal area = %.2f" % result)


main()
