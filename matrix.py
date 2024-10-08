import random


class Matrix:
    def __init__(self, n, m, matrix=None):
        if matrix is None:
            matrix = []

        self.n = n
        self.m = m
        self.matrix = matrix

    # Print the matrix
    def __repr__(self):
        s = ''
        for n in range(self.n):
            for m in range(self.m):
                s += f'{self.matrix[n][m]}\t\t'
            s += '\n'
        return s

    # Multiple two matrix
    def __mul__(self, other):
        if self.m != other.n:
            raise ValueError("Невозможно умножить: число столбцов первой матрицы не равно числу строк второй матрицы")

        result = Matrix(self.n, other.m)
        for n in range(self.n):
            result_row = []
            for m in range(other.m):
                element_sum = 0
                for k in range(self.m):
                    element_sum += self.matrix[n][k] * other.matrix[k][m]
                result_row.append(element_sum)
            result.matrix.append(result_row)

        return result

    # Building matrix using random values
    def build_matrix_random(self):
        for i in range(self.n):
            row = [random.randint(-100, 100) for _ in range(self.m)]
            self.matrix.append(row)

    # Transpose the matrix
    def transpose(self):
        self.matrix = [[self.matrix[j][i] for j in range(self.n)] for i in range(self.m)]
        self.n, self.m = self.m, self.n     # Swap n, m to correctly transpose print the matrix

    # Transpose static method
    @staticmethod
    def transpose_static(matrix):
        return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

    def inv(self):
        determinant = Matrix.det(self.matrix)
        if determinant == 0:
            raise ValueError("Матрица вырождена и не имеет обратной.")

        # Special for 2x2 matrix:
        if len(self.matrix) == 2:
            return Matrix(2, 2, [
                [self.matrix[1][1] / determinant, -1 * self.matrix[0][1] / determinant],
                [-1 * self.matrix[1][0] / determinant, self.matrix[0][0] / determinant]
            ])

        # Minor, transpose and /det
        cofactors = []
        for r in range(len(self.matrix)):
            cofactorRow = []
            for c in range(len(self.matrix)):
                minor = Matrix.minor(self.matrix, r, c)
                cofactorRow.append(((-1) ** (r + c)) * Matrix.det(minor.matrix))
            cofactors.append(cofactorRow)

        # Transpose the cofactor matrix
        cofactors = Matrix.transpose_static(cofactors)

        # Divide each element by the determinant
        inverse_matrix = []
        for r in range(len(cofactors)):
            inverse_row = []
            for c in range(len(cofactors[r])):
                inverse_row.append(cofactors[r][c] / determinant)
            inverse_matrix.append(inverse_row)

        return Matrix(self.n, self.m, inverse_matrix)

    def rank(self) -> int:
        matrix = self.matrix.copy()
        for row in range(self.n):
            if matrix[row][row] == 0:
                for i in range(row + 1, self.n):
                    if matrix[i][row] != 0:
                        matrix[row], matrix[i] = matrix[i], matrix[row]    # swap rows to avoid zero division
                        break

            if matrix[row][row] == 0:  # double check to avoid zero division
                continue

            leading_element = matrix[row][row]
            for i in range(self.m):  # normalize row by leading element
                matrix[row][i] /= leading_element

            for i in range(row + 1, self.n):
                factor = matrix[i][row]
                for j in range(self.m):
                    matrix[i][j] -= factor * matrix[row][j]

        rank = len(matrix)
        for i in range(len(matrix)):
            if all(element == 0 for element in matrix[i]):
                rank -= 1

        return rank

    @staticmethod
    def inv_static(matrix: list):
        determinant = Matrix.det(matrix)
        if determinant == 0:
            raise ValueError("Матрица вырождена и не имеет обратной.")

        if len(matrix) == 2:
            return Matrix(2, 2, [
                [matrix[1][1] / determinant, -1 * matrix[0][1] / determinant],
                [-1 * matrix[1][0] / determinant, matrix[0][0] / determinant]
            ])

        cofactors = []
        for r in range(len(matrix)):
            cofactorRow = []
            for c in range(len(matrix)):
                minor = Matrix.minor(matrix, r, c)
                cofactorRow.append(((-1) ** (r + c)) * Matrix.det(minor.matrix))
            cofactors.append(cofactorRow)

        cofactors = Matrix.transpose_static(cofactors)

        inverse_matrix = []
        for r in range(len(cofactors)):
            inverse_row = []
            for c in range(len(cofactors[r])):
                inverse_row.append(cofactors[r][c] / determinant)
            inverse_matrix.append(inverse_row)

        return Matrix(len(matrix), len(matrix[0]), inverse_matrix)

    @staticmethod
    def rank_static(matrix: list) -> int:
        matrix_copy = [row[:] for row in matrix]
        n = len(matrix_copy)
        m = len(matrix_copy[0])

        for row in range(n):
            if matrix_copy[row][row] == 0:
                for i in range(row + 1, n):
                    if matrix_copy[i][row] != 0:
                        matrix_copy[row], matrix_copy[i] = matrix_copy[i], matrix_copy[row]
                        break

            if matrix_copy[row][row] == 0:
                continue

            leading_element = matrix_copy[row][row]
            for i in range(m):
                matrix_copy[row][i] /= leading_element

            for i in range(row + 1, n):
                factor = matrix_copy[i][row]
                for j in range(m):
                    matrix_copy[i][j] -= factor * matrix_copy[row][j]

        rank = n
        for i in range(n):
            if all(element == 0 for element in matrix_copy[i]):
                rank -= 1

        return rank

    # Get minor of the matrix
    @staticmethod
    def minor(matrix: list, n: int, m: int):
        res_matrix = []
        for i in range(len(matrix)):
            row_res_matrix = []
            for j in range(len(matrix[0])):
                if i == n or j == m: continue
                row_res_matrix.append(matrix[i][j])
            if row_res_matrix:
                res_matrix.append(row_res_matrix)
        return Matrix(len(matrix) - 1, len(matrix[0]) - 1, res_matrix)

    # Find the determinant of the matrix
    @staticmethod
    def det(matrix: list) -> float | int:
        if len(matrix) != len(matrix[0]):
            raise ValueError('Можно вычислить определитель только на квадратной матрице.')

        if len(matrix) == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

        det = 0
        for i in range(len(matrix)):
            det += ((-1) ** (i + 2)) * matrix[0][i] * Matrix.det(Matrix.minor(matrix, 0, i).matrix)  # +2 - normalize and +1 (first row always)
        return det
