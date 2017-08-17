import math
import numpy as np

#Constants:

amu = 931.5 #MeV/c^2
boltzmann = 8.617e-11 # MeV/K
hbarc = 0.19733e-10 # MeV cm

g_n = 2.
g_AA1 = 1.

#Mass excess: from 2003 table NNDC http://www.nndc.bnl.gov/masses/mass.mas03
ME = np.asarray([-76.5, -71.0, -66.8]) # MeV [Sn-132, Sn-133, Sn-134]
ME_n = 8.071 # MeV

ME_A = ME[0]
ME_A1 = ME[1]
Sn = ME_A + ME_n - ME_A1

A = 132.
muc2 = (A / (A+1)) * 1.0087*amu # last factor = neutron mass

N_n = 1.0e24 #per cm^.
T = 1.5e9 # K

print("Sn = ", Sn)

#Sn = 2.399

Ratio = N_n * (g_AA1/g_n) * hbarc**3 * (2*math.pi/(muc2*boltzmann*T))**(3./2.) * np.exp(Sn / (boltzmann*T))

print("Ratio 133/132: ", Ratio)

ME_A = ME[1]
ME_A1 = ME[2]
Sn = ME_A + ME_n - ME_A1
A = 133.
muc2 = (A / (A+1)) * 1.0087*amu # last factor = neutron mass

print("Sn = ", Sn)

#Sn = 3.631

Ratio = N_n * (g_AA1/g_n) * hbarc**3 * (2*math.pi/(muc2*boltzmann*T))**(3./2.) * np.exp(Sn / (boltzmann*T))

print("Ratio 134/133: ", Ratio)

mass = list()
Z = list()
Sn = list()

with open("sepn_frdm2012-ame2016.dat") as data:
    for lines in data:
        words = lines.split()
        #print(words)
        #mass.append()
        

