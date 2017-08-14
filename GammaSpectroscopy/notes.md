#Lecture notes Gamma Spectroscopy - Jyväskylä#

##Lecture 1##

* Z^2/A: facilitation factor ~ 40 for instability against fission
* s p d f g (0 1 2 3 4) of orbital angular momentum (_L_). Sharp, Principal, Diffuse and Fundamental
* Nuclear excitations:

	* Rotational bands ~ tens of keV
	* Vibrational excitations
	* Proton separations at binding energy ~ 8 MeV
	* I.e. 0->8 MeV Gamma rays

**Clever units of constants can be found in slides!**

* Collective = rotational excitations !?
* 511 keV peak wider. Due to energy distribution of positron at annihilation.
* sigma_ph prop. Z^5
* sigma_c prop. Z
* Momentum 4-vectors can preferably be used in the derivation of the _Compton Scattering_ formula.
* _Point function_ of a single gamma ray presents the entire spectrum with all its features.
* Energy of thermal electron ~ 1/40 eV
* E_bandgap in Ge @ 77 K is 2.96 eV

**Timing resolution:**

* Count rate abilities. Better time resolution larger count rate possible.
* Ability to better distinguish cascades with lifetimes on the order of ns.

* Crystal orientation affects the time collection. I.e. pulse shapes.
* Drift velocity: 10^7 cm/s (saturated)
* Rule of thumb: 10 000 counts/s is maximum

##Lecture 2##

Scintillator pros: 

* Cheap
* Construct it in any possible shapes
* Could be liquid
* Large efficiency
* Time resolution

* Deteriorate: become progressively worse
* Heavy metal shield in front to remove x-rays. This could be multiple layers where each is to absorb the other elements x rays. 
* c = 1 foot per ns
* Coincidence window typically 100 ns
	
	* 10 000 Bq -> Probability of random = 0.1 %

* Gamma1 Gamma2 matrix: fill in every double mirror and if triple three doubles ...
* OBS: efficiency corrections
* High fold = nbr of coincidences
* Fold £ binomial distr.
* Throw away randoms in hyper-cube if no neighbours
* High granularity = many detectors measuring each a specific Gamma.
* Peak-to-total ~ up to 60-70 %.
* Resolving power = as large as possible ?= fold

##Lecture 3##

* One could not see transitions connecting super-deformed bands since these are E > 5 MeV. That is why not found still.
* Band: E prop. j(j+1) -> equal spacing
* Quadrupole rotating = electric quadrupole radiation
* Photon angular momentum: 1hbar
* Why E1 pretty rare in nuclei? Need changing dipole moment, i.e. center of charge is not in middle (even spatial distr. of nucleons).
* Quantisation axis: Defined e.g. as an emission of photon.
* Clebsch-Gordan coefficients: change of good quantum numbers for addition of angular momenta
* Momentum conservation: Low angular momentum of radiation -> anti-aligned I 
* Photon = positive parity. L parity: (-1)^L
* Magnetic dipole moment are common, i.e. M1.
* M0 not allowed since photon has positive parity
* Co-60 has angular correlation!
* Obs every state has substates: I = 3; m = ±3, ±2, ±1, 0
* Photon has two polarisation states; i.e. m = ± 1.

##Lecture 4##
With photon on quantisation axis: L = r x p -> Lz != 0. This is due to the two polarisation states of the photon. But this changes when one photon determines the quantisation axis for a subsequent. And gamma2 delta m = ±1, 0.

* The method presented holds also for alpha-gamma angular correlations BUT one needs to be careful with selection rules for the alpha particle.
* To perform angular correlation studies you need a lot of data because the difference in intensity is not so large. 
* IMPORTANT: differ between angular correlation and angular distribution.
* If you populate all substates of your three states equally probable then we will have an isotropical emission (no correlation). WARNING: Clebsch-Gordan!
* OBS: If you have cascades and you only have detectors covering certain angles then you need to correct for this to obtain the correct intensity distr.

**Mixing ratio:**

* Prob. of M1/E2. 
* delta = transition matrix element with M1 operator over operator E2. It has a sign.
* If this is the case then it will affect the angular correlation.
* If one measures: delta = 0. -> E1 transition and this determines parity of states.
* Beam -> You have an anisotropical distr. initially.
* You can distinguish stuff from angular distr.

* Parity assignements are mostly "guess-work" but based on some arguments from theory or measurements of delta or similar.

* Disentangle many gammas: how many were there? Where was interaction point? ---> Tracking!
* Preamps. AGATA deliberately slow to measure rise times.
* Rise time parameters have been decided: t30, t90 ... See slide
* Ofc. crystal axis plays a role in charge collection.
* "Calculation of pulse shapes has not worked yet"
* Voxel = volume pixel

##Lecture 5##

* SAGE spectrometer for gamma internal conversion coincidence measurements
* Auger = competition atomic deexcitation
* alpha > 1, IC dominates
* IC increase for lower transition energies. Since, gamma transition increases.
* Only IC for E0, otherwise always competition.
* By looking at electron spectrum and IC peak intensities it is possible to deduce multipole of transition.
* Delta electrons: beam on target and atom electrons emitted!
* Suppression of these delta electrons: negative electric potential on detector.
* Gate on subsequent gammas -> Clean e- spectrum
* Magnetic field for detection of electron
* Noise in Ge?
* Solenoidal field = divergence = 0 of vector field 

SHE

* Velocity of inner e- prop. cZ/137
* Limits of atomic shell: Z = 172
* Facility cut-off: Z^2/A
* Lifetime limit: 10^14 s from chemical reaction H+H->H2
