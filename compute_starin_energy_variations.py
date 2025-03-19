import sys
import os

from ase.io import read
from hotbit import Hotbit

sys.path.append(os.path.abspath('./src'))
import utils


input_file_name = 'POSCAR-goldene.vasp'
#
try:
    goldene_puc = read(input_file_name)

    if goldene_puc is None:
        raise ValueError("Input NOT defined.")
    cell = goldene_puc.get_cell()

    if not utils.check_xy_orthogonality(cell):
        raise ValueError("Invalid cell structure: The cell must be orthogonal.")

except Exception as e:
    raise IOError("Error in reading input file: {}".format(e))


maximum_strain = 0.08 # must be positive e.g. 8%    
strain_values = utils.generate_strain_list(
    absolute_value=maximum_strain, step=0.01)

AXIS = 10   # it takes a value of 0, 1, or 10
if AXIS not in [0, 1, 10]:
    raise ValueError("Invalid axis value: {}. Must be 0 (x-direction), 1 (y-direction), 10 (xy-directions).".format(AXIS))


energy_values = []
for strain_value in strain_values:
    #supercell size was optimized before!
    goldene_sc = goldene_puc.repeat([10, 5, 1])
    #apply strain 1d or 2d
    cell = goldene_sc.get_cell()
    if AXIS==0 or AXIS==1:
        cell_new = utils.apply_1d_strain(cell, strain_value, axis=AXIS)
    else:
        cell_new = utils.apply_xy_strain(cell, strain_value)
    goldene_sc.set_cell(cell_new, scale_atoms=True)

    calc = Hotbit(
        SCC=True,
        tables={'AuAu': './Au_Au_repulsion.par'},
        txt="None",
        gamma_cut=6
        )
    
    goldene_sc.set_calculator(calc)

    energy = goldene_sc.get_potential_energy()
    energy_values.append(energy)
    print("Strain: {:.3f}, Potential Energy: {:.6f} eV".format(strain_value, energy))

utils.save_strain_energy_values(
    'data/strain_energy_{}axis.csv'.format(AXIS),
    strain_values,
    energy_values)