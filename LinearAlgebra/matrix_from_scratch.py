from typing import List, Tuple
from sys import exit


class Matrix:
    def __init__(self, matrix: List, empty_matrix_dimentions=(1, 1)) -> None:
        self.empty_matrix_dimentions = empty_matrix_dimentions
        self.matrix = self.verify_matrix(matrix)
        self.shape = self.get_matrix_shape()

        if self.shape[1] > 1:
            self.determinant = self.calculate_determinant(self.matrix)
            self.matrix_type = self.get_matrix_type()
        else:
            self.determinant = None
            self.matrix_type = "vector"

    def verify_matrix(self, input_matrix) -> List:
        if input_matrix == []:
            rows = self.empty_matrix_dimentions[0]
            columns = self.empty_matrix_dimentions[1]
            return self.initialize_zeros_matrix(rows, columns)

        inside_matrix = type(input_matrix[0])
        if inside_matrix is int or inside_matrix is float:
            vector = []
            for x in input_matrix:
                x_list = []
                x_list.append(x)
                vector.append(x_list)
            return vector
        elif inside_matrix is list:
            return input_matrix
        else:
            print("Wrong element type, should be List[List] or List[int]")
            exit(1)

    def calculate_determinant(self, matrix):
        if len(matrix) == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

        determinant = 0
        for c in range(len(matrix)):
            sub_matrix = [row[:c] + row[c + 1 :] for row in matrix[1:]]

            sign = (-1) ** c
            sub_det = self.calculate_determinant(sub_matrix)
            determinant += sign * matrix[0][c] * sub_det

        return determinant

    def get_matrix_type(self) -> str:
        if self.determinant == 0:
            return "singular"
        else:
            return "non-singular"

    def get_matrix_shape(self, matrix=None) -> Tuple:
        if not matrix:
            matrix = self.matrix

        rows = len(matrix)
        columns = len(matrix[0])

        return (rows, columns)

    def initialize_zeros_matrix(self, rows, columns) -> List:
        matrix = []
        for _ in range(rows):
            row = [0] * columns
            matrix.append(row)

        return matrix

    def transpose(self, matrix=None) -> List:
        if not matrix:
            matrix = self.matrix

        shape = self.get_matrix_shape(matrix)
        rows = shape[0]
        columns = shape[1]
        reversed_matrix = self.initialize_zeros_matrix(rows, columns)

        for i in range(rows):
            for j in range(columns):
                reversed_matrix[i][j] = matrix[j][i]

        return reversed_matrix

    def _get_minor(self, m, i, j):
        return [row[:j] + row[j + 1 :] for row in (m[:i] + m[i + 1 :])]

    def calculate_inverse(self, matrix):
        determinant = self.calculate_determinant(matrix)

        if len(matrix) == 2:
            return [
                [matrix[1][1] / determinant, -1 * matrix[0][1] / determinant],
                [-1 * matrix[1][0] / determinant, matrix[0][0] / determinant],
            ]

        cofactors = []
        for row in range(len(matrix)):
            cofactor_row = []
            for column in range(len(matrix)):
                minor = self._get_minor(matrix, row, column)
                cofactor_row.append(
                    ((-1) ** (row + column)) * self.calculate_determinant(minor)
                )
            cofactors.append(cofactor_row)
        cofactors = self.transpose(cofactors)

        for r in range(len(cofactors)):
            for c in range(len(cofactors)):
                cofactors[r][c] = cofactors[r][c] / determinant

        return cofactors


class MatrixOps:
    def __init__(self, a: Matrix, b: Matrix, show=True) -> None:
        self.a = a
        self.b = b
        self.show = show

    def addition(self) -> Matrix:
        new_matrix = []
        for a, b in zip(self.a.matrix, self.b.matrix):
            new_matrix.append(a + b)

        if self.show:
            print(new_matrix)

        return Matrix(new_matrix)

    def _calculate_dot_product(self, x, y):
        if x.matrix_type == "vector" and y.matrix_type == "vector":
            product = 0.0
            for a, b in zip(x.matrix, y.matrix):
                product += a[0] * b[0]
            return product
        else:
            print("can only calculate dor product for vectors")
            exit(1)

    def dot_product(self) -> float | None:
        product = self._calculate_dot_product(self.a, self.b)

        if self.show:
            print(product)

        return product

    def multiplication(self):
        result = Matrix(
            [],
            empty_matrix_dimentions=(
                self.a.shape[1],
                self.b.shape[0],
            ),
        ).matrix

        for i, row_a in enumerate(self.a.matrix):
            row_a = Matrix(row_a)

            for j, column_b in enumerate(self.b.transpose()):
                column_b = Matrix(column_b)
                result[i][j] = self._calculate_dot_product(row_a, column_b)

        return result


if __name__ == "__main__":
    c = [
        [6, 1, 1],
        [4, -2, 5],
        [2, 8, 7],
    ]

    ma = Matrix(c)
    inverse = ma.calculate_inverse(c)
    print(inverse)
    # proof
    print(MatrixOps(ma, Matrix(inverse)).multiplication())
