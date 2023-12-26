from typing import List

class Matrix:
    def __init__(self, matrix: List) -> None:
        self.matrix = matrix
        self.determinant = self.calculate_determinant(self.matrix)

    def calculate_determinant(self, matrix):
        if len(matrix) == 2:
            return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

        determinant = 0
        for c in range(len(matrix)):
            sub_matrix = [row[:c] + row[c+1:] for row in matrix[1:]]
            
            sign = (-1) ** c
            sub_det = self.calculate_determinant(sub_matrix)
            determinant += sign * matrix[0][c] * sub_det

        return determinant


class MatrixOps:
    def __init__(self, a: List[int], b: List[int], show = True) -> None:
        self.a = a
        self.b = b
        self.show = show

    def addition(self) -> List[int]:
        new_matrix = []
        for a, b in zip(self.a, self.b):
            new_matrix.append(a + b)

        if self.show:
            print(new_matrix)

        return new_matrix

    def multiplication(self) -> List[int]:
        new_matrix = []
        for a, b in zip(self.a, self.b):
            new_matrix.append(a * b)

        if self.show:
            print(new_matrix)

        return new_matrix

    def find_type_using_sum(self) -> str:
        a_sum = sum(self.a)
        b_sum = sum(self.b)
        division = 0
        
        if a_sum >= b_sum:
            division = a_sum / b_sum
        else:
            division = b_sum / a_sum

        if division.is_integer():
            if self.show:
                print("Matrix is singular")
            return "singular"
        else:
            if self.show:
                print("Matrix is non-singular")
            return "non-singular"

    def find_type_using_determinant(self) -> str:
        determinant = self.find_determinant()

        if determinant == 0:
            if self.show:
                print("Matrix is singular")
            return "singular"
        else:
            if self.show:
                print("Matrix is non-singular")
            return "non-singular"

    def find_determinant(self) -> int:
        reverse_b = self.b[::-1]
        determinant = 0
        i = 1

        for a, b in zip(self.a, reverse_b):
            determinant += i * (a + b)
            i *= -1

        if self.show:
            print(f"Determinant is {determinant}")

        return determinant


if __name__ == "__main__":
    a = [
        [5, 1],
        [-1, 3],
    ]
    b = [
        [2, -1],
        [-6, 3],
    ]
    c = [
        [1, 2, 3],
        [4, 10, 6],
        [7, 8, 9],
    ]
    ma = Matrix(a)
    mb = Matrix(b)
    mc = Matrix(c)
    print(ma.determinant)
    print(mb.determinant)
    print(mc.determinant)

