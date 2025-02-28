import numpy as np
import control.matlab as ct
import matplotlib.pyplot as plt

s = ct.tf('s')

G_s = 1/(s+1)

G_z = ct.c2d(G_s, 1)

print(G_z)