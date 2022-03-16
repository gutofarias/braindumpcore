+++
title = "Dynamics Extension for Davies Method"
author = ["João Gutemberg Farias"]
draft = false
+++

Idea I had for extending [Davies Method]({{< relref "davies_method" >}}) which works only for Differential Kinematics and Statics. I wish to extend the formulation to include Dynamics.

My idea is to go through [Hyper-Dual Quaternions]({{< relref "hyper_dual_quaternions" >}}). But I should take a look at [Screw Calculus]({{< relref "screw_calculus" >}}) as well.

Start with a mechanism or robot (can be either a [Open Kinematic Chain System]({{< relref "serial_mechanism" >}}) or a [Closed Kinematic Chain System]({{< relref "closed_kinematic_chain_system" >}}))


## Enumerate the joints and links {#enumerate-the-joints-and-links}

Use letters for the joints and numbers for the links. The earth or [support]({{< relref "base_link" >}}) should be number 0 or 1 (when there is no 0).


## Build the [Coupling Graph]({{< relref "coupling_graph" >}}) {#build-the-coupling-graph--coupling-graph-dot-md}


## Evalute the [degrees of freedom]({{< relref "degrees_of_freedom" >}}) (f) and [constraints]({{< relref "constraints_of_motion" >}}) (c) of each joint. {#evalute-the-degrees-of-freedom--degrees-of-freedom-dot-md----f--and-constraints--constraints-of-motion-dot-md----c--of-each-joint-dot}


## Considerations {#considerations}


### [Joints taken in succession - Davies Method for Dynamics]({{< relref "joints_taken_in_succession_davies_method_for_dynamics" >}}) {#joints-taken-in-succession-davies-method-for-dynamics--joints-taken-in-succession-davies-method-for-dynamics-dot-md}


## Kinematic Analysis {#kinematic-analysis}


### [Understanding Davies Method's kinematic analysis]({{< relref "understanding_davies_method_s_kinematic_analysis" >}}) {#understanding-davies-method-s-kinematic-analysis--understanding-davies-method-s-kinematic-analysis-dot-md}


### [Difference of the approach to Dynamics]({{< relref "difference_of_the_approach_to_dynamics_on_the_kinematic_analysis_davies_method_for_dynamics" >}}) {#difference-of-the-approach-to-dynamics--difference-of-the-approach-to-dynamics-on-the-kinematic-analysis-davies-method-for-dynamics-dot-md}


### Build the [Motion Graph]({{< relref "motion_graph" >}}) {#build-the-motion-graph--motion-graph-dot-md}

In this case the motion graph does not need to take into account the [tree]({{< relref "tree_graph" >}}) configuration.


### For each link {#for-each-link}


#### Choose a graph trajectory {#choose-a-graph-trajectory}

The graph trajectory should go from the [Base Link]({{< relref "base_link" >}}) to the link in consideration.


#### [Considerations of using Hyper-Dual Quaternions/Vectors]({{< relref "considerations_of_using_hyper_dual_quaternions_vectors_davies_method_for_dynamics" >}}) {#considerations-of-using-hyper-dual-quaternions-vectors--considerations-of-using-hyper-dual-quaternions-vectors-davies-method-for-dynamics-dot-md}


#### Define the [Hyper-Dual Twist]({{< relref "hyper_dual_twist" >}}) of the [edges]({{< relref "graph_edge" >}}) using [Hyper-Dual Twist of a Joint]({{< relref "dual_twist_of_a_joint" >}}). Compute the twists relative to the center of mass of the link {#define-the-hyper-dual-twist--hyper-dual-twist-dot-md--of-the-edges--graph-edge-dot-md--using-hyper-dual-twist-of-a-joint--dual-twist-of-a-joint-dot-md--dot-compute-the-twists-relative-to-the-center-of-mass-of-the-link}

Remember you only need the twist of previous joints.


