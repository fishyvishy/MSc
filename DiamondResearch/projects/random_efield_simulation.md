# Random Electric Field Simulation 

### Comments 
- Not exactly structured as a package rn. If goal is to share code as python project, then restructuring would help, if just for within lab simulations, then not really. 

- hard-coded paths can get messy (electric_field_distributions->constants-> OUTPUT_BASE_PATH = "/Users/lilianchildress/Documents/GitHub/RandomElectricFieldSimulations/output_files/")

- what is max_lattice_index in DiamondParams? (sets size of region in lattice we simulate over?)
- DiamondParams redefines of some values in constants.py 


- use mask of current nv, n positions so that newly generated ones don't get too close

### File Tree 
    electric_field_distributions 
        -> constants.py (not needed? DiamandParams data class has same constants)
            ? EPSILON_R_DIAMOND = 5.7 (dielectric constant. how well is it known?)
            ? PPM (concentration of defects)
            ? MIN_N_TO_NV_DISTANCE_CELLS = 12e-10/CONVENTIONAL_UNIT_CELL_SIDE_M
            ? MIN_NV_TO_NV_DISTANCE_CELLS = 12e-10/CONVENTIONAL_UNIT_CELL_SIDE_M

        -> electric_field_simulation_functions
            


### Project Structure Examples 
- [qutip](https://github.com/qutip/qutip/tree/master)
- [pymatgen](https://github.com/materialsproject/pymatgen)