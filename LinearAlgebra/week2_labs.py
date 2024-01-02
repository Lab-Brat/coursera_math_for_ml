import numpy as np
from week1_matrix_from_scratch import Matrix

# solving systems of linear equations

# assume matrix
# 4x - 3y +  z = -10
# 2x +  y + 3z = 0
# -x + 2y - 5z = 17

# here is how to solve it with numpy
matrix = [
    [4, -3, 1],
    [2, 1, 3],
    [-1, 2, -5],
]
M = np.array(matrix, dtype=np.dtype(float))
b = np.array([-10, 0, 17], dtype=np.dtype(float))

x = np.linalg.solve(M, b)
print(f"solution: {x}")

# verification
v = [
    4*x[0] - 3*x[1] + 1*x[2],
    2*x[0] + 1*x[1] + 3*x[2],
   -1*x[0] + 2*x[1] - 5*x[2],
]
print(f"proof: {v == b}")


# calculating determinant
determinant_np = np.linalg.det(M)
determinant_cs = Matrix(matrix).determinant
print(f"determinants calculated with NumPy: {determinant_np}")
print(f"determinants calculated with custom class: {determinant_cs}")


# manual row reduction
# [TODO] update Matrix class with this functinoality

# elementary operations that can be done on matricies
#    Multiply any row by a non-zero number
#    Add two rows together and replace one with the result
#    Swap rows


def MultiplyRow(M, row_num, row_num_multiple):
    M_new = M.copy()
    M_new[row_num] = M_new[row_num] * row_num_multiple
    return M_new

def AddRows(M, row_num_1, row_num_2, row_num_1_multiple):
    M_new = M.copy()
    M_new[row_num_2] = row_num_1_multiple * M_new[row_num_1] + M_new[row_num_2]
    return M_new

def SwapRows(M, row_num_1, row_num_2):
    M_new = M.copy()
    M_new[[row_num_1, row_num_2]] = M_new[[row_num_2, row_num_1]]
    return M_new

A_system = np.hstack((M, b.reshape((3, 1))))
A_ref = SwapRows(A_system,0,2)
print(A_ref)
print("          vvvvv")
A_ref = AddRows(A_ref,0,1,2)
print(A_ref)
print("          vvvvv")
A_ref = AddRows(A_ref,0,2,4)
print(A_ref)
print("          vvvvv")
A_ref = AddRows(A_ref,1,2,-1)
print(A_ref)
print("          vvvvv")
A_ref = MultiplyRow(A_ref,2,-1/12)
print(A_ref)

# verification
x_3 = -2
x_2 = (A_ref[1,3] - A_ref[1,2] * x_3) / A_ref[1,1]
x_1 = (A_ref[0,3] - A_ref[0,2] * x_3 - A_ref[0,1] * x_2) / A_ref[0,0]

print(f"result: {[x_1, x_2, x_3]}")
print(f"proof: {[x_1, x_2, x_3] == x}")
