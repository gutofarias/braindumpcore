+++
title = "mirandadefarias2019 | Performance Study on dqRNEA  A Novel Dual Quaternion Based Recursive Newton-Euler Inverse Dynamics Algorithms"
author = ["João Gutemberg Farias"]
draft = false
+++

The work do a performace study on an Recursive [Newton-Euler]({{< relref "newton_euler_method" >}}) Inverse Dynamics Algorithm using dual quaternions. The algorithm uses Newton-Euler formulation to compute the kinematics and given the desired accelerations and external forces, computes the necessary torques of the motors to drive the system.

They use dual quaternions in the kinematics and kinetics, for the inertia they create an inertia function (so not explicitily a matrix). They use a screw theory approach for the kinematics, not using DH.

The performance of the algorithm using DQ is compared to using HTM, and the result is favorable to DQ, maybe like 33% less cost in terms of number of operations.


## Info {#info}

In this paper, the well known recursive NewtonEuler inverse dynamics algorithm for serial manipulators is reformulated into the context of the algebra of Dual Quaternions. Here we structure the forward kinematic description with screws and line displacements rather than the well established Denavit-Hartemberg parameters, thus accounting better efficiency, compactness and simpler dynamical models. Furthermore, the backwards iteration uses the previously calculated values for estimating the joint space torques. In addition, a cost analysis of the main Dual Quaternions operations and of the Newton-Euler inverse dynamics algorithm as a whole is made and compared with other results in the literature.


## Notes {#notes}


### Resumo {#resumo}

The work do a performace study on an Recursive Newton-Euler Inverse Dynamics Algorithm using dual quaternions. The algorithm uses Newton-Euler formulation to compute the kinematics and given the desired accelerations and external forces, computes the necessary torques of the motors to drive the system.

They use dual quaternions in the kinematics and kinetics, for the inertia they create an inertia function (so not explicitily a matrix). They use a screw theory approach for the kinematics, not using DH.

The performance of the algorithm using DQ is compared to using HTM, and the result is favorable to DQ, maybe like 33% less cost in terms of number of operations.
