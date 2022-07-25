"""ค่าไฟแพงเกินปุยมุ้ย!! / https://ejudge.it.kmitl.ac.th/problem/7931"""


def main():
    """Main Function"""
    watt_a = int(input())
    watt_b = int(input())
    watt_c = int(input())
    watt_d = int(input())
    watt_e = int(input())

    print("TV %d Watt 1 ea for 3 hours" % watt_a)
    print("%.2f unit." % float(watt_a * 3 * 30 / 1000))
    print("Microwave %d Watt 1 ea for 1 hours" % watt_b)
    print("%.2f unit." % float(watt_b * 1 * 30 / 1000))
    print("Hair dryer %d Watt 1 ea for 0.5 hours" % watt_c)
    print("%.2f unit." % float(watt_c * 0.5 * 30 / 1000))
    print("light bulb %d Watt 4 ea for 5 hours" % watt_d)
    print("%.2f unit." % float((watt_d * 5 * 30 / 1000) * 4))
    print("Refrigerator %d Watt 1 ea for 24 hours" % watt_e)
    print("%.2f unit." % float(watt_e * 24 * 30 / 1000))


main()
