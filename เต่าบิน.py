"""This is Docstring"""


def main():
    """TaoBin"""
    money = float(input())
    price = float(input())
    change_money = money - price
    change = money - price
    min_ans = 0
    coin_10 = change//10
    min_ans += coin_10
    change -= coin_10 * 10
    coin_5 = change//5
    min_ans += coin_5
    change -= coin_5 * 5
    coin_2 = change//2
    min_ans += coin_2
    change -= coin_2 * 2
    coin_1 = change//1
    min_ans += coin_1
    change -= coin_1 * 1
    coin_050 = change//0.50
    min_ans += coin_050
    change -= coin_050 * 0.5
    coin_025 = change//0.25
    min_ans += coin_025
    change -= coin_025 * 0.25
    max_ans = change_money // 0.25
    print(int(max_ans))
    print(int(min_ans))
    print(str(float(change_money)))


main()
