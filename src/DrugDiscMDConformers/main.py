from pymol import cmd
import sys
from openbabel import openbabel
import confgen_rdkit

###############################################################################################
#                                                                                             #
# This script fetches the pdb data for the protein using the protein code '4x61'.             #
# It also separate the protein from the ligand file for 3XV and saves them in the pdb format. #
# Ligand is converted to SMILES format and the python module called confgen.py is used to     #
# generate the conformers. Finally, the conformers are saved into one xyz file.               #
#                                                                                             #
###############################################################################################

#Fetch the protein + ligand file in pymol
cmd.fetch(sys.argv[1])

#Get sub-structures of the ligand and the protein indepedently
cmd.select(name='Prot',selection='polymer.protein')
cmd.select(name='Lig', selection='resn 3XV')
cmd.save(filename='4x61_clean.pdb',format='pdb',selection='Prot')
cmd.save(filename='3XV.pdb',format='pdb',selection='Lig')
cmd.delete('all')

#Storing the ligand file with hydrogens for the bound geometry energy calculation
cmd.load('3XV.pdb', 'ligandFile')
cmd.h_add()
cmd.save('3XV_H.pdb')
cmd.delete('all')

#Converting the ligand format to SMILES
conv=openbabel.OBConversion()
conv.OpenInAndOutFiles("3XV.pdb","3XV.smi")
conv.SetInAndOutFormats("pdb","smi")
conv.Convert()
conv.CloseOutFile()

#Convert the ligand pdb format into xyz format for xtb
conv1=openbabel.OBConversion()
conv1.OpenInAndOutFiles("3XV_H.pdb","3XV_H.xyz")
conv1.SetInAndOutFormats("pdb","xyz")
conv1.Convert()
conv1.CloseOutFile()

#Generating conformers through the module confgen_rdkit.py present in the current directory
with open('3XV.smi') as f:
    smiles = f.readlines()
    smiles = smiles[0].split()[0]
outputFile = sys.argv[2]
numconf = int(sys.argv[3])
confgen_rdkit.confgen(smiles, outputFile, numconf, mmTheory ='MMFF94s')

#Converting from sdf to xyz for xtb calculations
conv=openbabel.OBConversion()
conv.OpenInAndOutFiles("configurations_rdkit.sdf","configurations_rdkit.xyz")
conv.SetInAndOutFormats("sdf","xyz")
conv.Convert()
conv.CloseOutFile()

