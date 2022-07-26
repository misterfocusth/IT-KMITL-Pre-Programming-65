'''
Math Symbol
'''


def calculate_by_operator(number_list: list, operator: str):
    '''Calculate sum of number in array by operator'''

    total = number_list[0]

    for number in number_list:
        if number_list.index(number) == 0:
            continue

        if operator == '+':
            total += number
        elif operator == '-':
            total -= number
        elif operator == '*':
            total *= number
        elif operator == '/':
            total /= number

    return total


def main():
    '''This is main function'''

    number_list = []
    operator = ''

    while True:
        num = input()

        if num.isnumeric():
            number_list.append(int(num))
            continue

        if num == '+' or num == '-' or num == '*' or num == '/':
            operator = num
            break

    total = calculate_by_operator(number_list, operator)

    print('%.2f' % total)


main()
