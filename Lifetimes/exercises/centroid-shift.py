import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import math

def read_file(arr_x, arr_y, ifile):
    with open(ifile, 'r') as f:
        for line in f:
            a = line.split()
            arr_y.append(float(a.pop()))
            arr_x.append(float(a.pop()))
    f.close()

def norm_dist(x,a,x0,sigma):
    return a*np.exp(-(x-x0)**2/(2*sigma**2))

def fit(datafile, a1, a2):
    x1, y1 = [], []
    read_file(x1, y1, datafile)
    popt, cov = curve_fit(norm_dist, x1, y1, p0 = (1, a1, a2))
    print ('Width: ', str(abs(popt[2])))
    print ('Centroid: ', str(popt[1]))
    plt.plot(x1, norm_dist(x1, *popt), label = 'Fit')
    plt.plot(x1, y1, drawstyle = 'steps', label = 'Data')
    return float(str(popt[1]))

if __name__ == "__main__":
    # execute only if run as a script
    mu1, mu2 = 16500, 15500
    sigma1, sigma2 = 5000, 5500
    c1 = fit("cs1.dat", float(mu1), float(sigma1))
    c2 = fit("cs2.dat", float(mu2), float(sigma2))
    plt.xlabel('time (ps)')
    plt.ylabel('Intensity (arb. units)')
    plt.legend(loc = 'lower left')
    plt.show()

    print("Final result = ", (c1-c2)/2)
