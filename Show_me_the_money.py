"""Show Me The Money - https://ejudge.it.kmitl.ac.th/problem/7909"""


def show_me_the_money(received_money, item_price):
    """Cal Change Money and Return How Many Banknotes or Coins that need to return"""
    if item_price > received_money:
        return print("จำนวนเงินไม่พอ")
    elif received_money == item_price:
        return print("จ่ายมาพอดี")

    change_money = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    remaining_change = received_money - item_price

    change_money[9] = remaining_change // 100
    remaining_change = remaining_change % 100

    if remaining_change > 0:
        change_money[8] = remaining_change // 50
        remaining_change = remaining_change % 50

    if remaining_change > 0:
        change_money[7] = remaining_change // 20
        remaining_change = remaining_change % 20

    if remaining_change > 0:
        change_money[6] = remaining_change // 12
        remaining_change = remaining_change % 12

    if remaining_change > 0:
        change_money[5] = remaining_change // 10
        remaining_change = remaining_change % 10

    if remaining_change > 0:
        change_money[4] = remaining_change // 5
        remaining_change = remaining_change % 5

    if remaining_change > 0:
        change_money[3] = remaining_change // 2
        remaining_change = remaining_change % 2

    if remaining_change > 0:
        change_money[2] = remaining_change // 1
        remaining_change = remaining_change % 1

    if remaining_change > 0:
        change_money[1] = remaining_change // 0.50
        remaining_change = remaining_change % 0.50

    if remaining_change > 0:
        change_money[0] = remaining_change // 0.25
        remaining_change = remaining_change % 0.25

    print("เเบงค์ 100 บาท : %d" % change_money[9])
    print("เเบงค์ 50 บาท : %d" % change_money[8])
    print("เเบงค์ 20 บาท : %d" % change_money[7])
    print("เเบงค์ 12 บาท : %d" % change_money[6])
    print("เเบงค์ 10 บาท : %d" % change_money[5])
    print("เหรียญ 5 บาท : %d" % change_money[4])
    print("เหรียญ 2 บาท : %d" % change_money[3])
    print("เหรียญ 1 บาท : %d" % change_money[2])
    print("เหรียญ 50 สตางค์ : %d" % change_money[1])
    print("เหรียญ 25 สตางค์ : %d" % change_money[0])


def main():
    """Main Function"""
    received_money = float(input())
    item_price = float(input())
    show_me_the_money(received_money, item_price)


main()
