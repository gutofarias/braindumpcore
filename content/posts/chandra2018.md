+++
title = "chandra2018 | Dual-Arm Coordination Using Dual Quaternions and Virtual Mechanisms"
author = ["João Gutemberg Farias"]
draft = false
+++

The work uses what I think can be classified as a [Dual Robot]({{< relref "dual_robots" >}}) but they call a Dual-Arm robot. The authors use DQ to describe and control the coordinated motion of the arms of the robot.
In order to do that, the work defines three reference frames and uses [Relative Jacobians]({{< relref "relative_jacobian" >}}). Also they parametrize the task to be performed by a [Virtual Mechanism]({{< relref "virtual_mechanism" >}}) that conects both arms. It is an interesting idea, since by doing that they can impose restrictions to the robot arms movement by the layout of the virtual mechanism. So by using this, the whole modeling looks like a two [chains]({{< relref "kinematic_chains" >}}) parallel robot.


## Info {#info}

A novel approach to the kinematic coordination problem for dual-arm robots and for the definition of bimanual tasks is proposed, where both modelling and control aspects of the problem are handled using dual quaternion representation of pose and screw-based manipulator Jacobian. The proposed formulation is advantageous in terms of computation and storage efficiency compared to other formulations of dual-arm manipulator forward kinematics and Jacobian computation. Unit dual quaternion representation is also capable of avoiding representational singularities related to orientation.


## Notes {#notes}


### Resumo {#resumo}

The work uses what I think can be classified as a [Dual Robot]({{< relref "dual_robots" >}}) but they call a Dual-Arm robot. The authors use DQ to describe and control the coordinated motion of the arms of the robot.
In order to do that, the work defines three reference frames and uses [Relative Jacobians]({{< relref "relative_jacobian" >}}) which I didn't understand very well (looks like a normal jacobian but maybe the jacobian of a relative motion of two frames).
Also they parametrize the task to be performed by a [Virtual Mechanism]({{< relref "virtual_mechanism" >}}) that conects both arms. It is an interesting idea, since by doing that they can impose restrictions to the robot arms movement by the layout of the virtual mechanism. So by using this, the whole modeling looks like a two [chains]({{< relref "kinematic_chains" >}}) parallel robot.
