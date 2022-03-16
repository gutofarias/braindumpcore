+++
title = "schwung2021 | Rigid Body Movement Prediction Using Dual Quaternion Recurrent Neural Networks"
author = ["João Gutemberg Farias"]
draft = false
+++

The work uses [Dual-Quaternions Neural Networks]({{< relref "dual_quaternions_neural_networks" >}}) to predict the behavior (physics) of a simulated system of masses inside a box. So the neural network predicts rigid body movement.

The authors say that using DQ in a neural network allows to incorporate physical bias into the prediction task. I.e., just by using the DQ we are already favoring the task of rigid body movement prediction, due to how DQ relates to this task.

It applies two different neural networks, a DQ Recurrent NN (DQRNN) and a DQ Long Short Term Memory NN (DQLSTM). DQLSTM obtained a higher accuracy than DQRNN and when we compare it with a normal LSTM the DQLSTM got half the [root mean square error (RMSE)]({{< relref "root_mean_square_error" >}}). So it performed really well.


## Info {#info}

This paper presents a novel approach for the data based prediction of rigid body movements. To this end, we combine data based learning with a physically motivated neural network architecture using the theory of dual quaternions. Particularly, we develop a novel neural network architecture based on dual quaternion algebra which is particular suitable for representing rigid body movements. To account for multistep predictions and the inherent dynamics of rigid bodies, we particularly focus on recurrent neural networks. As such we propose both dual quaternion recurrent neural networks as well as dual quaternion long short term memories. We apply the approach to a simplified simulation environment developed using the discrete element method which allows for a very detailed simulation of the movements. The obtained results underline the applicability and potential of the approach in terms of improved prediction performance.


## Notes {#notes}


### Resumo {#resumo}

The work uses Dual-Quaternions Neural Networks to predict the behavior (physics) of a simulated system of masses inside a box. So the neural network predicts rigid body movement.

The authors says that using DQ in a neural network allows to incorporate physical byas into the prediction task. I.e., just by using the DQ we are already favoring the task of rigid body movement prediction, due to how DQ relates to this task.

It applies two different neural networks, a DQ Recurrent NN (DQRNN) and a DQ Long Short Term Memory NN (DQLSTM). DQLSTM obtained a higher accuracy than DQRNN and when we compare with a normal LSTM the DQLSTM got half the root square mean error (RSME). So it performed really well.
