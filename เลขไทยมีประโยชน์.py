"""เลขไทยมีประโยชน์ // https://ejudge.it.kmitl.ac.th/problem/7910"""


def entry_price_cal(is_thai, nationality, age, is_use_discount, discount_percent):
    """Calculate entry price for visitors"""
    kid_price = 20.00
    adult_price = 40.00
    eligible_discount_countries = ["Vietnam", "Singapore", "India"]

    total_price = kid_price if (age > 10 and age < 20) else adult_price

    if age <= 10 or age >= 60:
        return print(0.00)

    if is_thai == "N":
        total_price = total_price * 5

    if eligible_discount_countries.count(nationality) > 0:
        total_price = total_price * 0.50

    if is_use_discount == "Y":
        total_price = total_price - \
            (total_price * (float(discount_percent) / 100))

    return print("%.2f" % total_price)


def main():
    """Main Function"""
    is_thai = input()
    nationality = "Thai"

    if is_thai == "N":
        nationality = input()

    age = int(input())
    is_use_discount = input()
    discount_percent = 0.00

    if is_use_discount == "Y":
        discount_percent = float(input())

    entry_price_cal(is_thai, nationality, age,
                    is_use_discount, discount_percent)

    entry_price_cal("N", "Islamic Republic of Afghanistan", 42, "N", 0)
    entry_price_cal("Y", "Thai", 15, "N", 0)
    entry_price_cal("Y", "Thai", 55, "Y", 20)
    entry_price_cal("N", "Vietnam", 25, "Y", 50)


main()
