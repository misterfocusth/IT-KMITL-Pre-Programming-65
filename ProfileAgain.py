"""ProfileAgain // https://ejudge.it.kmitl.ac.th/problem/7914"""


def main():
    """Main Function"""
    sex = input().lower().replace("female", "Mrs. ").replace("male", "Mr. ")
    id_number = input()
    first_name = input().capitalize()
    last_name = input().capitalize()
    age = input()
    occupation = input().upper()

    print("=" * 6)
    print("ID : " + id_number[:6])
    print("Name : " + sex + first_name + " " + last_name)
    print("Age : " + age + " years old")
    print("Occupation : " + occupation)
    print("="*6)


main()
