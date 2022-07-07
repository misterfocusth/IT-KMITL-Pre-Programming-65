"""This is Docstring"""


def main():
    """ร้านขายเสื้อของจอมเวทย์"""
    item_price = 12800
    role = input()
    quantity = 0
    total_price = 0
    if role != "Magician":
        quantity = int(input())
        print("Total %d Jewel" % (item_price * quantity))
    else:
        guild_name = input()
        quantity = int(input())
        if guild_name == "Fairy Tail":
            total_price = (item_price * quantity) - \
                (20/100 * (item_price * quantity))
            print("Total %d Jewel" % total_price)
        elif guild_name == "Sabertooth" and quantity > 5:
            total_price = (item_price * quantity) - \
                (15/100 * (item_price * quantity))
            print("Total %d Jewel" % total_price)
        elif guild_name == "Lamia Scale" and quantity >= 3:
            total_price = (item_price * quantity) - \
                (10/100 * (item_price * quantity))
            print("Total %d Jewel" % total_price)
        elif guild_name == "Blue Pegasus" and quantity > 10:
            total_price = (item_price * quantity) - \
                (5/100 * (item_price * quantity))
            print("Total %d Jewel" % total_price)
        else:
            print("Total %d Jewel" % (item_price * quantity))


main()
