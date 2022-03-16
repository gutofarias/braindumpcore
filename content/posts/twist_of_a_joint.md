+++
title = "Twist of a Joint"
author = ["João Gutemberg Farias"]
draft = false
+++

A joint that allows one motion has one defining [screw]({{< relref "screw" >}}) and one defining variable.

If the joint is a [rotation joint]({{< relref "rotation_oint" >}}), the screw is the [axis of the joint]({{< relref "line_vector" >}}) and the variable is the angular velocity (as a scalar). The twist is then the angular velocity of the joint times its screw.

If the joint is a [prismatic joint]({{< relref "prismatic_joint" >}}), the screw can be:

-   A [pure vector]({{< relref "pure_vector" >}}) as the [dual part]({{< relref "dual_part" >}}) of a [dual vector]({{< relref "dual_vector" >}}) or last three components in [Plucker Coordinates]({{< relref "plucker_coordinates" >}}). The defining variable is the translational velocity (as a scalar). The vector is the direction of the translation.
    In that case, the twist will be the screw multiplied by the real translational velocity.

-   An [axis]({{< relref "line_vector" >}}) as a dual vector or in Plucker coordinates. The axis would be the literal line at which the translation happens, not only the direction. The defining variable is the dual translational velocity (\\(0 + \epsilon \\, v\\)) (v is a scalar)
    In that case, the twist will be the screw multiplied by a dual translational velocity (\\(0 + \epsilon \\, v\\)).

In general, almost every joint can be built as a combination of rotation joints and prismatic joints, so build the twists accordingly.
