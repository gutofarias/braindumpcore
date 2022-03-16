+++
title = "schilling2019 | Hierarchical Dual Quaternion-Based Recurrent Neural Network as a Flexible Internal Body Model"
author = ["João Gutemberg Farias"]
draft = false
+++

The author uses Mean of Multiple Computations (MMC) as a hierarchical recurrent neural network to model a redundant robot. The technique generates a lot of simple equations that converge to a feasible solution where there are many ways for the same pose of the [end-effector]({{< relref "end_link" >}}).
Using dual quaternions components in the neural network, the author can approximate transformations by interpolation, which is shown to be a great advantage of DQs.
At the end, the author shows the viability of the proposed solution applying it to a complex robot consisting of two arms each having 7 DoF.


## Info {#info}

Internal models of the body are assumed to serve a multitude of different functions. Forward and inverse models are important concepts in motor control. Usually, it is distinguished between these function and there are different models for each individual function or there are even models that are specific to individual behaviors. Here, we present a concept of a core internal model of the body which can act both as an inverse and forward model. In addition, it provides a mechanism for integration of sensory data and can be in this way grounded in the continuous interaction with the environment. In this article, a hierarchical Mean of Multiple Computations neural network is presented that is based on an axis-angle representation of joint movements using dual quaternions. It is shown in detail how the network provides a solution for the forward kinematic problem applied for the case of a seven degrees of freedom robotic arm. Furthermore, it is used in a complex scenario of a bimanual movement task. This demonstrates how the MMC approach can be easily scaled up from a representation of a single arm to a complex model of a complete body.


## Notes {#notes}


### Resumo {#resumo}

The author uses Mean of Multiple Computations (MMC) as a hierarchical recurrent neural network to model a redundant robot. The technique generates a lot of simple equations that converge to a feasible solution where there are many ways for the same pose of the end-effector.
Using dual quaternions components in the neural network, the author can approximate transformations by interpolation, which is shown to be a great advantage of DQs.
At the end, the author shows the viability of the proposed solution applying it to a complex robot consisting of two arms each having 7 DoF.
