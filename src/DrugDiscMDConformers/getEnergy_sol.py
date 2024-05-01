import os, sys, re

os.chdir('molecular_files')
os.chdir('rdkit_conformers')
nums = ["%.4d" % i for i in range(int(sys.argv[1]))]
for num in nums:
    os.chdir('sol_conf_' + num)
    INF = open('conf_' + num + '.log','r').read()
    energy = re.findall('TOTAL ENERGY\s+(\S+)\s+\S+\s+\S+', INF)
    if energy != []:
        print(num, energy[0])
    os.chdir('../../../')
os.chdir('../../../')
os.chdir('../../../')


