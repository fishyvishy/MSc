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
            
- what is t2star_s?
- Abragam: Principles of Nuclear Magnetism (red and blue)


- possible to vectorize over nv axes as well?? 

        class InhomogeneousEnsembleParams:
            random_efields_crystal_v_per_m: np.typing.NDArray
            bfield_crystal_t: np.typing.NDArray
            nv_axes: np.typing.NDArray
            t2star_s: float
            zfs_hz: float = ZFS_HZ
            a_hf_hz: float = A_HF_HZ
            seed: int = 0
            hyperfine_structure: bool = False
            nonsecular_hf_terms: bool = False
            weighted_spectrum: bool = False  # Whether to weight the contribution of each NV transition frequency to the spectrum by MW matrix element.
            # TODO what is the use of field here compared to anywhere else in the code? It seems to be messing with the NDArray typing

            # What are these used for? 
            mw_polarization_crystal: np.typing.NDArray = field(
                default_factory=lambda: np.array([1.0, 0.0, 0.0])
            )
            bx_by_bz_fluctuations_factor: np.typing.NDArray = field(
                default_factory=lambda: np.array([1.0, 1.0, 1.0])
            )  # Factor by which to scale the bx, by, bz fluctuations respectively
            zfs_fwhm_hz: float = 0


- driving field comes from ...
- where does magnetic noise come from? Is this abragam again? Why cauchy distributed. 



### Notes 
- odmr_spectra_refactored/inhomogeous_spectra/InhomogenousTransitions._generate_splittings_rabis_pops is where bulk of calculation comes from 


### Questions 
- why not take the average electric field after generating the dataset? 
- why is mw_polarization contribution not included in hamiltonian_hz. contribution included in `hamiltonian_diagonalizatoin.transition_freqs_and_weights'. 
- Review how these transition frequnces and splittings calculated.
- ~~why called "b_vector_t" and not just "b_vector"~~ probably units (t = Tesla)


-  why need `np.isclose(np.diag(SZ), 0)` instead of just == in `transition_freqs_rabis_pops`

### Project Structure Examples 
- [qutip](https://github.com/qutip/qutip/tree/master)
- [pymatgen](https://github.com/materialsproject/pymatgen)


### Useful Readings 
- [Exact Breit-Rabi formulae for NV center](https://arxiv.org/html/2609.14964v1)