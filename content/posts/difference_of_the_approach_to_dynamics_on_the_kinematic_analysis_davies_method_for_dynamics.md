+++
title = "Difference of the approach to Dynamics on the Kinematic Analysis - Davies Method for Dynamics"
author = ["João Gutemberg Farias"]
draft = false
+++

Check out [Understanding Davies Method's kinematic analysis]({{< relref "understanding_davies_method_s_kinematic_analysis" >}}) first.

To deal with dynamics, we can not reference the origin of the system, we need to reference the center of mass of each of the links. Also, we can not make a [Closed Kinematic Chain]({{< relref "closed_kinematic_chain" >}}) equation, as the kinematics of a link depends only on the previous joints, not on the next ones.

So in order to compute the kinematics of a link we use the the [Coupling Graph]({{< relref "coupling_graph" >}}) and make a graph trajectory going from the [base link]({{< relref "base_link" >}}) (origin of the system) to the link whose kinematics we are calculating. We take into account all the joints in this trajectory.

Going through each joint we are summing up the [twists]({{< relref "twist" >}}) of the joint relative to the center of mass of the link. The result is the kinematics of link's center of mass, which is the information we need in a Dynamics analysis.

When dealing with a [Closed Kinematic Chain System]({{< relref "closed_kinematic_chain_system" >}}), there is more than one trajectory to get from the [Base Link]({{< relref "base_link" >}}) to the link whose kinematics we are calculating. We choose one trajectory and use it. The ambiguity will be taken care of after when we analyse the relations between the joints.
