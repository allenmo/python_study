import numpy as np
a = np.arange(12).reshape(3, 4)
print "a:\n", a

print "a.shape:", a.shape
print "a.ndim:", a.ndim
print "a.dtype.name:", a.dtype.name
print "a.itemsize:", a.itemsize
print "a.size:", a.size
print "type(a):", type(a)

b = np.array([6,7,8])
print "b:", b
print "type(b):", type(b)
