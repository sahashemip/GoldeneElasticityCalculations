# GoldeneElasticityCalculations
This repository contains scripts and step-wise instructions for calculating Young's modulus and Poisson's ratio using strain-energy relations.

## _Energy calculator_
Hotbit was used to compute the potential energy of atomic configurations. For more details on its features, see [`Hotbit`](https://github.com/pekkosk/hotbit).  

For the Au-Au repulsive pairwise potential, we considered both the Au dimer and bulk systems.
The dimer data was obtained using the energy curve method and for a single Au2 dimer data when **σ = 0.5** and **σ = 1**.
For the bulk system, we used a single data point with **σ = 1**.  
Here, **σ** is inversely proportional to the weighting factor in the fitting process.  

The updated `Au_Au_repulsion.par`, which is compatible with goldene, has been uploaded to this repository.
To use the fitted potential, specify the path in the calculator as follows:

```python
tables = {'AuAu': 'path-to-Au_Au_repulsion.par'}
```
The computed lattice constant is **2.756 Å**, which is close to the **2.684 Å** obtained using the [PBEsol](https://www.vasp.at/wiki/index.php/GGA) functional implemented in [VASP](https://www.vasp.at/).
For comparison, the experimentally measured value is **2.62 Å**. 
