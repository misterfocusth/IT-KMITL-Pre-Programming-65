"""ไม่มีต้นหนก็ลำบากหน่อยนะ // https://ejudge.it.kmitl.ac.th/problem/7915"""


def main():
    """Main Function"""
    cached_fish = input()
    number_of_crews = int(input())
    number_of_fishes = cached_fish.count("<^))))><")
    if number_of_fishes > number_of_crews:
        print("We have many fish ahoyy!!!")
    elif number_of_fishes == number_of_crews:
        print("We have enough fish for everyone.")
    else:
        if number_of_fishes*2 == number_of_crews:
            print("We can share the fish together Yahoooo!!!")
        else:
            print("No one will eat them  because we cannot be divided the fish.")


main()
