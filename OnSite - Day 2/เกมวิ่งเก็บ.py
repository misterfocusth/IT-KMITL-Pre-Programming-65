"""Docstring"""


def main():
    """Main Functions"""
    positions = input().split()
    current_pos = 0
    total_distance = 0
    for position in positions:
        position = float(position)
        distant = abs(current_pos - position)
        current_pos = position
        total_distance += distant
    print("%.2f" % float(total_distance))


main()
