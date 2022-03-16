+++
title = "Considerations of using Hyper-Dual Quaternions/Vectors - Davies Method for Dynamics"
author = ["João Gutemberg Farias"]
draft = false
+++

[Hyper-Dual Quaternions]({{< relref "hyper_dual_quaternions" >}}) | [Hyper-Dual Vectors]({{< relref "hyper_dual_vectors" >}})

The kinematics using Davies Method is computed for the velocity. But dynamics needs acceleration. In order to obtain that we will use [hyper-dual quantities]({{< relref "hyper_dual_numbers" >}}).

For example, when describing a dual veclocity as a dual vector, we have:

\\[ \nu = \omega + \epsilon \\, v \\]

This has the information of the angular velocity and linear velociy. We extend that using the property of [Automatic Differentiation]({{< relref "automatic_differentiation" >}}) to:

\\[ \check{\nu} = (\omega + \epsilon \\, v) + \check{\epsilon} \\, (\dot{\omega} + \epsilon \\, \dot{v}) = \nu + \check{\epsilon} \\, \dot{\nu} \\]
