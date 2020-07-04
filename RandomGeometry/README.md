# Random Fuzzy Spaces Spectra

These folders contain the ensemble-averaged eigenvalues for the random fuzzy spaces.

The simulation outlined and analysed in ([1] and [2]) can produce many Dirac operators $D_i$, as you can repeatedly sample the simulation after it has thermalised. These Dirac operators each have a set of eigenvalues $\{\lambda^{(i)}_j\}_{j=1}^{n}$ (where $n$ here is the total number of eigenvalues for the Dirac operator $D_i$). You can calculate the spectral dimension and spectral variance for each of the Dirac operators that you sample from the simulation and then analyse the resulting data. However, for a personal computer (as opposed to the high performance computer that these simulations are ran on), this is very resource heavy and can take a very long time to complete. So the data provided here is the weighted-average of the eigenvalues from the simulation. Thus for each Clifford-type and for each value of the coupling constant $g_2$, there is only one set of eigenvalues for each of the matrix sizes the simulation investigated. 

The consequences of taking this average were examined in [3].


## References
[1] Barrett, J.W., Glaser, L.: Monte Carlo simulations of random non-commutative geometries. J. Phys. A: Math. Theor. 49, 245001, 27 (2016). https://doi.org/10.1088/1751-8113/49/24/245001

[2] Glaser, L.: Scaling behaviour in random non-commutative geometries. J. Phys. A: Math. Theor. 50, 275201–275219 (2016). https://doi.org/10.1088/1751-8121/aa7424

[3] Barrett, J.W., Druce, P., Glaser, L.: Spectral estimators for finite non-commutative geometries. J. Phys. A: Math. Theor. 52, 275203, 33 (2019). https://doi.org/10.1088/1751-8121/ab22f8