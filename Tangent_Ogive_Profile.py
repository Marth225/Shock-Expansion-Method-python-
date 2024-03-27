import numpy as np
import matplotlib.pyplot as plt

rho = 1.5 # radius of the circle (in m)
L = 1 # length of the ogive profile (in m)

#base radius of the tangent ogive profile
R = rho - np.sqrt(rho**2 - L**2)
print(R)

#profile data calculation
x = np.linspace(0, L, 1000)
y = np.sqrt(rho**2 - (L-x)**2) + R-rho
print(len(x))


plt.plot(x, y, 'k', label = 'Tangent Ogive Profile', linewidth = 1.5)
plt.plot(x, -y, 'k',linewidth = 1.5)
plt.plot([x[999], x[999]], [y[999], -y[999]], 'k', linewidth = 1.5)
plt.plot([x[0], x[999]], [y[0], y[0]], 'k--', linewidth = 1.5)
plt.xlim([-0.2, 1.2])
plt.ylim([-1, 1])
#plt.grid(True)
plt.legend()
plt.show()