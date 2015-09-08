## Analyze results of the initial OpenMM trial SETD2 simulation - Zn-CYM distances, angles
# imports
from __future__ import print_function
import mdtraj as md
import numpy as np

# load into mdtraj
traj = md.load("output.pdb")
topo = traj.topology

# generate indices of atoms for angles
# Zn's
zn246 = topo.select('resSeq 246 and name Zn')
zn247 = topo.select('resSeq 247 and name Zn')
zn248 = topo.select('resSeq 248 and name Zn')

# cysteines for ZN246
cs53 = topo.select('resSeq 53 and name SG')
cs55 = topo.select('resSeq 55 and name SG')
cs70 = topo.select('resSeq 70 and name SG')
cs74 = topo.select('resSeq 74 and name SG')
cc53 = topo.select('resSeq 53 and name CB')
cc55 = topo.select('resSeq 55 and name CB')
cc70 = topo.select('resSeq 70 and name CB')
cc74 = topo.select('resSeq 74 and name CB')
# cysteines for ZN247, CYM70 already defined
cs83 = topo.select('resSeq 83 and name SG')
cs87 = topo.select('resSeq 87 and name SG')
cs93 = topo.select('resSeq 93 and name SG')
cc83 = topo.select('resSeq 83 and name CB')
cc87 = topo.select('resSeq 87 and name CB')
cc93 = topo.select('resSeq 93 and name CB')
# cysteines for ZN248
cs185 = topo.select('resSeq 185 and name SG')
cs232 = topo.select('resSeq 232 and name SG')
cs234 = topo.select('resSeq 234 and name SG')
cs239 = topo.select('resSeq 239 and name SG')
cc185 = topo.select('resSeq 185 and name CB')
cc232 = topo.select('resSeq 232 and name CB')
cc234 = topo.select('resSeq 234 and name CB')
cc239 = topo.select('resSeq 239 and name CB')
# make arrays of trios
list246 = [[int(zn246), int(cs53), int(cc53)], [int(zn246), int(cs55), int(cc55)], [int(zn246), int(cs70), int(cc70)], [int(zn246), int(cs74), int(cc74)]]
list247 = [[int(zn247), int(cs70), int(cc70)], [int(zn247), int(cs83), int(cc83)], [int(zn247), int(cs87), int(cc87)], [int(zn247), int(cs93), int(cc93)]]
list248 = [[int(zn248), int(cs185), int(cc185)], [int(zn248), int(cs232), int(cc232)], [int(zn248), int(cs234), int(cc234)], [int(zn248), int(cs239), int(cc239)]]
array246 = np.asarray(list246)
array247 = np.asarray(list247)
array248 = np.asarray(list248)
# calc angles
angles246 = md.compute_angles(traj, array246)
angles247 = md.compute_angles(traj, array247)
angles248 = md.compute_angles(traj, array248)
# save results
np.savetxt('angles246.txt', angles246)
np.savetxt('angles247.txt', angles247)
np.savetxt('angles248.txt', angles248)
