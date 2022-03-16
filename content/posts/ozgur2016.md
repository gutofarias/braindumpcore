+++
title = "ozgur2016 | Kinematic modeling and control of a robot arm using unit dual quaternions"
author = ["João Gutemberg Farias"]
draft = false
+++

Very interesting article of kinematic modeling and control of robotic arms. It uses a [Screw Theory]({{< relref "screw_theory" >}}) approach to model the kinematics, much like [Successive Screws]({{< relref "successive_screws" >}}), but using only one frame, doesn't need a [convenient frame]({{< relref "convenient_frame" >}}). Also the metodology is mind opening someway because the authors model the rotations from [end-effector]({{< relref "end_link" >}}) to [base]({{< relref "base_link" >}}), and not the opositte, which in my opinion is easier to understand because going from end to base the successive rotations are not carried by the previous rotations.


## Info {#info}

This paper exploits screw theory expressed via unit dual quaternion representation and its algebra to formulate both the forward (position + velocity) kinematics and pose control of an n-dof robot arm in an efficient way. Efficiency is in less computer memory usage, in fast computation of the equations, in singularity-free representation of task space, in robustness to numerical errors, and in compactness of the representations. The formulation is simple, intuitive and straightforward to implement. We validated this formulation experimentally on a 7 dof robot arm.


## Notes {#notes}


### Resumo {#resumo}

Very interesting article of kinematic modeling and control of robotic arms. It uses a [Screw Theory]({{< relref "screw_theory" >}}) approach
to model the kinematics, much like Successive Screws, but using only one frame, doesn't need a convenient frame. Also the metodology is mind opening someway because the authors model the rotations from end-effector to base, and not the opositte, which in my opinion is easier to understand because going from end to base the successive rotations are not carried by the previous rotations.
