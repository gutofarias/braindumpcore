+++
title = "cheng2016 | Dual quaternion-based graphical SLAM"
author = ["João Gutemberg Farias"]
draft = false
+++

Parametrizes the [SLAM (Simultaneous Location and Mapping)]({{< relref "simultaneous_localization_and_mapping_slam" >}}) problem using dual-quaternions instead of [HTM]({{< relref "homogeneous_transformation_matrix" >}}). The problem is solved through a [graph]({{< relref "graph_theory" >}}) approach that in the DQ formulation can have DQs in the vertices and in the edges, because DQs can represent both the state and the restrictions. The proposed solution improves the computational performance when compared to the same approach using HTM.


## Info {#info}

This paper presents a new parameterization approach for the graph-based SLAM problem and reveals the differences of two popular over-parameterized ways in the optimization procedure. In the SALM problem, constraints or relative transformations between any two poses are generally separated into translations plus 3D rotations, which are then described in a homogeneous transformation matrix (HTM) to simplify computational operations. This however introduces added complexities in frequent conversions between the HTM and state variables, due to their different representations. This new approach, unit dual quaternion (UDQ), describes a spatial transformation as a screw with only 8 elements. We show that state variables can be directly represented by UDQs, and how their relative transformations can be written with the UDQ product, without the trivial computations of HTM. Then, we explore the performances of the unit quaternion and the axis      extendash angle representations in the graph-based SLAM problem, which have been successfully applied to over parameterize perturbations under the assumption of small errors. Based on public synthetic and real-world datasets in 2D and 3D environments, experimental results show that the proposed approach reduces greatly the computational complexity while obtaining the same optimization accuracies as the HTM-based algorithm, and the axis extendash angle representation is superior to be the quaternion in the case of poor initial estimations.


## Notes {#notes}


### Resumo {#resumo}

Parametriza o problema chamado de SLAM (Simultaneous Location and Mapping) usando quatérnios duais no lugar de matrizes de transformação homogêneas. O problema é tratado por meio da abordagem de grafo que, nesse caso, usa quatérnios duais nos vértices e arestas, pois conseguem representar tanto os estados como as restrições.
A resolução proposta melhora consideravelmente a performance computacional usando quatérnios duais quando comparado com HTM.
