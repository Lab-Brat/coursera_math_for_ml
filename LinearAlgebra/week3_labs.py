import numpy as np
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
#   v and -w (goes into the opposite direction of w)
#   construct a parallelagram,
#   where v-w is the diagonal
print(v - w)
plot_vectors(
    [v, w, -w, v + w, v - w],
    [f"$v$", f"$w$", f"$-w$", f"$v + w$", f"$v - w$"],
    ["black", "black", "black", "red", "red"],
)
