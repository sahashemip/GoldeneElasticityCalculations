from ase.io import read
from hotbit import Hotbit
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Enter path to your geometry file.
# Theacceptable formats can be found here:
# https://wiki.fysik.dtu.dk/ase/ase/io/io.html

goldene_puc = read('../POSCAR-goldene.vasp')
if goldene_puc is None:
    raise ValueError("goldene_puc could not be loaded. Check the input file.")

energy_values = []
bsizes = [1, 2, 3, 4, 5, 6, 7, 8, 9]
bvector_length_in_Angstrom = 4.718
blength = [x * bvector_length_in_Angstrom for x in bsizes]

for bsize in bsizes:
    goldene_sc = goldene_puc.repeat([2 * bsize, bsize, 1]) #makes a supercell
    number_of_atoms = goldene_sc.get_number_of_atoms()
    
    calc = Hotbit(SCC=True,
                  tables={'AuAu': '../Au_Au_repulsion.par'},
                  txt="None",
                  gamma_cut=5,
                  )
    
    goldene_sc.set_calculator(calc)

    pot_energy = goldene_sc.get_potential_energy()
    pot_energy_per_atom = pot_energy / number_of_atoms
    energy_values.append(pot_energy_per_atom)
    
    print("Natoms: {:.3f}, Nb: {:.3f}, Potential Energy: {:.6f} eV/atom".format(
        number_of_atoms, bsize, pot_energy_per_atom))

fig, ax = plt.subplots(figsize=(3.3, 2.5))  

ax.plot(blength , energy_values, 'go-', linewidth=1.5)

ax.set_xlabel(r'Y-axis Length ($\mathrm{\AA}$)', fontsize=10)
ax.set_ylabel(r'Potential Energy (eV/atom)', fontsize=10)

ax.set_ylim(-4.3, -3.3)

ax.xaxis.set_major_locator(ticker.MultipleLocator(10))   
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1)) 

ax.yaxis.set_major_locator(ticker.MultipleLocator(0.2)) 
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.05)) 

ax.tick_params(direction='in', length=6, width=1, labelsize=10) 
ax.tick_params(which='minor', direction='in', length=3, width=0.8)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.savefig("../images/cellsize-energy.png",
            dpi=600,
            format="png",
            bbox_inches="tight")
