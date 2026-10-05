Andrew's profile ('spectrum_profile.pstat')

    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        60000    4.936    0.000   11.926    0.000 hamiltonian_diagonalization.py:167(transition_freqs_rabis_pops)
        60012    4.874    0.000    5.072    0.000 hamiltonian_diagonalization.py:53(hamiltonian_hz)
    119755    3.063    0.000    3.063    0.000 inhomogeneous_spectra.py:243(avg_spin_flip_probability)
            1    2.444    2.444    6.405    6.405 inhomogeneous_spectra.py:255(generate_cw_odmr_spectrum)
        60012    2.028    0.000    4.211    0.000 .venv\Lib\site-packages\scipy\linalg\_decomp.py:284(eigh)
        60000    1.581    0.000    3.385    0.000 .venv\Lib\site-packages\numpy\_core\numeric.py:2373(isclose)
    540115    1.433    0.000    1.433    0.000 {method 'reduce' of 'numpy.ufunc' objects}
        60012    0.967    0.000    6.453    0.000 hamiltonian_diagonalization.py:113(get_ordered_eigensystem)
            1    0.615    0.615   25.053   25.053 inhomogeneous_spectra.py:109(_generate_splittings_rabis_pops)


# Oct 3rd, 2026 

no vectorization yet, ~9s see spectrum_profile.pstat. First few profiles were running generate_cw_odmr twice accidentally. 


Vectorized hamiltonian_hz
- Just needed to change 
    ```e_x, e_y, e_z = e_vector_v_per_m``` to 
    ```e_x, e_y, e_z = (e_vector_v_per_m.T).reshape(3, ndim, 1, 1)```
    gives `e_i` (N, 1, 1) so that `e_i * S_j`is (N, 3, 3) 
    H_zeeman and H_zfs are (3, 3) so (N, 3, 3) + (3, 3) broadcasts to (N, 3, 3) as needed. 

    and also `np.conj(np.transpose(H_total))` to `H_total.conj().swapaxes(-1, -2)`


- verified accuracy of both vectorized and looped methods for construction and eigensystems (np.linalg.eigh(N, 3, 3)) gives eigensystem of shape (2, eighResults). 



- basic timing tests show 
    - Hamiltonian Construction vectorized = 542 μs ± 5.19 μs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
    - Hamiltonian Construction looped = 108 ms ± 908 μs per loop (mean ± std. dev. of 7 runs, 10 loops each)

    - Hamiltonian Diagonalization vectorized = 5.2 ms ± 33.7 μs per loop (mean ± std. dev. of 7 runs, 100 loops each)

    - Hamiltonian Diagonalization looped = 129 ms ± 840 μs per loop (mean ± std. dev. of 7 runs, 1 loop each)

- About a 200x speedup 

- need to adapt inputs to function to permit vectorization



# Oct 4th 

