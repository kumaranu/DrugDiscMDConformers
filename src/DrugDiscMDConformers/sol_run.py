import os
import sys
from multiprocessing import Pool
from typing import List


def e2(i: str) -> None:
    """Run optimization calculations for solvated conformers.

    Args:
        i (str): Index of the conformer.

    Returns:
        None
    """
    os.chdir(f'sol_conf_{i}')
    os.system(f'xtb conf_{i}.xyz --ohess -P 1 --gfn 2 --alpb water > conf_{i}.log')
    os.chdir('../../../')


def run_solvated_optimization(num1: int, num2: int) -> None:
    """Run optimization calculations for solvated conformers.

    Args:
        num1 (int): Start index of the conformers.
        num2 (int): End index of the conformers.

    Returns:
        None
    """
    if __name__ == '__main__':
        os.chdir('molecular_files')
        os.chdir('rdkit_conformers')
        v: List[str] = ["%.4d" % i for i in range(num1, num2)]

        # Generating a pool of parallel processes
        with Pool(46) as p:  # Using 46 processes due to the limit of 48 cores on the computing machine
            p.map(e2, v)
        os.chdir('../../../')
        os.chdir('../../../')
