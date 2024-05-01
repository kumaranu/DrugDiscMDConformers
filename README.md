# DrugDiscMDConformers

DrugDiscMDConformers is a package designed to generate molecular conformers using SMILES for drug discovery applications.

## Outline of the Program
### Main Script:
- `make.bash`

### Supplementary Scripts:
1. `main.py`
2. `confgen_rdkit.py`
3. `call_slurm.tcsh`
4. `run.py`
5. `sol_run.py`
6. `getEnergy.py`
7. `getEnergy_sol.py`

### Files and Directories Needed from the User:
1. `run.slurm`
2. `sol_run.slurm`

## Summary of the Program
The package comprises several scripts, each with a specific purpose, aimed at facilitating the generation of molecular conformers and subsequent energy calculations. Here's a brief overview:

1. **Main Script Execution**:
   - The bash script `main.bash` invokes `main.py`, which retrieves the PDB structure for the protein and extracts the ligand.
   - `main.py` utilizes the `confgen` function from `confgen_rdkit.py` to generate conformers using rdkit.

2. **Conformer Generation**:
   - Conformers are segregated into different xyz inputs and stored in distinct directories, such as `molecular_files/rdkit_conformer/`.

3. **Energy Calculations**:
   - Energy calculations, for both solvated and non-solvated conformers, are submitted batchwise using `call_slurm.tcsh`.
   - Python scripts `getEnergy.py` and `getEnergy_sol.py` are employed to extract energies and sort conformations based on their energy.

4. **Bound Ligand Conformation**:
   - Energy calculations for the bound conformation of the ligand are also submitted.

5. **CREST Calculations**:
   - CREST calculations are independently submitted inside the `molecular_files` directory.

This package streamlines the process of molecular conformer generation and energy calculations, providing a comprehensive toolkit for drug discovery endeavors.

