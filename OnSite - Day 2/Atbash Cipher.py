'''Atbash Cipher'''


def main():
    '''This is main function'''

    sentence = input()
    result = ""
    a_z = "abcdefghijklmnopqrstuvwxyz"

    for alphabet in sentence:
        if alphabet.isalpha():
            idx = a_z.index(alphabet.lower())
            if alphabet.islower():
                result += chr(122 - idx)
            else:
                result += chr(90 - idx)
        else:
            result += alphabet

    print(result)


main()
