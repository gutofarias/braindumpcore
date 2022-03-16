+++
title = "bultmann2019 | Stereo Visual SLAM Based on Unscented Dual Quaternion Filtering"
author = ["João Gutemberg Farias"]
draft = false
+++

[SLAM]({{< relref "simultaneous_localization_and_mapping_slam" >}}) using an DQ unscented filter and using the stero visual data.
Não tenho muito a dizer porque não li muito.


## Info {#info}

We present DQV-SLAM (Dual Quaternion Visual SLAM). This novel feature-based stereo visual SLAM framework uses a stochastic filter based on the unscented transform and a progressive Bayes update, avoiding linearization of the nonlinear spatial transformation group. 6-DoF poses are represented by dual quaternions where rotational and translational components are stochastically modeled by Bingham and Gaussian distributions. Maps represented by point clouds of ORB-features are incrementally built and landmarks are updated with an unscented transform-based method. In order to get reliable measurements during the update, an optical flow-based approach is proposed to remove false feature associations. Drift is corrected by pose graph optimization once loop closure is detected. The KITTI and EuRoC datasets for stereo setup are used for evaluation. The performance of the proposed system is comparable to stateof-the-art optimization-based SLAM systems and better than existing filtering-based approaches.


## Notes {#notes}


### Resumo {#resumo}

SLAM using an DQ unscented filter and using the stero visual data.
Não tenho muito a dizer porque não li muito.
