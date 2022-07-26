"""Docstring"""


def rotage_90_deg(raw_string):
    result = ""
    if len(raw_string) == 1:
        for current_idx in range(len(raw_string[0])):
            print(raw_string[0][current_idx])
        return

    for x in range(len(raw_string[0])):




def main():
    """Main Function"""
    rotage_deg = int(input())
    lines = int(input())
    current_string_length = 0
    raw_string = []
    is_invalid = False
    for idx in range(lines):
        new_string = input()
        if idx == 0:
            current_string_length = len(new_string)
            raw_string.append(new_string)
        else:
            if len(new_string) == current_string_length:
                raw_string.append(new_string)
            else:
                is_invalid = True

    if is_invalid:
        return print("Invalid size")

    if rotage_deg == 90:
        rotage_90_deg(raw_string)


main()
