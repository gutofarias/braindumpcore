+++
title = "sveier2018 | Pose Estimation using Dual Quaternions and Moving Horizon Estimation"
author = ["João Gutemberg Farias"]
draft = false
+++

The author presents a [Moving Horizon Estimator]({{< relref "moving_horizon_estimator_mhe" >}}) for [pose estimation]({{< relref "pose_estimation" >}}) using Dual Quaternions. They were able to formulate the [cost function]({{< relref "cost_function" >}}) in terms of the DQ product and so satisfying the unitaryness constraint. Also they discretize the DQ and used a Caley transform presented in an article of Selig.
The resulting estimator was more accurate them DQ-MEKF (DQ Multiplicative Extended Kalman Filter) and T-UKF (Twistor-bases Unscented Kalman Filter) which the author attributes to the moving horizon strategy (so not only the last result is used).


## Info {#info}


## Notes {#notes}


### Resumo {#resumo}

The author presents a Moving Horizon Estimator for pose estimation using Dual Quaternions. They were able to formulate the cost function in terms of the DQ product and so satisfying the unitaryness constraint. Also they discretize the DQ and used a Caley transform presented in an article of Selig.
The resulting estimator was more accurate them DQ-MEKF (DQ Multiplicative Extended Kalman Filter) and T-UKF (Twistor-bases Unscented Kalman Filter) which the author attributes to the moving horizon strategy (so not only the last result is used).
