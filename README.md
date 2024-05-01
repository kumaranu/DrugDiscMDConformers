# DrugDiscMDConformers

A package to generate molecular conformer using SMILES for drug discovery applications.


-------------------------------------- Outline of the program ---------------------------------------------
Main script to run:
  make.bash

Supplementary scripts:
  1) main.py
  2) confgen_rdkit.py
  3) call_slurm.tcsh
  4) run.py
  5) sol_run.py
  6) getEnergy.py
  7) getEnergy_sol.py

Files and directories needed from the user:
  1) run.slurm
  2) sol_run.slurm
__________________________________________________________________________________________________________

-------------------------------------- Summary of the program ---------------------------------------------
All of the scripts contain comments to clarify their purpose in the program. A brief summary is provided below:
1) The bash script main.bash calls main.py
   - main.py fetches the PDB structure for the protein and extracts the ligand from it.
   - main.py also calls the function confgen from the module confgen_rdkit.py to generate the
     rdkit-based conformers.
2) Conformers are split into different xyz inputs and are stored in different directories, for example:
   |----molecular_files/
   |    |----rdkit_conformer/
   |    |    |----conf_0000/
   |    |    |    |----conf_0000.xyz

   and

   |----molecular_files/
   |    |----rdkit_conformer/
   |    |    |----sol_conf_0000/
   |    |    |    |----conf_0000.xyz
3) main.bash submits energy calculations for both the solvated and the non solvated versions are submitted for
   all the conformers in a batchwise manner using call_slurm.tcsh.
4) main.bash calls the python scripts getEnergy.py and getEnergy_sol.py to extract energies. The conformations are
   then sorted according to their energy.
5) main.bash submits energy calculations for the bound conformation of the ligand.
6) CREST calculations are also submitted independently inside molecular_files
__________________________________________________________________________________________________________
