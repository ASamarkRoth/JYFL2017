import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pylab as plt

xi2 = list() #µm
m20 = list()
m22 = list()

with open("PH3_demo.dat") as file:
    for lines in file:
        words = lines.split()
        xi2.append(float(words[0]))
        m20.append(float(words[1]))
        m22.append(float(words[2]))


xi2 = np.asarray(xi2)
m20 = np.asarray(m20)
m22 = np.asarray(m22)

print("xi2 = ", xi2)
print("m20 = ", m20)
print("m22 = ", m22)

#HOW TO PLOT 2D HIST?

#Hist = np.2DHistogram(

plt.figure()
plt.plot(xi2, m20, marker="*",linestyle="None")
plt.yscale("log")
plt.show()
plt.close()


