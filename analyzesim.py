## Analyze results of the initial OpenMM trial SETD2 simulation - Zn-CYM distances, angles
# imports
from __future__ import print_function
import mdtraj as md
import numpy as np

# load into mdtraj
traj = md.load("output.pdb")
topo = traj.topology

# gen pairs of Zn-S indices (ZNB are 246/7/8)
pairs246 =  topo.select_pairs('resSeq 246 and name Zn', '(resSeq 53 or resSeq 55 or resSeq 70 or resSeq 74) and name SG')
pairs247 =  topo.select_pairs('resSeq 247 and name Zn', '(resSeq 70 or resSeq 83 or resSeq 87 or resSeq 93) and name SG')
pairs248 =  topo.select_pairs('resSeq 248 and name Zn', '(resSeq 185 or resSeq 232 or resSeq 234 or resSeq 239) and name SG')

# calc distances
distances246 = md.compute_distances(traj,pairs246)
distances247 = md.compute_distances(traj,pairs248)
distances248 = md.compute_distances(traj,pairs248)

# save results
np.savetxt('distances246.txt', distances246)
np.savetxt('distances247.txt', distances247)
np.savetxt('distances248.txt', distances248)
