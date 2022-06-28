"""This is Docstring"""


def main():
    """สมการ"""
    num_a = int(input())
    num_b = int(input())
    num_c = int(input())
    num_d = int(input())
    num_x = int(input())
    num_y = int(input())
    result = (num_b / (num_a ** 2 / num_d) + num_x * (num_b / num_a)) / num_c
    print("%.2f" % result)
    num_y = num_y


main()
