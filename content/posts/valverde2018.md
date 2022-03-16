+++
title = "valverde2018 | Dual Quaternion Framework for Modeling of Spacecraft-Mounted Multibody Robotic Systems"
author = ["João Gutemberg Farias"]
draft = false
+++

The work describes an framework to derive the dynamics of a satellite, but it can be used to a general serial mechanism (at least I think), the proposed framework works with revolute, prismatic, cylindrical, spherical and planar joints. The equations are computed using dual quaternions and [Newton-Euler formulation]({{< relref "newton_euler_method" >}}).


## Info {#info}

This paper lays out a framework to model the kinematics and dynamics of a rigid spacecraft-mounted multibody robotic system. The framework is based on dual quaternion algebra, which combines rotational and translational information in a compact representation. Based on a Newton-Euler formulation, the proposed framework sets up a system of equations in which the dual accelerations of each of the bodies and the reaction wrenches at the joints are the unknowns. Five different joint types are considered in this framework via simple changes in certain mapping matrices that correspond to the joint variables. This differs from previous approaches that require the addition of extra terms that are joint-type dependent, and which decouple the rotational and translational dynamics.


## Notes {#notes}


### Resumo {#resumo}

The work describes an framework to derive the dynamics of a satellite, but it can be used to a general serial mechanism (at least I think), the proposed framework works with revolute, prismatic, cylindrical, spherical and planar joints. The equations are computed using dual quaternions and Newton-Euler formulation.
