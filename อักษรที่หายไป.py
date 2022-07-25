"""อักษรที่หายไป // https://ejudge.it.kmitl.ac.th/problem/7921"""


def main():
    """Main Function"""
    msg = input()
    if msg.count("\"") == 0:
        return print("No error")
    else:
        cal = msg.index("\"")
        cal2 = msg.rindex("\"")
        character = chr(int(msg[cal+1:cal2]))
        print(msg.replace(msg[cal:cal2+1], character))


main()