#### Sum up the hyper-dual twists to obtain the kinematics of the center of mass of the link {#sum-up-the-hyper-dual-twists-to-obtain-the-kinematics-of-the-center-of-mass-of-the-link}


## Forces Analysis {#forces-analysis}


### [Understanding Davies Method's statics analysis]({{< relref "understanding_davies_method_s_statics_analysis" >}}) {#understanding-davies-method-s-statics-analysis--understanding-davies-method-s-statics-analysis-dot-md}


### [Difference of the approach to Dynamics in Force Analysins - Davies Method for Dynamics]({{< relref "difference_of_the_approach_to_dynamics_in_force_analysins_davies_method_for_dynamics" >}}) {#difference-of-the-approach-to-dynamics-in-force-analysins-davies-method-for-dynamics--difference-of-the-approach-to-dynamics-in-force-analysins-davies-method-for-dynamics-dot-md}


### Build the [Action Graph]({{< relref "action_graph" >}}) {#build-the-action-graph--action-graph-dot-md}

In this case the motion graph does not need to take into account the [tree]({{< relref "tree_graph" >}}) configuration.


### For each link (using the same sequence of the kinematic analysis) {#for-each-link--using-the-same-sequence-of-the-kinematic-analysis}


#### Make a "circular cut" in the equivalent graph node to account for the efforts acting in the link. {#make-a-circular-cut-in-the-equivalent-graph-node-to-account-for-the-efforts-acting-in-the-link-dot}

The efforts cutted by the circular cut will be considered. Positiviness should be either arrows pointing in the circular cut or arrows pointing out.


#### Define the [wrenches]({{< relref "wrench" >}}) of the edges by [Wrench of a Joint]({{< relref "wrench_of_a_joint" >}}). {#define-the-wrenches--wrench-dot-md--of-the-edges-by-wrench-of-a-joint--wrench-of-a-joint-dot-md--dot}

We do not need to use hyper-dual quatities because we do not want the derivative or integral of the forces.

\\[\hat{F}\_{ij} = \vec{F}\_{ij} + \epsilon \\, \vec{M}\_{ij} \\]


#### Sum up all the wrenches to find the efforts acting in the link {#sum-up-all-the-wrenches-to-find-the-efforts-acting-in-the-link}

\\[ \hat{F}\_i = \sum\_j \hat{F}\_{ij} \\]


### Build the Action Network Matrix (A_N) and the Vector of Action Parameters (\\(\varphi\_A\\)) {#build-the-action-network-matrix--a-n--and-the-vector-of-action-parameters---varphi-a}

Just write the half-equations obtained for the force analysis in a matricial form putting toghether all the half-equations and separating the Vector of Motion Parameters.

Do not change the order of equations.


## Hyper-dual momentum {#hyper-dual-momentum}


### For each link {#for-each-link}


#### Build the [Dual Mass]({{< relref "dual_mass" >}}) of each link as {#build-the-dual-mass--dual-mass-dot-md--of-each-link-as}

\\[ M\_i = {\_I}I\_{i} \\, \epsilon + m\_{i} \\, d\epsilon \\]

Perceba que a utilização dos operadores \\(\epsilon\\) e \\(d\epsilon\\) em conjunto fazem um [swap]({{< relref "dual_swap_operator" >}}) na velocidade linear e angular. O resultado fica:

\\[ M\_i \\, \nu\_i = m\_i \\, \vec{v} + \epsilon \\, {\_I}I\_{i} \\, \vec{\omega} \\]

O que deixa compatível com o wrench que é \\((\vec{F} + \epsilon \\, \vec{M})\\)


#### Build the [Hyper-Dual Mass]({{< relref "hyper_dual_mass" >}}) of each link as {#build-the-hyper-dual-mass--hyper-dual-mass-dot-md--of-each-link-as}

\\[ \check{M}\_i = M\_i + \check{\epsilon} \\, \dot{M}\_i \\]

