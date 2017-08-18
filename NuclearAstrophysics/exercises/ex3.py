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

#this is the first one in the file
Z_current = 8

A_z = list()
Sn_z = list()

with open("sepn_frdm2012-ame2016.dat") as data:
    for lines in data:
        words = lines.split()
        if int(words[0]) <= Z_current:
            A_z.append(int(words[1]))
            Sn_z.append(float(words[2]))
        else:
            Z.append(Z_current)
            A.append(np.asarray(A_z))
            Sn.append(np.asarray(Sn_z))
            A_z = list()
            Sn_z = list()
            Z_current = int(words[0])
            A_z.append(int(words[1]))
            Sn_z.append(float(words[2]))
            

print("Len of A, Sn, Z = ", len(A), len(Sn), len(Z))

all_ratios = list()

for i, z in enumerate(Z):
    #Setting correct isotope chain
    iso_Sn = Sn[i]
    iso_A = A[i]

    ratio = list()

    SnRef = -boltzmann*T*np.log(0.5*N_n*((2*math.pi*hbarc**2)/(1.0087*amu*boltzmann*T))**(3./2.))

    idx = np.abs(SnRef-iso_Sn).argmin()
    ARef = iso_A[idx]

    print("Z, iso_A, Sn_ref = ", z, iso_A[idx], SnRef)

    #for j, sn in enumerate(iso_Sn):
    #    print("Mass = ", iso_A[j], " Sn = ", sn)

    for j, mass in enumerate(iso_A):
        muc2 = (mass / (mass+1)) * 1.0087*amu # last factor = neutron mass
        r = N_n * (g_AA1/g_n) * hbarc**3 * (2*math.pi/(muc2*boltzmann*T))**(3./2.) * np.exp(iso_Sn[j] / (boltzmann*T))
        #print("Mass = ", mass, "ratio = ", r)
        ratio.append(r)

    ratio = np.asarray(ratio)

    acc = ratio[idx]
    ratio[idx] = 1

    for j, r in enumerate(ratio[idx+1:]):
        acc = acc*r
        ratio[idx+j+1] = acc

    acc = ratio[idx]

    for j, r in enumerate(reversed(ratio[:idx])):
        #print(j,r)
        acc = acc/r
        ratio[idx-j-1] = acc

    all_ratios.append(ratio)

    #start = np.abs(125-iso_A).argmin()
    #end = np.abs(165-iso_A).argmin()

    #print(start, end)

    #plt.figure()
    #plt.plot(iso_A[start:end], ratio[start:end])
    #plt.yscale('log')
    #plt.show()
    #plt.close()

#Get maximum abundant
A_max = list()

for i, z in enumerate(Z):
    amax = A[i][all_ratios[i].argmax()]
    A_max.append(amax)

A_max = np.asarray(A_max)
print("A_max = ", A_max)
N_max = A_max - Z
print("N_max = ", N_max)

plt.figure()
plt.plot(range(len(Z)), Z)
plt.plot(N_max, Z)
#plt.yscale('log')
plt.show()
plt.close()

#Get abundance as a function of mass number
min_A = 100
max_A = 0

for j, a in enumerate(A):
    if a.min() < min_A:
        min_A = a.min()
    if a.max() > max_A:
        max_A = a.max()
print("min_A, max_A = ", min_A, max_A)

A_A = np.asarray(range(min_A, max_A+1))
Y_A = np.zeros(len(A_A))

print("Len A_A & Y_A = ", len(A_A), len(Y_A))

for j, a in enumerate(A):
    for i in range(len(a)):
        #print("j, i a[i] = ", j,i, a[i])
        index = np.abs(a[i]-A_A).argmin()
        #print(index)
        Y_A[index] = Y_A[index] + all_ratios[j][i]

plt.figure()
plt.plot(A_A, Y_A)
plt.yscale('log')
plt.show()
plt.close()