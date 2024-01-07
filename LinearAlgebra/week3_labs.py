import numpy as np
from matrix_from_scratch import Matrix, MatrixOps
from plotter import plot_vectors

# Vector properties
#  norm - absolute length
#  direcation - arrow pointing to a direction
#
# In linear algebra, vectors always start at (0,0)

# Vector operations
v = np.array([[1], [3]])
w = np.array([[4], [-1]])

# Scalar multiplication
# Geometric meaning: stretching vector out
print(v * 3)
print(v * -2)

# vector summation
# Geometric meaning:
#   v and w construct a parallelagram,
#   where v+w is the diagonal
print(v + w)


# vector subtraction
# Geometric meaning:
#   v and -w (goes into the opposite direction of w)
#   construct a parallelagram,
#   where v-w is the diagonal
print(v - w)
# plot_vectors(
#     [v, w, -w, v + w, v - w],
#     [f"$v$", f"$w$", f"$-w$", f"$v + w$", f"$v - w$"],
#     ["black", "black", "black", "red", "red"],
# )


# vector norm
# Geometric meaning: absolute vector length
unit_v = np.array([[1], [0]])
print(np.linalg.norm(unit_v))
print(np.linalg.norm(w))


# dot product
# dot product is multiplication between vectors
# Geometric meaning: x * y = |x|*|y|*cos(t)
#   where t is the angle between x and y
x = [1, -2, -5]
y = [4, 3, -1]
Mx = Matrix(x)
My = Matrix(y)

MatrixOps(Mx, My, show=True).dot_product()
print(np.dot(x, y))



# Matrix Multiplication
a1 = [
    [2, 1],
    [-3, 2],
]
b1 = [
    [1, 3],
    [6, 2],
]
A1 = np.array(a1)
B1 = np.array(b1)
A2 = Matrix(a1)
B2 = Matrix(b1)

print(np.matmul(A1,B1))
print(MatrixOps(A2,B2).multiplication())
