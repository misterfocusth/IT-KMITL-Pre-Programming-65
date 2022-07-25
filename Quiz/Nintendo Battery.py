"""Nintendo Battery / https://ejudge.it.kmitl.ac.th/problem/8044"""


def main():
    """Main Function"""
    battery_percent = int(input())
    battery_wide_range = int(input())
    remaining_battery = int(battery_percent / 100 * battery_wide_range) * "O"
    used_battery = (battery_wide_range - len(remaining_battery)) * "_"
    print("(%s%s) %d%%" % (remaining_battery, used_battery, battery_percent))


main()
