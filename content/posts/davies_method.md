+++
title = "Davies Method"
author = ["João Gutemberg Farias"]
draft = false
+++

Davies Method is a method for computing the differential kinematics and statics of a general mechanical system using [Graph Theory]({{< relref "graph_theory" >}}), [Screw Theory]({{< relref "screw_theory" >}}) and [Plucker Coordinates]({{< relref "plucker_coordinates" >}}).

Start with a [Closed Kinematic Chain System]({{< relref "closed_kinematic_chain_system" >}}) (can be used with a [Open Kinematic Chain System]({{< relref "serial_mechanism" >}}) but it requires virtual links and joints) then follow the procedure


## Enumerate the joints and links {#enumerate-the-joints-and-links}

Use letters for the joints and numbers for the links. The earth or [support]({{< relref "base_link" >}}) should be number 0 or 1 (when there is no 0).


## Build a [Coupling Graph]({{< relref "coupling_graph" >}}) {#build-a-coupling-graph--coupling-graph-dot-md}


## Build a [Tree Graph]({{< relref "tree_graph" >}}) by [transforming the coupling graph into a tree]({{< relref "transforming_a_graph_into_a_tree" >}}). {#build-a-tree-graph--tree-graph-dot-md--by-transforming-the-coupling-graph-into-a-tree--transforming-a-graph-into-a-tree-dot-md--dot}

Account for the number os branches (k) and the number of strings (v) in the final tree.


## Evalute the [degrees of freedom]({{< relref "degrees_of_freedom" >}}) (f) and [constraints]({{< relref "constraints_of_motion" >}}) (c) of each joint. {#evalute-the-degrees-of-freedom--degrees-of-freedom-dot-md----f--and-constraints--constraints-of-motion-dot-md----c--of-each-joint-dot}


## Kinematic Analysis {#kinematic-analysis}


### Build the [Motion Graph]({{< relref "motion_graph" >}}) {#build-the-motion-graph--motion-graph-dot-md}


### Build the [Networks Graph]({{< relref "networks_graph" >}}) {#build-the-networks-graph--networks-graph-dot-md}


### Build the [Circuits Matrix]({{< relref "circuits_matrix" >}}) (B) {#build-the-circuits-matrix--circuits-matrix-dot-md----b}


### Define the [twists]({{< relref "twist" >}}) of the [edges]({{< relref "graph_edge" >}}) by [Twist of a Joint]({{< relref "twist_of_a_joint" >}}). {#define-the-twists--twist-dot-md--of-the-edges--graph-edge-dot-md--by-twist-of-a-joint--twist-of-a-joint-dot-md--dot}


### Build the [Direct Twists Matrix]({{< relref "direct_twists_matrix" >}}) (M_D) {#build-the-direct-twists-matrix--direct-twists-matrix-dot-md----m-d}

Acho esse passo desnecessário, dá pra construir M_N sem M_D.


### Build the [Motion Network Matrix]({{< relref "motion_network_matrix" >}}) (M_N) {#build-the-motion-network-matrix--motion-network-matrix-dot-md----m-n}


### Define the [Vector of Motion Parameters]({{< relref "vector_of_motion_parameters" >}}) (\\(\varphi\_M\\)) {#define-the-vector-of-motion-parameters--vector-of-motion-parameters-dot-md-----varphi-m}


### The Kinematics realtions can be found by: {#the-kinematics-realtions-can-be-found-by}

\\[M\_N \ \varphi\_M = 0\\]


## Statics Analysis {#statics-analysis}


### Build the [Action Graph]({{< relref "action_graph" >}}) {#build-the-action-graph--action-graph-dot-md}


### Build the [Cut-Set Matrix]({{< relref "cut_set_matrix" >}}) (Q_a) {#build-the-cut-set-matrix--cut-set-matrix-dot-md----q-a}


### Define the [wrenches]({{< relref "wrench" >}}) of the edges by [Wrench of a Joint]({{< relref "wrench_of_a_joint" >}}). {#define-the-wrenches--wrench-dot-md--of-the-edges-by-wrench-of-a-joint--wrench-of-a-joint-dot-md--dot}


### Build the [Direct Wrenches Matrix]({{< relref "direct_wrenches_matrix" >}}) (A_D) {#build-the-direct-wrenches-matrix--direct-wrenches-matrix-dot-md----a-d}

Acho esse passo desnecessário, dá pra construir A_N sem A_D.


### Build the [Action Network Matrix]({{< relref "action_network_matrix" >}}) (A_N) {#build-the-action-network-matrix--action-network-matrix-dot-md----a-n}


### Define the [Vector of Action Parameters]({{< relref "vector_of_action_parameters" >}}) (\\(\varphi\_A\\)) {#define-the-vector-of-action-parameters--vector-of-action-parameters-dot-md-----varphi-a}


### The Statics relations can be found by: {#the-statics-relations-can-be-found-by}

\\[A\_N \ \varphi\_A = 0\\]


## Coupling Between Kinematics and Statics {#coupling-between-kinematics-and-statics}

There may be a coupling between kinematics and statics, much like in the form of a viscous friction.


## Solving the System {#solving-the-system}


### Build the [Vector of System Parameters]({{< relref "vector_of_system_parameters" >}}) (\\(\varphi\\)) {#build-the-vector-of-system-parameters--vector-of-system-parameters-dot-md-----varphi}


### Build the [Coupled Equations Matrix]({{< relref "coupled_equations_matrix" >}}) (\\(C\_{T\omega}\\)) {#build-the-coupled-equations-matrix--coupled-equations-matrix-dot-md----c-t-omega}


### Build the [System Matrix]({{< relref "system_matrix" >}}) (\\(M\_S\\)) {#build-the-system-matrix--system-matrix-dot-md----m-s}


### The combined equation for Kinematics and Statics can be found by: {#the-combined-equation-for-kinematics-and-statics-can-be-found-by}

\\[M\_S \ \varphi = 0\\]


### Arrange the known parameters to the other side {#arrange-the-known-parameters-to-the-other-side}


#### Localize the known variables {#localize-the-known-variables}


#### Extract the respective column of the known variables and negate it to the other side of the equation. {#extract-the-respective-column-of-the-known-variables-and-negate-it-to-the-other-side-of-the-equation-dot}


#### Now you have: {#now-you-have}

<!--list-separator-->

-  \\(\varphi^\*:\\) \\(\varphi\\) without the extracted variables.

<!--list-separator-->

-  \\(M\_S^\* :\\) \\(M\_S\\) without the columns related to the extracted variables.

<!--list-separator-->

-  \\(b\_S:\\) Other side of the equation with the extracted varibles combined.


### Solve the resulting linear system to compute the Kinematics and Statics {#solve-the-resulting-linear-system-to-compute-the-kinematics-and-statics}

\\[M\_S^\* \ \varphi^\* = b\_s\\]
