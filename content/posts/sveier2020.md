+++
title = "sveier2020 | Dual Quaternion Particle Filtering for Pose Estimation"
author = ["João Gutemberg Farias"]
draft = false
+++

The authors develop a Dual Quaternion [Particle Filter]({{< relref "particle_filter" >}}) and test it in the [pose estimation]({{< relref "pose_estimation" >}}) of a hanging payload using point clouds data from a Kinect. The pose estimation is then validated showing accurate results.


## Info {#info}

This article presents a particle filter for pose estimation using unit dual quaternion kinematics. The eight-parameter unit dual quaternion is used for global representation of the pose, whereas the six parameters of the dual modified Rodrigues parameters (MRPs) are used for local pose representation in the state-space model. The dual MRPs enable estimates of the mean and the covariance to be calculated from the particles without violating the algebraic constraint of the unit dual quaternion. For verification of the filter and comparison with state of the art, we consider pose measurements available in the form of unit dual quaternions. Angular velocity and specific force measurements from a body-mounted inertial measurement unit are also considered in the filtering. We show through simulations that the suggested particle filter has comparable accuracy with a previously proposed unscented Kalman filter based on unit dual quaternions. We also consider a practical application where the pose of an arbitrary rigid object is estimated using a sequence of point clouds from a 3-D camera. A model point cloud of the object is displaced with the unit dual quaternion associated with each particle, and a fitting score is calculated between the displaced model point cloud and the measured point cloud from the 3-D camera. The likelihoods of the fitting scores are calculated from an exponential distribution and are used to update the weights of the particles. The system was verified in an experiment where the motion of a swinging payload hanging from a crane was estimated using a 3-D camera.


## Notes {#notes}


### Resumo {#resumo}

The authors develop a Dual Quaternion [Particle Filter]({{< relref "particle_filter" >}}) and test it in the [pose estimation]({{< relref "pose_estimation" >}}) of a hanging payload using point clouds data from a Kinect. The pose estimation is then validated showing accurate results.
