+++
title = "Considerations over the inertia matrix - Davies Method for Dynamics"
author = ["João Gutemberg Farias"]
draft = false
+++

We are using all the efforts in the inertial reference frame, so the inertia matrix should be writen in that same frame.
One problem arrises, the inertia matrix is not constant in the inertial frame, but it is so in an appropriate mobile frame. So we go frame from the mobile frame and transform it to the inertial frame. I.e.,

\\[ {\_I}I\_{i} = R^T\_i \\, {\_{Bi}I\_{i} \\]

where \\(i\\) refers to one of the links.

We are using \\(R\\) as a [transformation matrix]({{< relref "transformation_matrix" >}}). But maybe we should use \\(q\\) and \\(q^\*\\) in order to remain in the quaternion world.

The derivative of the inertia matrix is computed by:

\\[ {\_I}\dot{I}\_{i} = \Omega\_i \\, R^T\_i \\, {\_{Bi}I\_{i} \\]

where \\(\Omega\_i\\) is the anti-simmetrical matrix equivalent to a vectorial product of the angular velocity \\(\vec{\omega}\_i\\). This term comes from the derivative of the transformation matrix.
