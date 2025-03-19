import numpy as np

def check_xy_orthogonality(lattice, tol = 1e-4):
    """
    Checks if the in-plane (xy) axes of a 3x3 lattice matrix are orthogonal.

    Parameters:
    - lattice (np.ndarray): A 3x3 matrix representing the lattice vectors.
    - tol (float): Tolerance for numerical precision errors (default: 1e-4).

    Returns:
    - bool: True if the xy-plane vectors are orthogonal, False otherwise.

    Raises:
    - ValueError: If input lattice is not a 3x3 matrix.
    """

    if not isinstance(lattice, np.ndarray) or lattice.shape != (3, 3):
        raise ValueError("Input must be a 3x3 numpy array.")

    v_x = lattice[:3, 0]
    v_y = lattice[:3, 1]

    dot_product = np.dot(v_x, v_y)

    return abs(dot_product) < tol

def generate_strain_list(absolute_value = 0.1, step = 0.01):
    """
    Generates a list of strain values symmetrically ranging
    from -absolute_value to +absolute_value.

    Parameters:
    - absolute_value (float): The maximum absolute strain value.
    - step (float): The step size between strain values.

    Returns:
    - list: A list of strain values.

    Raises:
    - ValueError: If absolute_value is negative.
    - Warning: If absolute_value exceeds 0.2.
    """
    if absolute_value > 0.2:
        print("Warning: This value brings more than 20'%' strain!")

    if absolute_value < 0.0:
        raise ValueError("Error: absolute_value must be non-negative.")

    return np.arange(-absolute_value, absolute_value + step, step).tolist()

def func(x, a, b):
    """
    Compute a quadratic function of the form: f(x) = a * x^2 + b.
    
    Parameters:
    x (float or int): The input value.
    a (float or int): Quadratic coefficient.
    b (float or int): Constant term.
    
    Returns:
    float: The computed function value.
    """
    return float(a) * float(x)**2 + float(b)

def save_strain_energy_values(filename, strain, energy):
    """
    Saves strain and energy values to a CSV file.
    
    Parameters:
    filename (str): Name of the output CSV file (without or with .csv extension).
    strain (array-like): Array of strain values.
    energy (array-like): Array of potential energy values.

    Returns:
    None
    """
    strain = np.asarray(strain)
    energy = np.asarray(energy)

    try:
        np.savetxt(filename, 
                   np.column_stack((strain, energy)), 
                   delimiter=",", 
                   header="Strain,Potential Energy(eV)", 
                   fmt="%.6f", 
                   comments="")
        
        print("Data successfully saved to '{}'".format(filename))

    except IOError as e:
        print("Error saving file '{}': {}".format(filename, e))


def apply_1d_strain(cell, strain_value, axis = 0):
    """
    Applies a 1D strain to a 3x3 transformation matrix along the specified axis.

    Parameters:
    - cell (np.ndarray): A 3x3 numpy array representing the cell matrix.
    - strain_value (float): The strain to apply along the given axis.
    - axis (int): The axis along which to apply the strain (0, 1, or 2).

    Returns:
    - np.ndarray: The deformed matrix after applying the strain.

    Raises:
    - ValueError: If the axis is not in {0, 1, 2}.
    """

    if axis not in {0, 1, 2}:
        raise ValueError("Invalid axis value. Allowed values: 0, 1, 2.")

    identity_matrix = np.eye(3)

    strain_matrix = np.zeros((3, 3))
    strain_matrix[axis, axis] = strain_value

    deformation_matrix = identity_matrix + strain_matrix

    return np.dot(deformation_matrix, cell)

def apply_xy_strain(cell, strain_value):
    """
    Applies an xy-plane strain to a 3x3 transformation matrix.

    Parameters:
    - cell (np.ndarray): A 3x3 numpy array representing the cell matrix.
    - strain_value (float): The strain value to be applied.

    Returns:
    - np.ndarray: The deformed matrix after applying the strain.

    Raises:
    - ValueError: If `cell` is not a valid 3x3 matrix.
    """

    if not isinstance(cell, np.ndarray) or cell.shape != (3, 3):
        raise ValueError("Input `cell` must be a 3x3 numpy array.")

    identity_matrix = np.eye(3)

    strain_matrix = np.zeros((3, 3))
    strain_matrix[0, 0] = strain_value  
    strain_matrix[1, 1] = strain_value 
    strain_matrix[0, 1] = strain_value / 2 
    strain_matrix[1, 0] = strain_value / 2 

    deformation_matrix = identity_matrix + strain_matrix

    return np.dot(deformation_matrix, cell)
