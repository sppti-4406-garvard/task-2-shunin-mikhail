from matrix import Matrix


def main():
    matrix_to_transpose = Matrix(3, 3)
    matrix_to_transpose.build_matrix_random()
    print(f'{"*" * 5} Исходная матрица/Транспонированная {"*" * 5}')
    print(matrix_to_transpose)

    matrix_to_transpose.transpose()
    print(matrix_to_transpose)
    print('-' * 20)

    ########################################################################

    print(f'{"*" * 5} Умножение матриц {"*" * 5}')
    matrix_a = Matrix(2, 3)  # Create matrix 2x3
    matrix_a.build_matrix_random()
    print('Matrix A:')
    print(matrix_a)

    matrix_b = Matrix(3, 2)  # Create matrix 3x2
    matrix_b.build_matrix_random()
    print('Matrix B:')
    print(matrix_b)

    try:
        result = matrix_a * matrix_b
        print('Result of A * B:')
        print(result)
    except ValueError as e:
        print(f"Error: {e}")
    print('>' * 15)

    ########################################################################

    matrix_to_rank = Matrix(3, 3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    print("Исходная матрица:")
    print(matrix_to_rank)

    rank = matrix_to_rank.rank()
    print(f"Ранг матрицы: {rank}")


if __name__ == '__main__':
    main()