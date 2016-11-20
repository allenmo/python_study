import numpy as np
from numpy import pi

a = np.arange(10,30,5)
print "a:\n", a

b = np.arange(0,2,0.3)
print "b:\n", b

c = np.linspace(0, 2, 9)
print "c:\n", c

d = np.linspace(0, 2*pi, 100)
f = np.sin(d)
print "d:\n", d
print "f:\n", f
