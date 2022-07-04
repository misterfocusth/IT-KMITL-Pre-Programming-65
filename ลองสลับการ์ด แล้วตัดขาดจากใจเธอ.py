"""This is Docstring"""


def main():
    """Suffer Card"""
    card_deck = ["A", "B", "C"]
    new_deck = ["A", "B", "C"]
    suffer_idx = int(input())
    new_deck[((suffer_idx - 1) % 10 // 1)] = card_deck[(suffer_idx // 10) - 1]
    new_deck[(suffer_idx // 10) - 1] = card_deck[((suffer_idx - 1) % 10 // 1)]
    print(new_deck[1])


main()
