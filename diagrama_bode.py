# -*- coding: utf-8 -*-
"""
Created on Sat May 20 03:44:56 2023

@author: paola
"""

from scipy import signal
import matplotlib.pyplot as plt

sys = signal.TransferFunction([1], [1, -1])
w, mag, phase = signal.bode(sys)

plt.figure()
plt.semilogx(w, mag)    # Bode magnitude plot
plt.figure()
plt.semilogx(w, phase)  # Bode phase plot
plt.show()