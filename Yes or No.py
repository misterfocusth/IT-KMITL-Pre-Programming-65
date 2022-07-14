"""yes or no // https://ejudge.it.kmitl.ac.th/problem/7913"""


def main():
    """Check is text is identical or not"""
    is_identifier = input().isalnum()
    print("Yes, it is." if is_identifier else "No, it's not.")


main()
