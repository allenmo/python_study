import numpy as np

x = np.arange(6)
x = x.reshape((2,3))
print "x:\n", x

x_zeros_like = np.zeros_like(x)
print "x_zeros_like:\n", x_zeros_like

y = np.arange(3, dtype=np.float)
print "y:\n", y

y_zeros_like = np.zeros_like(y)
print "y_zeros_like:\n", y_zeros_like

j = np.arange(10).reshape(2,5).reshape(10)
print "j:\n", j

j_ones_like = np.ones_like(j)
print "j_ones_like:\n", j_ones_like
