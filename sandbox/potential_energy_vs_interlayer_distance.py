import numpy as np
import matplotlib.pyplot as plt
from ase import Atoms
from hotbit import Hotbit

#predefined
CELL_AU = [
    [2.7202854156,  0.0000000000,  0.0000000000],
    [-1.3543521268,  2.3591699937,  0.0000000000],
    [0.0000000000,  0.0000000000, 30.0000000000]
]

def compute_potential_energy(distance):
    """
    Computes the potential energy for a given interlayer distance.
    """
    
    positions = [
        [0.000000000, 0.000000000, 0],  
        [0.682966644, 1.179584997, distance]
    ]
    
    atoms = Atoms('Au2', positions=positions, cell=CELL_AU, pbc=True)
    goldene = atoms.repeat([10, 10, 1])
    
    calc = Hotbit(
        SCC=True,
        tables={'AuAu': '../Au_Au_repulsion.par'},
        txt="None",
        gamma_cut=5,
    )
    
    goldene.set_calculator(calc)
    return goldene.get_potential_energy()


#computing energy for distances
DISTANCES = [2.8, 3.0, 3.2, 3.3, 3.35, 3.4, 3.45, 3.5, 3.6]
ENERGY_VALUES = []

for d in DISTANCES:
    energy = compute_potential_energy(d)
    ENERGY_VALUES.append(energy)
    print(r'Distance: {:.3f} Angstrom, Potential Energy: {:.6f} eV'.format(d, energy))


#plotting
fig, ax = plt.subplots(figsize=(3.3, 2.5))

ax.plot(DISTANCES, ENERGY_VALUES, 'bs--', linewidth=1.2)

ax.set_ylim([-831, -820])
ax.set_xlabel(r'Interlayer Distance ($\mathrm{\AA}$)', fontsize=10)
ax.set_ylabel(r'Potential Energy (eV)', fontsize=10)

ax.tick_params(direction='in', length=4, width=1, labelsize=10)
ax.tick_params(which='minor', direction='in', length=2, width=0.8)

plt.savefig("../images/distance-energy.png", dpi=600, format="png", bbox_inches="tight")

