import os, sys
from multiprocessing import Pool

##############################################
#                                            #
# This program takes in two arguments        #
# arg 1: index of the first calculation      #
# arg 2: index of the (last + 1) calculation #
#                                            #
##############################################

num1, num2 = int(sys.argv[1]), int(sys.argv[2])

def e1(i):
    ######################################################################
    #                                                                    #
    # This function runs optimization calculation for the i-th conformer #
    #                                                                    #
    ######################################################################
    os.chdir('conf_' + i)
    os.system('xtb conf_' + i + '.xyz --opt -P 1 --gfn 2 > conf_' + i + '.log')
    os.chdir('../../../')

if __name__ == '__main__':
    os.chdir('molecular_files')
    os.chdir('rdkit_conformers')
    v = ["%.4d" % i for i in range(num1, num2)]
    #Generating a pool of 46 parallel processes below due to the limit of 48 cores on the computing machine used
    with Pool(46) as p:
        p.map(e1, v)
    os.chdir('../../../')
    os.chdir('../../../')

