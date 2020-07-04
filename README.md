# Spectral Estimators for Finite Noncommutative Geometries

Here is python code to calculate the spectral dimension and variance of a finite spectral triple. Some examples spectra are included for the fuzzy sphere (as given in [1] and [2]), fuzzy torus (as given in [3] and [4]) and random fuzzy spaces (as studied in [5] and [6]).



You will need to have the following python packages:

- Uncertainties: https://pythonhosted.org/uncertainties/
  - This is used when dealing with the random geometries. The spectra we have for the random geometries is actually an average. This average is taken over a large ensembled of Dirac operators from the simulation, and as such, it comes with some associated errors. The uncertainties package keeps track of how these errors propagate through the various calculations needed. 





## References

[1] Grosse, H., Prešnajder, P.: The Dirac operator on the fuzzy sphere. Lett. Math. Phys. 33, 171–181 (1995). https://doi.org/10.1007/BF00739805

[2] Barrett, J.W.: Matrix geometries and fuzzy spaces as finite spectral triples. J. Math. Phys. 56, 082301 (2015). https://doi.org/10.1063/1.4927224

[3] Gaunt, J.A.B.: Aspects of the fuzzy torus, *Ph.D Thesis* (2018)

[4] Barrett, J.W., Gaunt, J.: Finite spectral triples for the fuzzy torus, http://arxiv.org/abs/1908.06796, (2019)

[5] Barrett, J.W., Glaser, L.: Monte Carlo simulations of random non-commutative geometries. J. Phys. A: Math. Theor. 49, 245001, 27 (2016). https://doi.org/10.1088/1751-8113/49/24/245001

[6] Glaser, L.: Scaling behaviour in random non-commutative geometries. J. Phys. A: Math. Theor. 50, 275201–275219 (2016). https://doi.org/10.1088/1751-8121/aa7424
