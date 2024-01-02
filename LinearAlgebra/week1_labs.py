# introduction to numpy arrays

import numpy as np


# define arrays
a = np.array([1,2,3,4,5,6])
b = np.arange(3)
c = np.arange(1,100,20)
d = np.linspace(0,100,5)
e = np.linspace(0,100,5, dtype=int)
f = np.array(['string array'])
g = np.ones(3)
h = np.zeros(3)
i = np.empty(3)
j = np.random.rand(3)
k = np.array([[1,1.5,2], [2.5,3,3.5]])

# linspace and arange difference:
# https://stackoverflow.com/questions/62106028/what-is-the-difference-between-np-linspace-and-np-arange

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(a.dtype)
print(f.dtype)
print(g)
print(h)
print(i)
print(j)
print(k)
print(k.ndim)
print(k.shape)


# array operations
l = np.reshape(a, (2,3))
m = g + np.array([6,7,8])
n = np.array([11,12,13]) - g
o = l * 2
p = l * np.array([6,5,4,3,2,1]).reshape(2,3)
q = a[0]
r = a[:2]
s = l[1][2]

print(l)
print(l.shape)
print(l.size)
print(m)
print(n)
print(o)
print(p)
print(q)
print(r)
print(s)
