+++
title = "Maneuver Regulation"
author = ["João Gutemberg Farias"]
draft = false
+++

The goal of a maneuver regulation is to track a desired trajectory, but it differs from a [Trajectory Tracking]({{< relref "trajectory_tracking" >}}) task in the sense that a trajectory is locked in time and a maneuver regulation is not.
Imagine a circular trajectory, if you are in the circle but according to the time your trajectory should be in the opposite side of the circle. That would be a problem for a trajectory tracking, but a maneuver regulation can just perform a time warping so that you can match the trajectory already where you are. The trajectory would be the same but with a time offset.
Also, as I understood, it just adjusts the initial time of the trajectory it doesnt keep always adjusting.
It uses a [Cost Function]({{< relref "cost_function" >}}) to determine the time offset which minimizes the cost function.
