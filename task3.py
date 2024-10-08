from matrix import Matrix


def main():
    matrix = Matrix(3, 3, [
        [1, -2, 3],
        [4, 0, 6],
        [-7, 8, 9]
    ])

    print(matrix)
    print(Matrix.minor(matrix.matrix, 1, 0))
    print(Matrix.det(matrix.matrix))

    print(matrix.inv())
    print(Matrix.inv_static(matrix.matrix))

    matrix_non_square = Matrix(3, 6, [
        [1, 2, 3, 4, 7, 3],
        [1, 2, 3, 4, 23, 2],
        [5, 6, 3, -1, 2, 2]
    ])
    print(Matrix.rank_static(matrix_non_square.matrix))

    matrix_non_square_2 = Matrix(3, 4, [
        [1, 2, 3, 4],
        [1, 2, 3, 4],
        [5, 6, 3, -11]
    ])
    print(Matrix.rank_static(matrix_non_square_2.matrix))

if __name__ == '__main__':
    main()
