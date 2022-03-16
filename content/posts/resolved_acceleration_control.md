+++
title = "Resolved-Acceleration Control"
author = ["João Gutemberg Farias"]
draft = false
+++

Is a method for [task space]({{< relref "task_space" >}}) control.

It consists in compute the torques and forces using the second order (acceleration) kinematics of the system. In order to do that one has to plan a trajectory to have the desired kinematics of the [end-effector]({{< relref "end_link" >}}). Then, compute the joints acceleration (using the end-effector kinematics) and then compute the torques and forces necessary to create such accelerations.

The controller is presented in:

Luh, J., Walker, M., &amp; Paul, R. (1980). Resolved-acceleration control of mechanical manipulators. IEEE Trans. Automat. Contr., 25(3), 468–474. <http://dx.doi.org/10.1109/TAC.1980.1102367>

[luh1980 | Resolved-acceleration control of mechanical manipulators]({{< relref "luh1980" >}})
