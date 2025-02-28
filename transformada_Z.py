import numpy as np
import matplotlib.pyplot as plt

size=int(input('digite el valor final de la sumatoria: '))

u_t=1

n = np.zeros(size)
y = np.zeros(size)


for i in range(0, size):
    n[i] = i
    y[i] =0.6321*u_t + (0.3679)*y[i-1]
    
plt.plot(n,y)
plt.show()