\\[ \check{M}\_i = {\_I}I\_{i} \\, \epsilon + m\_{i} \\, d\epsilon + \check{\epsilon} \\,  ({\_I}\dot{I}\_{i} \\, \epsilon ) \\]


#### [Considerations over the inertia matrix - Davies Method for Dynamics]({{< relref "considerations_over_the_inertia_matrix_davies_method_for_dynamics" >}}) {#considerations-over-the-inertia-matrix-davies-method-for-dynamics--considerations-over-the-inertia-matrix-davies-method-for-dynamics-dot-md}


#### Find the Hyper-Dual Momentum of each link {#find-the-hyper-dual-momentum-of-each-link}

\\[ \check{P}\_i = \check{M}\_i \\, \check{\nu}\_i \\]

\\[ \check{P} = (M + \check{\epsilon} \\, \dot{M})(\nu + \check{\epsilon} \\, \dot{\nu}) = M \\, \nu + \check{\epsilon} ( M \\, \dot{\nu} + \dot{M} \\, \nu ) \\]


#### Isolate the Hyper-Dual part, which is the acceleration {#isolate-the-hyper-dual-part-which-is-the-acceleration}

\\[ \dot{\hat{P}} = d\check{\epsilon} \\, (\check{P}) =  M \\, \dot{\nu} + \dot{M} \\, \nu \\]


### Build the Motion Network Matrix (\\(M\_N\\)), the Vector of Motion Parameters (\\(\varphi\_M\\)) and the Vector of Independent Terms (\\(b\_M\\)) {#build-the-motion-network-matrix--m-n---the-vector-of-motion-parameters---varphi-m---and-the-vector-of-independent-terms--b-m}

Just write the half-equations obtained for the momenta in a matricial form putting toghether all the half-equations and separating the Vector of Motion Parameters (the accelerations).
The terms that do not contain an explicit second order differential joint variable, should be placed in the Vector of Independent Terms \\(b\_M\\).

The result should be:

\\[ M\_N \\, \varphi\_M + b\_M \\]

Do not change the order of equations.


## Apply Newton's Law and Euler's Law of motion {#apply-newton-s-law-and-euler-s-law-of-motion}

A dual version of Newton's law should be:

\\[ \hat{F}\_i = \dot{\hat{P}}\_i = \frac{d}{dt} [M\_i \\, \nu\_i]  \\]

\\[ \hat{F}\_i - \dot{\hat{P}}\_i = 0 \\]

When we consider all equations in matricial form:

\\[A\_N \\, \varphi\_A - M\_N \\, \varphi\_N - b\_M = 0\\]

\\[ \begin{bmatrix} A\_N & - M\_N \end{bmatrix} \\, \begin{bmatrix} \varphi\_A \\\ \varphi\_N \end{bmatrix} = b\_M \\]


## Case of Parallel Systems {#case-of-parallel-systems}

In that case, we will end-up with more joint variables than motion equations. But the joints variables are related one to the other and we can use the traditional [Davies Method]({{< relref "davies_method" >}}) with [Hyper-Dual Numbers]({{< relref "hyper_dual_numbers" >}}) to find the relations.


### Start by the already made [Coupling Graph]({{< relref "coupling_graph" >}}) {#start-by-the-already-made-coupling-graph--coupling-graph-dot-md}


### Do the kinematic analysis of [Davies Method]({{< relref "davies_method" >}}) but using [Hyper-Dual Twist of a Joint]({{< relref "dual_twist_of_a_joint" >}}) instead of the traditional twist. {#do-the-kinematic-analysis-of-davies-method--davies-method-dot-md--but-using-hyper-dual-twist-of-a-joint--dual-twist-of-a-joint-dot-md--instead-of-the-traditional-twist-dot}


### Isolate the Hyper-Dual part, which is the acceleration {#isolate-the-hyper-dual-part-which-is-the-acceleration}

\\[ \dot{\nu} = d\check{\epsilon} \\, (\check{\nu}) =  \dot{\omega} + \epsilon \\, \dot{v} \\]


