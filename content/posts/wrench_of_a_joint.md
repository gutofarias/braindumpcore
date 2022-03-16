+++
title = "Wrench of a Joint"
author = ["João Gutemberg Farias"]
draft = false
+++

A [joint]({{< relref "joints" >}}) that allows one motion has 5 defining [screws]({{< relref "screw" >}}) and 5 defining variables in 3d and 2 defining screws and 2 defining variables in 2d. (One for each [Constraints of Motion]({{< relref "constraints_of_motion" >}})).

For each motion a joint does not allows, there should be a wrench constructed by:

-   Translational motion: for each translational motion it does not allows add one wrench whose [axis]({{< relref "line_vector" >}}) (defining screw) has the direction of the translational motion and position of the center of the joint. The defining variable should be the force (as a scalar) which does the constraintment.

-   Rotation motion: for each rotation motion it does not allows add one wrench, there are two options
    -   A screw given by a [pure vector]({{< relref "pure_vector" >}}) as the [dual part]({{< relref "dual_part" >}}) of a [dual vector]({{< relref "dual_vector" >}}) or last three components in [Plucker Coordinates]({{< relref "plucker_coordinates" >}}). The defining variable is the moment the does the constraintment (as a scalar). The vector is in the direction of the moment.
        In that case, the twist will be the screw multiplied by the force.

    -   An [axis]({{< relref "line_vector" >}}) as a dual vector or in Plucker coordinates. The axis would be the line given by the direction of the moment and the position of the center of the joint. The defining variable is the dual moment (\\(0 + \epsilon \\, M\\)) (M is a scalar)
        In that case, the twist will be the screw multiplied by the dual moment (\\(0 + \epsilon \\, M\\)).
