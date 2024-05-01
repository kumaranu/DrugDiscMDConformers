from rdkit import Chem
from rdkit.Chem import rdDistGeom
from rdkit.Chem import AllChem
from rdkit.Chem import rdMolAlign
import sys

'''
    The confgen method calculated the molecular conformers and writes them to a file. The details are as follows:
      prerequisites:
        - This function needs rdkit library to be installed
      parameters:
        1) smiles string       (a string) - Smiles string for the molecule
        2) outputFile          (a string) - Path to a file where you want the output to be put in.
        3) numconf           (an integer) - No. of conformers needed to be generated.
        4) (Optional) mmTheory (a string) - The level of theory you want to use for the force fields used to generate the conformers
                                            The default argument is 'MMFF94s'
'''

def confgen(smiles, outputFile, numconf, mmTheory = 'MMFF94s'):
    mol = Chem.MolFromSmiles(smiles)
    mol = Chem.AddHs(mol)
    cids = rdDistGeom.EmbedMultipleConfs(mol, numconf)
    mp = AllChem.MMFFGetMoleculeProperties(mol, mmffVariant=mmTheory)
    AllChem.MMFFOptimizeMoleculeConfs(mol, numThreads=0, mmffVariant=mmTheory)
    w = Chem.SDWriter(outputFile)
    for cid in cids:
        w.write(mol, confId=cid)
    w.close()

