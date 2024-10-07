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

if __name__ == '__main__':
    main()
