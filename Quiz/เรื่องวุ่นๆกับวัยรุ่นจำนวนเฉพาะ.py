"""เรื่องวุ่นๆกับวัยรุ่นจำนวนเฉพาะ / https://ejudge.it.kmitl.ac.th/problem/8045"""
import math


def main():
    """Main Function"""
    number = int(input())
    is_prime = True
    mod_number = 2
    if number > 1:
        while mod_number <= math.sqrt(number):
            if number % mod_number < 1:
                is_prime = False
            mod_number += 1
    else:
        is_prime = False

    if is_prime:
        print("Prime Number")
    else:
        print("Not Prime Number")


main()
