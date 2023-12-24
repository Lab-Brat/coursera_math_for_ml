from typing import List

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
        a_sum = sum(a)
        b_sum = sum(b)
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
    a = [1, 1]
    b = [2, 1]
    m = MatrixOps(a, b)
    m.addition()
    m.multiplication()
    m.find_type_using_sum()
    m.find_type_using_determinant()

