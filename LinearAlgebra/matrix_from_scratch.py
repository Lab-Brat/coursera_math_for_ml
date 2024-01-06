from typing import List, Tuple


class Matrix:
    def __init__(self, matrix: List) -> None:
        self.matrix = matrix
        self.determinant = self.calculate_determinant(self.matrix)
        self.matrix_type = self.get_matrix_type()
        self.size = self.get_matrix_size()

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

    def get_matrix_size(self) -> Tuple:
        rows = len(self.matrix[0])
        columns = len(self.matrix)

        return (rows, columns)


class MatrixOps:
    def __init__(self, a: Matrix, b: Matrix, show=True) -> None:
        self.a = a.matrix
        self.b = b.matrix
        self.show = show

    def addition(self) -> Matrix:
        new_matrix = []
        for a, b in zip(self.a, self.b):
            new_matrix.append(a + b)

        if self.show:
            print(new_matrix)

        return Matrix(new_matrix)

    def dot_product(self) -> float:
        return 0.1


if __name__ == "__main__":
    a = [
        [-3, 8, 1],
        [2, 2, -1],
        [-5, 6, 2],
    ]
    ma = Matrix(a)
    print(ma.determinant)
    print(ma.size)
