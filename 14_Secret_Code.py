"""This is Docstring"""


def main():
    """Secret Code"""
    nums = int(input())
    nums_1 = nums % 1000000000 // 100000000
    nums_2 = nums % 10000000 // 1000000
    nums_3 = nums % 100000 // 10000
    nums_4 = nums % 1000 // 100
    nums_5 = nums % 10 // 1
    print("%d%d%d%d%d" % (nums_1, nums_2, nums_3, nums_4, nums_5))


main()
