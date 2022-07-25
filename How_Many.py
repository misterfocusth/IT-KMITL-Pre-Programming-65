"""ฺHow many // https://ejudge.it.kmitl.ac.th/problem/7918"""


def solve(text, search_type, keyword):
    """Count how many words or chars found on sentences"""
    count_result = str(text).lower().count(str(keyword).lower())
    if count_result == 0:
        return print("No word and character.")

    if search_type == "Word":
        print("Word : %d" % count_result)
    elif search_type == "Character":
        print("Character : %d" % count_result)


def main():
    """Main Function"""
    text = input()
    keyword = input()
    if len(keyword) == 1:
        solve(text, "Character", keyword)
    else:
        solve(text, "Word", keyword)


main()
