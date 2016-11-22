import numpy as np
import matplotlib.pyplot as plt

n=100
t=np.arange(n)
a = np.random.randn(n)
print "a:\n", a
plt.plot(a)
# plt.show()

std=np.std(a)
print "std deviation:\n", std

b =np.random.rand(n)
print"b:\n", b
std_b = np.std(b)
print "std deviation of b:\n", std_b
plt.plot(b)
plt.show()
