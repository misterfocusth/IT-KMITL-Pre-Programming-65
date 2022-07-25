"""Toy Factory / https://ejudge.it.kmitl.ac.th/problem/7932"""


def main():
    """Main Function"""
    parts = [" ^----^", "( 0--0 )", "<------>", "(------)", " u----u"]
    part_1 = int(input()) - 1
    part_2 = int(input()) - 1
    part_3 = int(input()) - 1
    part_4 = int(input()) - 1
    part_5 = int(input()) - 1

    print(parts[part_1])
    print(parts[part_2])
    print(parts[part_3])
    print(parts[part_4])
    print(parts[part_5])


main()
