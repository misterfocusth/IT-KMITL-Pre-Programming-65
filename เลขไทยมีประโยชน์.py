"""เลขไทยมีประโยชน์ // https://ejudge.it.kmitl.ac.th/problem/7910"""


def main():
    """ Main function """
    is_half = False
    is_thai = True
    ticket_price = 0
    if input() == "N":
        is_thai = False
        nationality = input()
        if nationality == "Vietnam" or nationality == "Singapore" or nationality == "India":
            is_half = True
    age = int(input())
    if age > 60 or age <= 10:
        ticket_price = 0
    elif age > 10 and age <= 20:
        ticket_price = 100
    else:
        ticket_price = 200
    if is_thai:
        ticket_price *= 0.2
    if is_half:
        ticket_price *= 0.5
    if input() == "Y":
        ticket_price = ticket_price - (ticket_price * (int(input()) / 100))
    print("%.2f" % ticket_price)


main()
