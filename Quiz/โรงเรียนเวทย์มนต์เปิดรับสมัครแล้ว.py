"""โรงเรียนเวทย์มนต์เปิดรับสมัครแล้ว / https://ejudge.it.kmitl.ac.th/problem/8046"""


def main():
    """Main Function"""
    name = input()
    age = int(input())
    sex = input().lower()
    height = float(input())
    name_title = "Mr." if sex == "male" else "Miss"

    application_result = "You can not join this school."

    print("%s %s Age: %d Height: %.2f" %
          (name_title, name, age, height))

    if 13 <= age <= 15:
        if sex == "male" and height >= 160:
            application_result = "You can study in junior high school."
        elif sex == "female" and height >= 155:
            application_result = "You can study in junior high school."
    elif 16 <= age <= 18:
        if sex == "male" and height >= 170:
            application_result = "You can study in senior high school."
        elif sex == "female" and height >= 165:
            application_result = "You can study in senior high school."

    print(application_result)


main()
