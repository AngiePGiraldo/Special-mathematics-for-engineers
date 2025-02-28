import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
import scipy as sp


a0,err0 = integrate.quad(lambda t: (t-3)**2, 0, 6)
a0,err0 = integrate.quad(lambda t: ((-9/2)*t + 36), 6, 8) #intervalo periodo de trozo de signal

T=10
a0 = (2/T)*a0

y = a0*0.5 
z = np.arange(0, 8, 0.001);#periodo total de la signal
fig = plt.figure()

K = 10#cantidad de coeficientes de la serie.
i = 1

while (i<=K):
    
    ai, erri = integrate.quad(lambda t: ((t-3)**2 * sp.cos(i*t), 0, 6) 
    ai = (1/sp.pi)*ai
    bi,erri =  integrate.quad(lambda t: ((t-3)**2 * sp.sin(i*t), 0, 6)
    bi = (1/sp.pi)*bi
    ai, erri = integrate.quad(lambda t: ((-9/2)*t + 36) * sp.cos(i*t), 6, 8) 
    ai = (1/sp.pi)*ai
    bi,erri =  integrate.quad(lambda t: ((-9/2)*t + 36) * sp.sin(i*t), 6, 8)
    bi = (1/sp.pi)*bi
    y += ai*np.cos(i*z) + bi*np.sin(i*z) + ai*np.cos(i*z) + bi*np.sin(i*z)
    i=i+1
    
plt.plot(z,y)
plt.grid()
plt.show()

#t = np.arange(0, 6, 0.01)  
#u1 = lambda t: np.piecewise((t-3)**2, t>=0, [0,6])
#u2 = lambda t: np.piecewise(((-9/2)*t + 36), t>=6, [6,8])
#ui = u2(t)-u1(t)

    
#plt.figure()
#plt.grid()
#plt.plot(t,ui)