### Build the [Motion Network Matrix]({{< relref "motion_network_matrix" >}}) (\\(M\_{N}^\*\\)) {#build-the-motion-network-matrix--motion-network-matrix-dot-md----m-n}


### The Kinematics realtions can be found by: {#the-kinematics-realtions-can-be-found-by}

\\[M\_N^\* \ \varphi\_M = 0\\]


## Final System {#final-system}


### Serial Mechanisms {#serial-mechanisms}

\\[ \begin{bmatrix} A\_N & - M\_N \end{bmatrix} \\, \begin{bmatrix} \varphi\_A \\\ \varphi\_N \end{bmatrix} = b\_M \\]

\\(M\_S : \begin{bmatrix} A\_N & - M\_N \end{bmatrix}\\)

\\(\varphi : \begin{bmatrix} \varphi\_A \\\ \varphi\_N \end{bmatrix}\\)

\\(b : b\_M\\)

\\[ M\_S \ \varphi = b \\]


### Parallel mechanisms {#parallel-mechanisms}

Increase the previous system to add the relations between the joints variables in a parallel system.

\\[ \begin{bmatrix}  A\_N  & - M\_N  \\\ 0 & M\_N^\*  \end{bmatrix}
\\, \begin{bmatrix} \varphi\_A \\\ \varphi\_N \end{bmatrix} = \begin{bmatrix} b\_M \\\ 0 \end{bmatrix} \\]

\\(M\_S : \begin{bmatrix}  A\_N  & - M\_N  \\\ 0 & M\_N^\*  \end{bmatrix}\\)

\\(\varphi : \begin{bmatrix} \varphi\_A \\\ \varphi\_N \end{bmatrix}\\)

\\(b : \begin{bmatrix} b\_M \\\ 0 \end{bmatrix}\\)

\\[ M\_S \ \varphi = b \\]


## Solving the System {#solving-the-system}


### Arrange the known parameters to the other side {#arrange-the-known-parameters-to-the-other-side}


#### Localize the known variables {#localize-the-known-variables}


#### Extract the respective column of the known variables and negate it to the other side of the equation. {#extract-the-respective-column-of-the-known-variables-and-negate-it-to-the-other-side-of-the-equation-dot}


#### Now you have: {#now-you-have}

<!--list-separator-->

-  \\(\varphi^\*:\\) \\(\varphi\\) without the extracted variables.

<!--list-separator-->

-  \\(M\_S^\* :\\) \\(M\_S\\) without the columns related to the extracted variables.

<!--list-separator-->

-  \\(b\_S:\\) Other side of the equation with the extracted varibles combined plus \\(b\\)


### Solve the resulting linear system to compute the Kinematics and Statics {#solve-the-resulting-linear-system-to-compute-the-kinematics-and-statics}

\\[M\_S^\* \ \varphi^\* = b\_s\\]


## Considerações adicionais sobre a técnica {#considerações-adicionais-sobre-a-técnica}


### [Como tratar casos de quebra de continuidade nos referenciais móveis]({{< relref "loss_of_continuity_in_mobile_frames_davies_method_for_dynamics" >}}) {#como-tratar-casos-de-quebra-de-continuidade-nos-referenciais-móveis--loss-of-continuity-in-mobile-frames-davies-method-for-dynamics-dot-md}


### [Integração com o método dos helicóides successivos]({{< relref "integration_with_successive_screws_method_davies_method_for_dynamics" >}}) {#integração-com-o-método-dos-helicóides-successivos--integration-with-successive-screws-method-davies-method-for-dynamics-dot-md}


### Ver se existe integração possível com [Screw Calculus]({{< relref "screw_calculus" >}}) {#ver-se-existe-integração-possível-com-screw-calculus--screw-calculus-dot-md}


### Ler o trabalho do Prof Daniel sobre o Método de Davies {#ler-o-trabalho-do-prof-daniel-sobre-o-método-de-davies}
