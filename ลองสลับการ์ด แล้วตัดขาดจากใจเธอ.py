"""This is Docstring"""


def main():
    """Suffer Card"""
    card_deck = ["A", "B", "C"]
    suffer_idx = int(input())
    result = suffer_idx % 3
    print(card_deck[result])


main()
