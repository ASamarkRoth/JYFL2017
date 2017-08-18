import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pylab as plt

def ExpFunc(x, a, l):
    return a*np.exp(-x/l)

distance = list() #µm
intensity = list()
error = list()

with open("decay_curve.txt") as file:
    for lines in file:
        words = lines.split()
        distance.append(float(words[0]))
        intensity.append(float(words[1]))
        error.append(float(words[2]))


distance = np.asarray(distance)
intensity = np.asarray(intensity)
error = np.asarray(error)

print("distance = ", distance)
print("intensity = ", intensity)
print("error = ", error)

estimates, covar = curve_fit(ExpFunc, distance, intensity, p0=None)

#print("tau = ", estimates[0])

c = 3e8

v = 0.043*c

tau = np.mean(distance / v) * 1e-6

print("tau = ", tau, "s")

plt.figure()
plt.plot(distance, intensity, marker="*",linestyle="None")
plt.yscale("log")
plt.show()
plt.close()


