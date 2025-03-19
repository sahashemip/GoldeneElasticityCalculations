import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from utils import *

def compute_elastic_constant(strains, energies, axis, volume, quadratic_function):
    """Fits the quadratic function and computes the elastic constant."""
    parameters, _ = curve_fit(quadratic_function, strains, energies)
    fit_A, fit_B = parameters  # Unpack fitting parameters

    # Predefined elastic constants (eV/A3)
    c11 = 78.5620508475068
    c22 = 86.59810090977048

    if axis in [0, 1]:  # For x and y directions
        elastic_constant = fit_A / volume
    else:  # For xy-direction
        elastic_constant = ((fit_A / volume) - c11 - c22) / 2

    return elastic_constant, parameters


# Lattice parameters (in Angstrom)
ax, ay, d0 = 2.758, 4.713, 3.45
volume = ax * ay * d0 
    
AXIS = 1
if AXIS not in [0, 1, 10]:
    raise ValueError("Invalid AXIS value: {}. Must be 0 (x), 1 (y), or 10 (xy).".format(AXIS))

csvfile = 'data/strain_energy_{}axis.csv'.format(AXIS)
    
strains, energies = read_data(csvfile)
elastic_constant, fit_params = compute_elastic_constant(strains, energies, AXIS, volume, quadratic_function)

elastic_constant_eVA3 = elastic_constant

if AXIS==0:
    axis_label = 'x'
elif AXIS==1:
    axis_label = 'y'
else:
   axis_label = 'xy'

print("Elastic Constant along {}-axis:".format(axis_label))
print("{:.4f} eV/A3".format(elastic_constant))

plot_fit(strains, energies, fit_params)

