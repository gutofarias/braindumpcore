+++
title = "Understanding Davies Method's kinematic analysis"
author = ["João Gutemberg Farias"]
draft = false
+++

When performing [Davies Method]({{< relref "davies_method" >}}), we use the [origin of the system]({{< relref "base_link" >}}) as a reference for kinematic calculations. Once we compute the effect of a joint into a link, it is computed as if the link virtually extended to the origin. So we compute the kinematic of a point in the link virtually positioned when the whole link suffers the kinematic effects caused by the joint movement.

As Davies Method deals with [Closed Kinematic Chain System]({{< relref "closed_kinematic_chain_system" >}}) by conception, the [Kirchhoff Voltage Law]({{< relref "kirchhoff_voltage_law_davies_method" >}}) applied using [Graph Theory]({{< relref "graph_theory" >}}) generates an equation for a [Closed Kinematic Chain]({{< relref "closed_kinematic_chain" >}}). So we compute all the joint contribution to the kinematics of the origin and, as the circuit is closed, we begin at the origin an end at the origin, obtaining a net velocity of zero. Thats how one kinematic equation is born in Davies Method.

The use of [Kirchhoff Voltage Law]({{< relref "kirchhoff_voltage_law_davies_method" >}}) in a [Graph]({{< relref "graph_theory" >}}) framework allows us to get unambiguous equations.
