import numpy as np


if __name__ == '__main__':
    matrix = np.matrix((
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9)
    ))
    print(f'Исходная матрица A:\n{matrix}', end='\n\n')
    print(f'Транспонированная матрица A:\n{matrix.transpose()}', end='\n\n')

    matrix_b = np.matrix((
        (5, 8, 2),
        (6, 3, 2),
        (8, 9, 1)
    ))
    print(f'Матрица B:\n{matrix_b}', end='\n\n')
    print(f'A * B:\n{matrix * matrix_b}', end='\n\n')

    print(f'Ранг матрицы A:\n{np.linalg.matrix_rank(matrix)}', end='\n\n')
