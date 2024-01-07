from typing import List, Tuple
from sys import exit


class Matrix:
    def __init__(self, matrix: List) -> None:
        self.matrix = self.verify_matrix(matrix)
        self.shape = self.get_matrix_shape()

        if self.shape[1] > 1:
            self.determinant = self.calculate_determinant(self.matrix)
            self.matrix_type = self.get_matrix_type()
        else:
            self.determinant = None
            self.matrix_type = "vector"

    def verify_matrix(self, input_matrix) -> List:
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

    def get_matrix_shape(self) -> Tuple:
        rows = len(self.matrix)
        columns = len(self.matrix[0])

        return (rows, columns)

    def initialize_empty_matrix(self, rows, columns) -> List:
        matrix = []
        for _ in range(rows):
            row = [None] * columns
            matrix.append(row)

        return matrix

    def reverse(self) -> List:
        rows = self.shape[0]
        columns = self.shape[1]
        reversed_matrix = self.initialize_empty_matrix(rows, columns)

        for i in range(rows):
            for j in range(columns):
                reversed_matrix[i][j] = self.matrix[j][i]

        return reversed_matrix


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
        if self.a.matrix_type == "vector" and self.b.matrix_type == "vector":
            product = 0.0
            for a, b in zip(x, y):
                product += a[0] * b[0]
            return product
        else:
            print("can only calculate dor product for vectors")
            exit(1)

    def dot_product(self) -> float | None:
         product = self._calculate_dot_product(self.a.matrix, self.b.matrix)

         if self.show:
             print(product)

         return product


if __name__ == "__main__":
    a = [
        [-3, 8, 1],
        [2, 2, -1],
        [-5, 6, 2],
    ]
    ma = Matrix(a)

    a1 = [
        [2, 1],
        [-3, 2],
    ]
    b1 = [
        [1, 3],
        [6, 2],
    ]
    A1 = Matrix(a1)
    B1 = Matrix(b1)

    print(A1.reverse())
    print(ma.reverse())
