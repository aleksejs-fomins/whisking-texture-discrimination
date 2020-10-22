import matplotlib.pyplot as plt
import numpy as np

def w1(x, L, k):
    return (L-x)/k - (x/2)*(L**2 - x**2 / 3) + L**3 / 3

L = 5
x = np.linspace(0, 5, 100)
y = w1(x, L, 1.0)

plt.plot(x, y)
plt.show()