"""This is Docstring"""


def find_det(num_1, num_2, num_3, num_4):
    """find det value of matrix"""
    return (num_1 * num_4) - (num_2 * num_3)


def main():
    """Oh My Matrix"""
    matrix_a1 = int(input())
    matrix_a2 = int(input())
    matrix_a3 = int(input())
    matrix_a4 = int(input())

    matrix_c1 = int(input())
    matrix_c2 = int(input())
    matrix_c3 = int(input())
    matrix_c4 = int(input())

    matrix_b1 = matrix_c1 - matrix_a1
    matrix_b2 = matrix_c2 - matrix_a2
    matrix_b3 = matrix_c3 - matrix_a3
    matrix_b4 = matrix_c4 - matrix_a4

    result = float(find_det(matrix_a1, matrix_a2, matrix_a3, matrix_a4)
                   + find_det(matrix_b1, matrix_b2, matrix_b3, matrix_b4)
                   + find_det(matrix_c1, matrix_c2, matrix_c3, matrix_c4))

    print("b1: %s" % str(matrix_b1))
    print("b2: %s" % str(matrix_b2))
    print("b3: %s" % str(matrix_b3))
    print("b4: %s" % str(matrix_b4))
    print("D: %.2f" % result)


main()
