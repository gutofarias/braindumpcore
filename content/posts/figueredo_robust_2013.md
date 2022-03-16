+++
title = "figueredo_robust_2013 | Robust kinematic control of manipulator robots using dual quaternion representation"
author = ["João Gutemberg Farias"]
draft = false
+++

tags
: [Dual Quaternions Applications]({{< relref "dual_quaternions_applications" >}})


## Resumo {#resumo}

Very good article in general, very well writen. Talks about a \\(H\_\infty\\) control using dual quaternions for the kinematics and control (for control the dual quarternion is used as an 8-vector). The control strategy is robust as it rejects perturbations. Also it defines a new error metric (more in the notes).
Very good introduction.


## Info {#info}

This paper addresses the H\\(infty\\) robust control problem for robot manipulators using unit dual quaternion representation, which allows an utter description of the end-effector transformation without decoupling rotational and translational dynamics. We propose three different H\\(infty\\) control criteria that ensure asymptotic convergence, whereas reducing the influence of disturbances upon the system stability. Also, with a new metric of dual quaternion error in SE(3) we prove independence from robot coordinate changes. Simulation results highlight the importance and effectiveness of the proposed approach in terms of performance, robustness, and energy efficiency.


## Notes {#notes}


### Resumo {#resumo}

Very good article in general, very well writen. Talks about a \\(H\_\infty\\) control using dual quaternions for the kinematics and control (for control the dual quarternion is used as an 8-vector). The control strategy is robust as it rejects perturbations. Also it defines a new error metric (more in the notes).
Very good introduction.


### Curiosidade {#curiosidade}

Kinematic control can be used when robot dynamics can be neglected, as in stiff (rígido) robots operating at low velocities.


### Nova métrica de erro {#nova-métrica-de-erro}

The author defines a new error metric, very simple and given by

\begin{align\*}
x\_e &= x\_m^\* \\, x\_d \\\\
e &= 1 - x\_e
\end{align\*}

The author claims that this new error is coordinate invariant, which is true but it is so because \\(x\_e\\) itself is coordinate invariant.
