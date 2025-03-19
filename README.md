# GoldeneElasticityCalculations
This repository contains scripts and step-wise instructions for calculating Young's modulus and Poisson's ratio using strain-energy relations.

## _Energy calculator_
Hotbit was used to compute the potential energy of atomic configurations. For more details on its features, see [`Hotbit`](https://github.com/pekkosk/hotbit).  

### I. Hotbit's repulsive interaction term
For the Au-Au repulsive pairwise potential, we considered both the Au dimer and bulk systems.
The dimer data was obtained using the energy curve method and for a single Au2 dimer data when **σ = 0.5** and **σ = 1**.
For the bulk system, we used a single data point with **σ = 1**.  
Here, **σ** is inversely proportional to the weighting factor in the fitting process.  

**Note:** By navigating to `"hotbit/examples/AuAu_parametrization"` and editing the `"AuAu.py"` script, the new potential was generated.

The updated `Au_Au_repulsion.par`, which is compatible with goldene, has been uploaded to this repository.
To use the fitted potential, specify the path in the calculator as follows:

```python
 Hotbit(tables = {'AuAu': 'path-to-Au_Au_repulsion.par'},**other_params)
```
The computed lattice constant is **2.756 &#197;**, which is close to the **2.684 &#197;** obtained using the [PBEsol](https://www.vasp.at/wiki/index.php/GGA) functional implemented in [VASP](https://www.vasp.at/).
For comparison, the [experimentally measured](https://www.nature.com/articles/s44160-024-00518-4) value is **2.62 &#197;**. 

### II. Potential energy vs. cell size
To ensure that the calculations are not affected by the parameters of the **DFTB** method, we use a **conventional cell**.
Specifically, we select a **rectangular-shaped cell** for studying strain-energy relationships.  
We set $$N_b = 5$$ and $$N_a = 2 N_b = 10$$, resulting in a system containing **100 Au atoms**.
This configuration provides an energy accuracy of **2 meV/atom**.

<p align="center">
  <img src="images/cellsize-energy-withunitcell.png" 
       alt="Cell Size vs. potential energy plot with a rectangular unit cell (top view)." 
       width="400">
</p>

A rectangular conventional cell allows for the study of strain effects along different edges.

### III. Bilayer goldene interlayer distance
In a **goldene sheet**, Au atoms experience **strong metallic bonding** within the layers and **weak van der Waals interactions** between the layers.
We investigated the **interlayer distance dependence** of the **potential energy** in a **bilayer goldene system**.
The system is made of a **10×10×1 triclinic cell** containing **200 Au atoms**, with a **vacuum size of 30 &#197;**.  
Our calculations indicate that the **optimal interlayer distance** is **3.45 &#197;** (which represents the effective thickness of the layer).

<p align="center">
  <img src="images/distance-energy-withcell.png" 
       alt="Interlayer distance vs. potential energy." 
       width="400">
</p>

`We are now confident that the Hotbit parameters are well-configured for accurately calculating energy in what follows.`
