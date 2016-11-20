import numpy as np

a = np.array([2,3,4])
print "a:", a
print "type(a):", type(a)
print "a.dtype:", a.dtype

b = np.array([1.2, 3.5, 5.1])
print "b.dtype:", b.dtype

# c = np.array(1,2,3,4) #WRONG
c = np.array([1,2,3,4]) #RIGHT
print "c:", c
d = np.array((1,2,3,4)) #RIGHT
print "d:", d

a1d = np.array([1,2,3]) 		#sequences to 1 dimensional array
a2d = np.array([[1,2,3],[4,5,6]])	#sequences of sequences into 2 D array
a3d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]) #3D array
print "a1d(%dD):\n" %a1d.ndim, a1d, "\n"
print "a2d(%dD):\n" %a2d.ndim, a2d, "\n"
print "a3d(%dD):\n" %a3d.ndim, a3d, "\n"

e = np.array([[1,2],[3,4]], dtype=complex)
print "e:\n", e
