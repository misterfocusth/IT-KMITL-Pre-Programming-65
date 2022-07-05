"""This is Docstring"""


def main():
    """Introduce Yourself"""
    name = input()
    nickname = input()
    born_in = int(input())
    age = 2022 - born_in
    print("My name is %s, My nickname is %s, I'm I was born in %d" %
          (name, nickname, age))


main()
