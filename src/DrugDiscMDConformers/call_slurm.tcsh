#!/bin/tcsh

###################################################################
#                                                                 #
# This script submits energy calculations using the slurm scripts #
# run.slurm and sol_run.slurm for a batch of 500 geometries which #
# are run parallelly by the python program called run.py.         #
#                                                                 #
###################################################################

#Clearing the slurm job directories if they already exist
rm -r -f dirSlurms

#Creating a separate directory for slurm job inputs
mkdir -p dirSlurms
cd dirSlurms
  set i = 0
  #The loop below will edit the slurm script templates run.slurm and sol_run.slurm and submit slurm jobs
  foreach j(`seq -w 500 500 10000`)
    echo "$i $j"
    sed "s/XX/$i/g; s/YY/$j/g" ../run.slurm > run$i.slurm
    sbatch run$i.slurm
    sed "s/XX/$i/g; s/YY/$j/g" ../sol_run.slurm > sol_run$i.slurm
    sbatch sol_run$i.slurm
    set i = $j
  end
cd ..


