"""ฺBinaryปิด/เปิด // https://ejudge.it.kmitl.ac.th/problem/7917"""


def decimal_to_binary(number):
    """converting decimal to binary and removing the prefix(0b)"""
    return bin(number).replace("0b", "")


def solve(number):
    """Covert binary number to Open/Close text"""
    number = str(number).replace("1", "open ")
    number = str(number).replace("0", "close ")
    number = number.split(" ")
    number.pop()
    print(", ".join(number))


def main():
    """Main Function"""
    number = decimal_to_binary(int(input()))
    solve(number)


main()
