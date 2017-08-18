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

A_t = list()
t = list()
Z_t = list()

A_z = list()
t_z = list()

Z_current = 8

with open("Moller2003_halflives.dat") as data:
    for lines in data:
        words = lines.split()
        if int(words[0]) <= Z_current:
            A_z.append(int(words[1]))
            t_z.append(float(words[2]))
        else:
            Z_t.append(Z_current)
            A_t.append(np.asarray(A_z))
            t.append(np.asarray(t_z))
            A_z = list()
            t_z = list()
            Z_current = int(words[0])
            A_z.append(int(words[1]))
            t_z.append(np.log(2)/float(words[2]))
            
print("t: Len of A, t, Z = ", len(A_t), len(t), len(Z_t))

all_ratios = list()

for i, z in enumerate(Z):
    #Setting correct isotope chain
    iso_Sn = Sn[i]
    iso_A = A[i]

    ratio = list()

    SnRef = -boltzmann*T*np.log(0.5*N_n*((2*math.pi*hbarc**2)/(1.0087*amu*boltzmann*T))**(3./2.))

    idx = np.abs(SnRef-iso_Sn).argmin()
    ARef = iso_A[idx]

    #print("Z, iso_A, Sn_ref = ", z, iso_A[idx], SnRef)

    #for j, sn in enumerate(iso_Sn):
    #    print("Mass = ", iso_A[j], " Sn = ", sn)

    for j, mass in enumerate(iso_A):
        muc2 = (mass / (mass+1)) * 1.0087*amu # last factor = neutron mass
        r = N_n * (g_AA1/g_n) * hbarc**3 * (2*math.pi/(muc2*boltzmann*T))**(3./2.) * np.exp(iso_Sn[j] / (boltzmann*T))
        #print("Mass = ", mass, "ratio = ", r)
        ratio.append(r)

    ratio = np.asarray(ratio)

    NSum = np.sum(ratio)

    ratio = ratio/NSum

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
#print("A_max = ", A_max)
N_max = A_max - Z
#print("N_max = ", N_max)

plt.figure()
plt.plot(range(len(Z)), Z)
plt.plot(N_max, Z)
#plt.yscale('log')
#plt.show()
plt.close()

#Correct for beta rates

for j, z in enumerate(Z):
    amax = A[j][all_ratios[j].argmax()]
    print("Amax = ", amax)
    if z > 109:
        all_ratios[j] = np.zeros(len(all_ratios[j]))
    elif any(A_t[j] == amax):
        ind_A = np.abs(amax - A_t[j]).argmin()
        all_ratios[j] = all_ratios[j]/t[j][ind_A]
        print("lambda = ", t[j][ind_A])
    else:
        all_ratios[j] = np.zeros(len(all_ratios[j]))

#for j, z in enumerate(Z):
#    for i, a in enumerate(A[j]):
#        #print("j, i, z = ", j,a,z)
#        print("Z = ", z)
#        if z > 109:
#            all_ratios[j][i] = 0
#        elif any(A_t[j] == a):
#            ind_A = np.abs(a - A_t[j]).argmin()
#            #print(ind_A)
#            #print("This A exists: ", a, " with t = ", t[j][ind_A], " and ratio = ", all_ratios[j][i])
#            all_ratios[j][i] = all_ratios[j][i]/t[j][ind_A]
#        else:
#            #print("This A NOT exists: ", a, " removing ...")
#            #print("Z = ", z)
#            all_ratios[j][i] = 0

#print("Z_t = ", Z_t)
#print("A_t = ", A_t)


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
