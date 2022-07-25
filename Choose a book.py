"""Choose a book // https://ejudge.it.kmitl.ac.th/problem/7914"""
import math


def main():
    """Main Function"""
    num_n = int(input())
    num_r = int(input())
    result = math.factorial(num_n) / (math.factorial(num_r)
                                      * math.factorial(num_n - num_r))
    print(int(result))


main()
