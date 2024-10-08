from matrix import Matrix


def main():
    matrix = Matrix(3, 4, [
        [1, -2, 3, 7],
        [4, 0, 6, 4],
        [-7, 8, 9, 3]
    ])

    print(matrix)
    print(Matrix.minor(matrix.matrix, 1, 0))
    print(Matrix.det(matrix.matrix))

    print(matrix.inv())
    print(Matrix.inv_static(matrix.matrix))

if __name__ == '__main__':
    main()
