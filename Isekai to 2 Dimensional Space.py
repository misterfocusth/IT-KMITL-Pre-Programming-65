"""Isekai to 2 Dimensional Space // https://ejudge.it.kmitl.ac.th/problem/7920"""
import math


def main():
    """Main Function"""
    position_x = float(input())
    position_y = float(input())
    kajud = float(input())
    deg = float(input())

    rad_x = abs(math.radians(deg))
    rad_y = abs(math.radians(deg))

    dis_x = math.cos(rad_x)*kajud
    dis_y = math.sin(rad_y)*kajud
    total_x = position_x + dis_x
    total_y = position_y + dis_y
    print("%.2f" % total_x)
    print("%.2f" % total_y)


main()
