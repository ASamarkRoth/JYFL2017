import sys
import numpy as np
import matplotlib.pyplot as plt

def plot_decay(ll, x):
    for i in ll:
        operand = -i*x
        func = np.exp(operand)
        plt.plot(x, func, label = str(1/i) + ' ps')

def longest(args):
    longest_t = 0.0
    i = 1
    while i < len(args):
        z = float(args[i])
        if z > longest_t:
            longest_t = z
        i= i + 1
    return longest_t

def feeding(l,x):
    j = 1
    sum = 0
    op1 = -l[0]*x
    while j < len(l):
        op2 = -l[j]*x
        sum = sum + ((l[0]/l[j])*np.exp(op2)-np.exp(op1))
        j = j + 1
    f = np.exp(op1) + sum
    return -f/max(-f)

if __name__ == "__main__":
    # execute only if run as a script
    tt = longest(sys.argv)*1e-12
    t = np.arange(0.0, 2*tt, tt/1000)
    sum = 0.0
    lines = []
    lambdas = []
    i = 1
    while i < len(sys.argv):
        lambdas.append(1/(float(sys.argv[i])*1e-12))
        i = i + 1
    feeder = lambdas[1:]

    curve2 = feeding(lambdas, t)
    der = np.gradient(curve2)/(tt/1000)
    der2 = der/max(der)
    curve3 = feeding(feeder, t)

    diff = -curve2 + curve3
    max_diff_index = np.argmin(diff)
    difference = diff[max_diff_index]
    print ('Difference: ', str(difference))
    print ('Derivative: ', str(der[max_diff_index]))
    print ('Tau: ', str(difference/der[max_diff_index]) + ' s = ' + str((difference/der[max_diff_index])/1e-12) + ' ps')
    print ('at x=', str(t[max_diff_index]) + ' s')

    lines.append(plt.plot(t, diff, linewidth=3, label = 'Difference'))
    plt.plot(t, curve2, linewidth=3, label = 'State i')
    plt.plot(t, curve3, linewidth=3, label = 'Feeder')
    plt.xscale('log')
    plt.xlabel('time (s)')
    plt.ylabel('Intensity (arb. units)')
    plt.legend(loc = 'upper right')
    plt.grid(which='both')
    plt.show()
