import matplotlib.pyplot as plt
import numpy as np

def cantHarm(b, L, x):

    cbx = np.cos(b * x)
    sbx = np.sin(b * x)
    chbx = np.cosh(b * x)
    shbx = np.sinh(b * x)

    cbl = np.cos(b * L)
    sbl = np.sin(b * L)
    chbl = np.cosh(b * L)
    shbl = np.sinh(b * L)

    return chbx - cbx - (shbx - sbx)*(chbl + cbl)/(shbl + sbl)

def cantHarmT(h, w, t):
    return h * np.cos(w * t)


L = 5.0
b = np.pi / L * np.array([0.59686, 1.49418, 2.50025])
x = np.linspace(0, 5, 100)

h1 = cantHarm(b[0], L, x)
h2 = cantHarm(b[1], L, x)
h3 = cantHarm(b[2], L, x)

y1 = cantHarmT(h1, 1, 0)
y2 = cantHarmT(h1, 1, 0.3)
y3 = cantHarmT(h1, 1, 0.6)




plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.show()