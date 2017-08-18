import math
import numpy as np

import matplotlib.pyplot as plt

#Constants:

amu = 931.5 #MeV/c^2
boltzmann = 8.617e-11 # MeV/K
hbarc = 0.19733e-10 # MeV cm

g_n = 2.
g_AA1 = 1.

N_n = 1.0e24 #per cm^.
T = 1.5e9 # K

A = list()
Sn = list()
Z = list()

with open("sepn_frdm2012-ame2016.dat") as data:
    for lines in data:
        words = lines.split()
        #print(words)
        if words[0] == '50':
            Z.append(int(words[0]))
            A.append(int(words[1]))
            Sn.append(float(words[2]))
        
#for j in range(len(A)):
#    print("A, Sn = ", A[j], Sn[j])

ratio = list()

total = 1
start = 0

SnRef = -boltzmann*T*np.log(0.5*N_n*((2*math.pi*hbarc**2)/(1.0087*amu*boltzmann*T))**(3./2.))

Sn = np.asarray(Sn)

idx = np.abs(SnRef-Sn).argmin()
ARef = A[idx]

print("A = ", A[idx])

print("Sn ref = ", SnRef)

for j, sn in enumerate(Sn):
    print("Mass = ", A[j], " Sn = ", sn)

for j, mass in enumerate(A):
    muc2 = (mass / (mass+1)) * 1.0087*amu # last factor = neutron mass
    r = N_n * (g_AA1/g_n) * hbarc**3 * (2*math.pi/(muc2*boltzmann*T))**(3./2.) * np.exp(Sn[j] / (boltzmann*T))
    print("Mass = ", mass, "ratio = ", r)
    ratio.append(r)

ratio = np.asarray(ratio)

acc = ratio[idx]
ratio[idx] = 1

for j, r in enumerate(ratio[idx+1:]):
    acc = acc*r
    ratio[idx+j+1] = acc

acc = ratio[idx]

for j, r in enumerate(reversed(ratio[:idx])):
    print(j,r)
    acc = acc/r
    ratio[idx-j-1] = acc

N_n = 1.0e28 #per cm^.
T = 1.5e9 # K

ratio2 = list()

total = 1
start = 0

SnRef = -boltzmann*T*np.log(0.5*N_n*((2*math.pi*hbarc**2)/(1.0087*amu*boltzmann*T))**(3./2.))

Sn = np.asarray(Sn)

idx = np.abs(SnRef-Sn).argmin()
ARef = A[idx]

print("A = ", A[idx])

print("Sn ref = ", SnRef)

for j, sn in enumerate(Sn):
    print("Mass = ", A[j], " Sn = ", sn)

ratio2 = list()

for j, mass in enumerate(A):
    muc2 = (mass / (mass+1)) * 1.0087*amu # last factor = neutron mass
    r = N_n * (g_AA1/g_n) * hbarc**3 * (2*math.pi/(muc2*boltzmann*T))**(3./2.) * np.exp(Sn[j] / (boltzmann*T))
    print("Mass = ", mass, "ratio = ", r)
    ratio2.append(r)

ratio2 = np.asarray(ratio2)

acc = ratio2[idx]
ratio2[idx] = 1

for j, r in enumerate(ratio2[idx+1:]):
    acc = acc*r
    ratio2[idx+j+1] = acc

acc = ratio2[idx]

for j, r in enumerate(reversed(ratio2[:idx])):
    print(j,r)
    acc = acc/r
    ratio2[idx-j-1] = acc

A = np.asarray(A)
start = np.abs(125-A).argmin()
end = np.abs(165-A).argmin()

print(start, end)


plt.figure()
plt.plot(A[start:end], ratio[start:end])
plt.plot(A[start:end], ratio2[start:end])
plt.yscale('log')
plt.show()
plt.close()
