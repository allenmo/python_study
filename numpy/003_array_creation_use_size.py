import numpy as np

zero_arr = np.zeros((3,4))
print "zero_arr:\n", zero_arr

zero_arr2 = np.zeros([3,4], dtype=np.int16)
print "zero_arr2:\n", zero_arr2

one_arr = np.ones((2,3,4), dtype=np.int8)
print "one_arr:\n", one_arr

empty_arr = np.empty((2,3))
print "empty_arr:\n", empty_arr

