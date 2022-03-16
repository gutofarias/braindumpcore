+++
title = "amininan2017 | Explicit Inverse Kinematic Solution for the Industrial FUM Articulated Arm using Dual Quaternion Approach"
author = ["João Gutemberg Farias"]
draft = false
+++

The paper solves the [inverse kinematics]({{< relref "inverse_kinematics" >}}) of an specific [serial 6dof industrial arm]({{< relref "serial_mechanism" >}}) using dual quaternions. The [direct kinematics]({{< relref "direct_kinematics" >}}) equations are derived using DQ and through manipulating the equations they can solve it for the inverse kinematics problem. Nothing too fancy or new.


## Info {#info}

The industrial grade FUM articulated arm is a six-axis robot arm, here on referred to as, FUM 6R-20, designed by Ferdowsi University of Mashhad Robotics Lab. In this paper, an explicit inverse kinematics solution for the industrial grade FUM 6R-20 is presented. The dual quaternion, DQ, method is presented. This method uses two quaternions, one for orientation and one for position to represent the kinematics equations of the robot. The DQ method avoids the wrist singularity as a result of the rotation matrices. It is shown that this approach eliminates the wrist singularity and the gimbal lock problem. The Simulink as well as the SolidWorks models of the FUM 6R-20 are also developed. All eight inverse kinematics solutions are obtained. Three random positions and orientations in space are selected and results of the closed-form solutions are verified with the results of both Simulink and SolidWorks software.


## Notes {#notes}

The paper solves the inverse kinematics of an specific serial 6dof industrial arm using dual quaternions. The direct kinematics equations are derived using DQ and through manipulating the equations they can solve it for the inverse kinematics problem. Nothing too fancy or new.
