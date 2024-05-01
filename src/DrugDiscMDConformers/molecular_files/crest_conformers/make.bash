#!/bin/bash

#conda activate docking-rdock

#Optimizing using xtb
xtb input.xyz --opt -P 1 --gfn 2 > input.log

grep -iwA56 "final structure" input.log | tail -55 > input1.xyz

#Running conformer sampling
crest input1.xyz -gfn2 -T 16

