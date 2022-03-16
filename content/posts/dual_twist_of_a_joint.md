+++
title = "Hyper-Dual Twist of a Joint"
author = ["João Gutemberg Farias"]
draft = false
+++

To construct the [Hyper-Dual Twist]({{< relref "hyper_dual_twist" >}}), start with [Twist of a Joint]({{< relref "twist_of_a_joint" >}}). Use the separation of the twist as an [axis]({{< relref "line_vector" >}}) and a dual joint variable:

\\[ \xi = (\omega + \epsilon \\, 0) \\, \hat{s}   = \hat{\omega}  \\, \hat{s}\\]

Transforming to hyper-dual numbers we obtain:

\\[ \check{\xi} = [ (\omega + \epsilon \\, 0) + \check{\epsilon} (\dot{\omega} + \epsilon \\, 0)] (\hat{s} + \check{\epsilon} \\, \dot{\hat{s}}) = (\hat{\omega} + \check{\epsilon} \\, \dot{\hat{\omega}})(\hat{s} + \check{\epsilon} \\, \dot{\hat{s}})  \\]

\\[ \check{\xi} = \check{\omega} \\, \check{s}\\]

Note that in the hyper-dual part we get the true derivative of the hyper-real part:

\\[ \check{\xi} = (\hat{\omega} + \check{\epsilon} \\, \dot{\hat{\omega}})(\hat{s} + \check{\epsilon} \\, \dot{\hat{s}}) = \hat{\omega} \\, \hat{s} + \check{\epsilon} ( \hat{\omega} \\, \dot{\hat{s}} + \dot{\hat{\omega}} \\, \hat{s} ) \\]

If working with prismatic joint we have two choices:

1.  Using the velocity as a [pure dual number]({{< relref "pure_dual_number" >}})

    \\[\xi = (0 + \epsilon \\, v) \\, \hat{s} \\]

    \\[\check{\xi} = [\epsilon \\, v + \check{\epsilon} (\epsilon \\, \dot{v})\]\(\hat{s} + \check{\epsilon} \\, \dot{\hat{s}}) \\]

2.  Applying the dual operator in \\(\hat{s}\\) and using \\(v\\) as a [pure real number]({{< relref "pure_real_number" >}}).

    \\[ \hat{s} = \vec{s} + \epsilon \\, \vec{s}\_o\\]
    \\[\hat{s}^\* = \epsilon \\, \hat{s} = 0 + \epsilon \\, \vec{s}\\]

    \\[\xi = (0 + \epsilon \\, v) \\, \hat{s} = (v + \epsilon \\, 0) \\, \hat{s}^\* = \hat{v} \\, \hat{s}^\*\\]

    \\[ \check{\xi} = (\hat{v} + \check{\epsilon} \\, \dot{\hat{v}}) (\hat{s}^\* + \check{\epsilon} \\, \dot{\hat{s}}^\*) = \check{v} \\, \check{s}^\* \\]

    That way is better for when dealing with [Dynamics Extension for Davies Method]({{< relref "dynamics_extension_for_davies_method" >}}), because we can isolate the variable \\(\dot{v}\\) without the \\(\epsilon\\) getting in the way.

Once composed that way, we can use the hyper-dual joint variables and hyper-dual axis as normal. The structure of the dual entities will guarantee that the differentiation stays valid. I.e., whatever you got in the hyper-dual side is the derivative of whatever you got in the hyper-real side.
