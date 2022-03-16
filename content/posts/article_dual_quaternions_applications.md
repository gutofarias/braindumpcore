+++
title = "Article - Dual Quaternions Applications"
author = ["João Gutemberg Farias"]
draft = false
+++

Esboço do artigo de revisão que estou fazendo sobre [Dual Quaternions Applications]({{< relref "dual_quaternions_applications" >}}).


## Introdução <code>[0/1]</code> {#introdução}


### <span class="org-todo todo TODO">TODO</span> <sup id="a666c7a16141742141ff61342199d764"><a href="#figueredo_robust_2013" title="Figueredo, Adorno, Ishihara \&amp; Borges, Robust Kinematic Control of Manipulator Robots Using Dual Quaternion Representation, 1949--1955, in in: {Robotics and {{Automation}} ({{ICRA}}), 2013 {{IEEE International Conference}} On}, edited by {IEEE} (2013)">figueredo_robust_2013</a></sup> {#943110}

A introdução desse trabalho é muito boa


## Medical Applications <code>[0/2]</code> {#medical-applications}

Acho que não vou usar


### <span class="org-todo todo TODO">TODO</span> <sup id="643835c6bb62493a58aba8836a303f78"><a href="#birlescu2020" title="Birlescu, Husty, Vaida, Gherman, Tucan \&amp; Pisla, Joint-{{Space Characterization}} of a {{Medical Parallel Robot Based}} on a {{Dual Quaternion Representation}} of {{SE}}(3), {Mathematics}, v(7), 1086 (2020).">birlescu2020</a></sup> {#38f649}

Muito grande. Não li. Só sei que usa os [parâmetros de Study]({{< relref "study_parameters" >}}) e aplica num [robô médico paralelo]({{< relref "parallel_mechanisms" >}})


### <span class="org-todo todo TODO">TODO</span> <sup id="4a1c9c09af4e1abc9e96d6a4d4dacfd4"><a href="#husty2019" title="Husty, Birlescu, Tucan, Vaida \&amp; Pisla, An Algebraic Parameterization Approach for Parallel Robots Analysis, {Mechanism and Machine Theory}, v(), 245--257 (2019).">husty2019</a></sup> {#648390}

The authors proposes a new method to parametrize parallel mechanisms using Study parameters, applying it in a mechanism to help in the lower limb rehabilitation process of post-stroke patients.


## Vantagens <code>[1/2]</code> {#vantagens}


### <span class="org-todo done DONE">DONE</span> Comparação com HTM <code>[3/3]</code> {#comparação-com-htm}


#### <span class="org-todo done DONE">DONE</span> <sup id="5ede57612c8e5d5c19c55dbc76a8853a"><a href="#pham2018" title="Pham, Adorno, Perdereau \&amp; Fraisse, Set-Point Control of Robot End-Effector Pose Using Dual Quaternion Feedback, {Robotics and Computer-Integrated Manufacturing}, v(), 100--110 (2018).">pham2018</a></sup> {#d608e6}

The proposed controller is tested using DQ and HTM. The result is that the DQ controller is almost twice as fast to compute.


#### <span class="org-todo done DONE">DONE</span> <sup id="b52bc18b61897fe939bc7b74acf0aa7c"><a href="#yacob2020" title="Yacob \&amp; Semere, Variation Compensation in Machining Processes Using Dual Quaternions, {Procedia CIRP}, v(), 879--884 (2020).">yacob2020</a></sup> {#640716}

The common way to compensate variation is using HTM. Using DQ the modeling of the problem became easier as some steps became unnecessary obtaining the same result. Also, DQ allowed to analize other types of form error which the classical model can not analize.


#### <span class="org-todo done DONE">DONE</span> <sup id="a88a6598a0751d7ebb8eff58fcc3bf61"><a href="#mirandadefarias2019" title="Miranda de Farias, da Cruz Figueredo \&amp; Yoshiyuki Ishihara, Performance {{Study}} on {{dqRNEA}} \textendash{} {{A Novel Dual Quaternion Based Recursive Newton}}-{{Euler Inverse Dynamics Algorithms}}, 94--101, in in: {2019 {{Third IEEE International Conference}} on {{Robotic Computing}} ({{IRC}})}, edited by {IEEE} (2019)">mirandadefarias2019</a></sup> {#2d7915}

The performance of the algorithm using DQ is compared to using HTM, and the result is favorable to DQ, maybe like 33% less cost in terms of number of operations.


### <span class="org-todo todo TODO">TODO</span> Técnica usando DQ melhor do que as mais comuns <code>[0/3]</code> {#técnica-usando-dq-melhor-do-que-as-mais-comuns}


#### <span class="org-todo todo TODO">TODO</span> <sup id="597bcef833a6d040afcef41bc2a99cf9"><a href="#wang2018" title="Wang, Liu \&amp; Han, A {{Method}} of {{Robot Base Frame Calibration}} by {{Using Dual Quaternion Algebra}}, {IEEE Access}, v(), 74865--74873 (2018).">wang2018</a></sup> {#bcb023}

Method for frame calibration:
The result was much favorable to the dual quaternion method when compared to a quaternion method and a Procrustes Analysis. The authors credits the higher precision of dual quaternions due to the fact that it computes rotation and translation coupled, so there is no error propagation when computing one and using the result to compute the other.


#### <span class="org-todo todo TODO">TODO</span> <sup id="497f6a856013fed14901b2617bc355c8"><a href="#fu2020" title="Fu, Pan, Spyrakos-Papastavridis, Chen \&amp; Li, A {{Dual Quaternion}}-{{Based Approach}} for {{Coordinate Calibration}} of {{Dual Robots}} in {{Collaborative Motion}}, {IEEE Robot. Autom. Lett.}, v(3), 4086--4093 (2020).">fu2020</a></sup> {#aa81ae}

The article concludes that the DQ methodology offers higher calibration accurary when compared to existing methods.


#### <span class="org-todo todo TODO">TODO</span> <sup id="414c8095cc4a3998b0a6858d107d87a8"><a href="#schwung2021" title="Schwung, Poppelbaum \&amp; Nutakki, Rigid {{Body Movement Prediction Using Dual Quaternion Recurrent Neural Networks}}, 756--761, in in: {2021 22nd {{IEEE International Conference}} on {{Industrial Technology}} ({{ICIT}})}, edited by {IEEE} (2021)">schwung2021</a></sup> {#bb562d}

It applies two different neural networks, a DQ Recurrent NN (DQRNN) and a DQ Long Short Term Memory NN (DQLSTM). DQLSTM obtained a higher accuracy than DQRNN and when we compare it with a normal LSTM the DQLSTM got half the [root mean square error (RMSE)]({{< relref "root_mean_square_error" >}}). So it performed really well.


## Hyper-Dual Numbers <code>[1/1]</code> {#hyper-dual-numbers}


### <span class="org-todo done DONE">DONE</span> <sup id="534fc4e2534d5702b6afc1d74746f0b9"><a href="#cohen2020" title="Cohen \&amp; Shoham, Hyper {{Dual Quaternions}} Representation of Rigid Bodies Kinematics, {Mechanism and Machine Theory}, v(), 103861 (2020).">cohen2020</a></sup> {#4d6276}

The authors applies for the first time Hyper-Dual Quaternions. Finding a compact representation of pose and its derivative in a single element. Being able to compute kinematics and differential kinematics in only one pass.


## Origami <code>[3/3]</code> {#origami}


### <span class="org-todo done DONE">DONE</span> <sup id="89ceacc7dafe9653593b9cfd99bd2637"><a href="#cai2016" title="Cai, Zhang, Xu, Zhou \&amp; Feng, The {{Foldability}} of {{Cylindrical Foldable Structures Based}} on {{Rigid Origami}}, {Journal of Mechanical Design}, v(3), 031401 (2016).">cai2016</a></sup> {#81df0a}

The authors develop a method to check for the rigid foldability of multi-vertex cylindrical origami using dual quaternions. It's a multi step method, one of the steps uses quaternions and the other uses dual quaternions.


### <span class="org-todo done DONE">DONE</span> <sup id="74ae13da79b7fc820b521f6e8e3e4f4b"><a href="#jianguo2017" title="Jianguo, Yangqing, Ruijun, Jian \&amp; Ya, Nonrigidly {{Foldability Analysis}} of {{Kresling Cylindrical Origami}}, {Journal of Mechanisms and Robotics}, v(4), 041018 (2017).">jianguo2017</a></sup> {#3b3324}

The paper studies the rigid foldability of a cylindrical origami with Kresling patterns concluding that it is not rigidly foldable. DQs are used in the method that analyses the ridid foldability.


### <span class="org-todo done DONE">DONE</span> <sup id="2d247d8e5df74fef24286999199d25cb"><a href="#wu2010" title="Wu \&amp; You, Modelling Rigid Origami with Quaternions and Dual Quaternions, {Proc. R. Soc. A.}, v(2119), 2155--2174 (2010).">wu2010</a></sup> {#710941}

The work uses the correspondence between single-vertex rigid origami and spherical linkage to model it as quaternions and the correspondence of multi-vertex rigid origami and spatial linkage to model it as dual quaternions.


## DQ Neural Networks <code>[2/2]</code> {#dq-neural-networks}


### <span class="org-todo done DONE">DONE</span> <sup id="4249a347fccdd66742ec1aa617d662bd"><a href="#schilling2019" title="Schilling, Hierarchical {{Dual Quaternion}}-{{Based Recurrent Neural Network}} as a {{Flexible Internal Body Model}}, 1--8, in in: {2019 {{International Joint Conference}} on {{Neural Networks}} ({{IJCNN}})}, edited by {IEEE} (2019)">schilling2019</a></sup> {#123bac}

The author uses Mean of Multiple Computations (MMC) as a hierarchical recurrent neural network to model a redundant robot. The technique generates a lot of simple equations that converge to a feasible solution where there are many ways for the same pose of the end-effector.
Using dual quaternions components in the neural network, the author can approximate transformations by interpolation, which is shown to be a great advantage of DQs.
At the end, the author shows the viability of the proposed solution applying it to a complex robot consisting of two arms each having 7 DoF.


### <span class="org-todo done DONE">DONE</span> <sup id="414c8095cc4a3998b0a6858d107d87a8"><a href="#schwung2021" title="Schwung, Poppelbaum \&amp; Nutakki, Rigid {{Body Movement Prediction Using Dual Quaternion Recurrent Neural Networks}}, 756--761, in in: {2021 22nd {{IEEE International Conference}} on {{Industrial Technology}} ({{ICIT}})}, edited by {IEEE} (2021)">schwung2021</a></sup> {#bb562d}

The work uses [Dual-Quaternions Neural Networks]({{< relref "dual_quaternions_neural_networks" >}}) to predict the behavior (physics) of a simulated system of masses inside a box. So the neural network predicts rigid body movement.

The authors say that using DQ in a neural network allows to incorporate physical bias into the prediction task. I.e., just by using the DQ we are already favoring the task of rigid body movement prediction, due to how DQ relates to this task.

It applies two different neural networks, a DQ Recurrent NN (DQRNN) and a DQ Long Short Term Memory NN (DQLSTM). DQLSTM obtained a higher accuracy than DQRNN and when we compare it with a normal LSTM the DQLSTM got half the [root mean square error (RMSE)]({{< relref "root_mean_square_error" >}}). So it performed really well.


## Machining  <code>[2/2]</code> {#machining}


### <span class="org-todo done DONE">DONE</span> <sup id="843b40f21c59e2f067805967760a54ca"><a href="#zhao2017" title="Zhao, Zhao, Li \&amp; Ding, Path Smoothing for Five-Axis Machine Tools Using Dual Quaternion Approximation with Dominant Points, {Int. J. Precis. Eng. Manuf.}, v(5), 711--720 (2017).">zhao2017</a></sup> {#3a3359}

The paper proposes a dual quaternion B-Spline approximation method for using in five-axis CNC machines. The advantages of the method are: reduced computation time, reduced storage consuption, reduced number of control points. Also using the dual quaternionic method can eliminate the fitting oscillatory and solve the parameter synchronization problem simultaneously (no idea what this two mean).


### <span class="org-todo done DONE">DONE</span> <sup id="b52bc18b61897fe939bc7b74acf0aa7c"><a href="#yacob2020" title="Yacob \&amp; Semere, Variation Compensation in Machining Processes Using Dual Quaternions, {Procedia CIRP}, v(), 879--884 (2020).">yacob2020</a></sup> {#640716}

The authors use DQ to compensate for variations in machining process. The variations are differences between the ideal/projected piece and the obtained through machining.
The common way to compensate variation is using HTM. Using DQ the modeling of the problem became easier as some steps became unnecessary obtaining the same result. Also, DQ allowed to analize other types of form error which the classical model can not analize.


## Motion Planning <code>[1/1]</code> {#motion-planning}


### <span class="org-todo done DONE">DONE</span> <sup id="424b1f73619bc284e79679d73ad7f225"><a href="#oh_study_2017" title="Oh, Abhishesh \&amp; Ryuh, Study on {{Robot Trajectory Planning}} by {{Robot}} {{End}}-{{Effector Using Dual Curvature Theory}} of the {{Ruled Surface}}, {International Journal of Mechanical and Materials Engineering}, v(3), 6 (2017).">oh_study_2017</a></sup> {#cfe225}

Alternatively to motion interpolation, <sup id="424b1f73619bc284e79679d73ad7f225"><a href="#oh_study_2017" title="Oh, Abhishesh \&amp; Ryuh, Study on {{Robot Trajectory Planning}} by {{Robot}} {{End}}-{{Effector Using Dual Curvature Theory}} of the {{Ruled Surface}}, {International Journal of Mechanical and Materials Engineering}, v(3), 6 (2017).">oh_study_2017</a></sup> uses differential geometry and dual curvature theory. The author claims that it makes the expressions simpler and intuitive.


## Robotics <code>[3/4]</code> {#robotics}


### <span class="org-todo done DONE">DONE</span> Dual Robots <code>[2/2]</code> {#dual-robots}


#### <span class="org-todo done DONE">DONE</span> <sup id="a4dceea8d49ed091b58811d886fc3444"><a href="#chandra2018" title="Chandra, Mateo, Corrales-Ramon \&amp; Mezouar, Dual-{{Arm Coordination Using Dual Quaternions}} and {{Virtual Mechanisms}}, 759--765, in in: {2018 {{IEEE International Conference}} on {{Robotics}} and {{Biomimetics}} ({{ROBIO}})}, edited by {IEEE} (2018)">chandra2018</a></sup> {#454b9c}

The work uses what I think can be classified as a [Dual Robot]({{< relref "dual_robots" >}}) but they call a Dual-Arm robot. The authors use DQ to describe and control the coordinated motion of the arms of the robot.
In order to do that, the work defines three reference frames and uses [Relative Jacobians]({{< relref "relative_jacobian" >}}). Also they parametrize the task to be performed by a [Virtual Mechanism]({{< relref "virtual_mechanism" >}}) that conects both arms. It is an interesting idea, since by doing that they can impose restrictions to the robot arms movement by the layout of the virtual mechanism. So by using this, the whole modeling looks like a two [chains]({{< relref "kinematic_chains" >}}) parallel robot.


#### <span class="org-todo done DONE">DONE</span> <sup id="497f6a856013fed14901b2617bc355c8"><a href="#fu2020" title="Fu, Pan, Spyrakos-Papastavridis, Chen \&amp; Li, A {{Dual Quaternion}}-{{Based Approach}} for {{Coordinate Calibration}} of {{Dual Robots}} in {{Collaborative Motion}}, {IEEE Robot. Autom. Lett.}, v(3), 4086--4093 (2020).">fu2020</a></sup> {#aa81ae}


### <span class="org-todo done DONE">DONE</span> SLAM <code>[2/2]</code> {#slam}


#### <span class="org-todo done DONE">DONE</span> <sup id="f81900bfc159c2c268a8aa36c1082377"><a href="#cheng2016" title="Cheng, Kim, Jiang \&amp; Che, Dual Quaternion-Based Graphical {{SLAM}}, {Robotics and Autonomous Systems}, v(), 15--24 (2016).">cheng2016</a></sup> {#85d11c}

Parametrizes the [SLAM (Simultaneous Location and Mapping)]({{< relref "simultaneous_localization_and_mapping_slam" >}}) problem using dual-quaternions instead of [HTM]({{< relref "homogeneous_transformation_matrix" >}}). The problem is solved through a [graph]({{< relref "graph_theory" >}}) approach that in the DQ formulation can have DQs in the vertices and in the edges, because DQs can represent both the state and the restrictions. The proposed solution improves the computational performance when compared to the same approach using HTM.


#### <span class="org-todo done DONE">DONE</span> <sup id="f0a1695fbd59e42430ca9ed7ce39a984"><a href="#bultmann2019" title="Bultmann, Li \&amp; Hanebeck, Stereo {{Visual SLAM Based}} on {{Unscented Dual Quaternion Filtering}}, v(), 8 (2019).">bultmann2019</a></sup> {#f5446e}

[SLAM]({{< relref "simultaneous_localization_and_mapping_slam" >}}) using an DQ unscented filter and using the stero visual data.
Não tenho muito a dizer porque não li muito.


### <span class="org-todo done DONE">DONE</span> Aerial Manipulator <code>[1/1]</code> {#aerial-manipulator}


#### <span class="org-todo done DONE">DONE</span> <sup id="9b8b8f5b8e41c78bd18104de4e60cedc"><a href="#abaunza2017" title="Abaunza, Castillo, Victorino \&amp; Lozano, Dual {{Quaternion Modeling}} and {{Control}} of a {{Quad}}-Rotor {{Aerial Manipulator}}, {J Intell Robot Syst}, v(2-4), 267--283 (2017).">abaunza2017</a></sup> {#9cdc4b}

The work presents modeling and control of a quadcopter with an robotic arm attached, forming a aerial manipulator. Both modeling and control uses dual quaternions.
The work is very similar to <sup id="c5131fa61eb5d7177d4fdf0d017a8cb7"><a href="#abaunza_quadrotor_2016" title="Abaunza, Castillo, Lozano \&amp; Victorino, Quadrotor Aerial Manipulator Based on Dual Quaternions, 152--161, in in: {Unmanned {{Aircraft Systems}} ({{ICUAS}}), 2016 {{International Conference}} On}, edited by {IEEE} (2016)">abaunza_quadrotor_2016</a></sup> (same authors)


### <span class="org-todo todo TODO">TODO</span> Set-Point Control <code>[0/1]</code> {#set-point-control}


#### <span class="org-todo todo TODO">TODO</span> <sup id="5ede57612c8e5d5c19c55dbc76a8853a"><a href="#pham2018" title="Pham, Adorno, Perdereau \&amp; Fraisse, Set-Point Control of Robot End-Effector Pose Using Dual Quaternion Feedback, {Robotics and Computer-Integrated Manufacturing}, v(), 100--110 (2018).">pham2018</a></sup> {#d608e6}

The paper implements a [set-point controller]({{< relref "set_point_controller" >}}) for an industrial 6DOF robot using Dual Quaternions. The authors computes the [direct kinematics]({{< relref "direct_kinematics" >}}) using DQ and [differential kinematics]({{< relref "differential_kinematics" >}}) using DQ as vectors in R8. The error equation is manipulated in order to obtain a matrix times a variable, but the matrix represents the system dynamics. This matrix is then writen in Laplace Domain and becomes a [Transference Matrix]({{< relref "transference_matrix" >}}), so Classic Control techniques can be used. Using this approach, two different control laws are generated using the [Jacobian Matrix]({{< relref "jacobian_matrix" >}}) (which are compared). The authors state that the proposed controllers does not have the best performance, compared to more sophisticated controllers, but it is simple to implement and using Laplace it is possible to tune the controller using dynamic system parameteres as damping factor and natural frequency.


## Estimation <code>[3/3]</code> {#estimation}


### <span class="org-todo done DONE">DONE</span> <sup id="6cc334e272a3940da00d7d02b1c606ed"><a href="#sveier2018" title="Sveier \&amp; Egeland, Pose {{Estimation}} Using {{Dual Quaternions}} and {{Moving Horizon Estimation}}, {IFAC-PapersOnLine}, v(13), 186--191 (2018).">sveier2018</a></sup> {#59fdfc}

The author presents a [Moving Horizon Estimator]({{< relref "moving_horizon_estimator_mhe" >}}) for [pose estimation]({{< relref "pose_estimation" >}}) using Dual Quaternions. They were able to formulate the [cost function]({{< relref "cost_function" >}}) in terms of the DQ product and so satisfying the unitaryness constraint. Also they discretize the DQ and used a Caley transform presented in an article of Selig.
The resulting estimator was more accurate them DQ-MEKF (DQ Multiplicative Extended Kalman Filter) and T-UKF (Twistor-bases Unscented Kalman Filter) which the author attributes to the moving horizon strategy (so not only the last result is used).


### <span class="org-todo done DONE">DONE</span> <sup id="816b389312aa70e77ba23e9dcfdc36a8"><a href="#dong2019" title="Dong, Hu, Akella \&amp; Mazenc, Partial {{Lyapunov Strictification}}: {{Dual}}-{{Quaternion}}-{{Based Observer}} for 6-{{DOF Tracking Control}}, {IEEE Trans. Contr. Syst. Technol.}, v(6), 2453--2469 (2019).">dong2019</a></sup> {#3d2296}

The authors develop a Dual Quaternion based 6-DOF observer and controller. The controller has a PD-like structure. The observer and controller are validated through simulation of a spacecraft in absensce of both translational and angular velocity measurements.


### <span class="org-todo done DONE">DONE</span> <sup id="8b40081c0d2bed67397c17a806abd466"><a href="#sveier2020" title="Sveier \&amp; Egeland, Dual {{Quaternion Particle Filtering}} for {{Pose Estimation}}, {IEEE Trans. Contr. Syst. Technol.}, v(), 1--14 (2020).">sveier2020</a></sup> {#7a6200}

The authors develop a Dual Quaternion [Particle Filter]({{< relref "particle_filter" >}}) and test it in the [pose estimation]({{< relref "pose_estimation" >}}) of a hanging payload using point clouds data from a Kinect. The pose estimation is then validated showing accurate results.


## Calibration <code>[2/2]</code> {#calibration}


### <span class="org-todo done DONE">DONE</span> <sup id="597bcef833a6d040afcef41bc2a99cf9"><a href="#wang2018" title="Wang, Liu \&amp; Han, A {{Method}} of {{Robot Base Frame Calibration}} by {{Using Dual Quaternion Algebra}}, {IEEE Access}, v(), 74865--74873 (2018).">wang2018</a></sup> {#bcb023}

The work proposes a method for calibrating the transformation between the [inertial/world frame]({{< relref "inertial_frame" >}}) and the [robot frame]({{< relref "body_frame" >}}). It uses a sensor to measure the position of the [end-effector]({{< relref "end_link" >}}) and calibrates the dual quaternion resposible to acheive the transformation.

The result was much favorable to the dual quaternion method when compared to a quaternion method and a Procrustes Analysis. The authors credits the higher precision of dual quaternions due to the fact that it computes rotation and translation coupled, so there is no error propagation when computing one and using the result to compute the other.


### <span class="org-todo done DONE">DONE</span> <sup id="497f6a856013fed14901b2617bc355c8"><a href="#fu2020" title="Fu, Pan, Spyrakos-Papastavridis, Chen \&amp; Li, A {{Dual Quaternion}}-{{Based Approach}} for {{Coordinate Calibration}} of {{Dual Robots}} in {{Collaborative Motion}}, {IEEE Robot. Autom. Lett.}, v(3), 4086--4093 (2020).">fu2020</a></sup> {#aa81ae}

Interesting article about coordinate calibration of [dual robots]({{< relref "dual_robots" >}}) using dual quaternions. The problem itself is very interesting, we have two robot coordinates system, one camera coordinate system and one coordinate system relative to the object being held. So in order to relate all this coordinates systems and assure that they are calibrated, the authors calibrate a hand-eye, a robot-robot and a tool-flange transformations.


## Formation Control <code>[2/2]</code> {#formation-control}


### <span class="org-todo done DONE">DONE</span> <sup id="bc527fe28b161aa5db1129e3156c6a16"><a href="#giribet2021" title="Giribet, Colombo, Moreno, Mas \&amp; Dimarogonas, Dual {{Quaternion Cluster}}-{{Space Formation Control}}, {IEEE Robot. Autom. Lett.}, v(), 1--1 (2021).">giribet2021</a></sup> {#d370c3}

The authors present a cluster-space formation control and apply it to leader-follower configuration using dual quaternions and reducing steady-state errors when compared to previous works. Experiments are made to validade the formation control using a ground and an aerial vehicles, and using two aerial vehicles.


### <span class="org-todo done DONE">DONE</span> <sup id="00f39b5169f2732fdc4ff7583047a966"><a href="#huang2017" title="Huang, Yan, Zhou \&amp; Yang, Dual-Quaternion Based Distributed Coordination Control of Six-{{DOF}} Spacecraft Formation with Collision Avoidance, {Aerospace Science and Technology}, v(), 443--455 (2017).">huang2017</a></sup> {#6d3872}

The work proposes a [formation control]({{< relref "formation_control" >}}) using dual quaternions, the formation error is controlled through a [sliding modes controller]({{< relref "sliding_modes" >}}) and one term is added for [collision avoidance]({{< relref "collision_avoidance" >}}) using [Artificial Potential Function]({{< relref "artificial_potential_function" >}}).


## Whole-Body <code>[1/1]</code> {#whole-body}


### <span class="org-todo done DONE">DONE</span> <sup id="747e94e6940d1d9117cd49b9b40b1669"><a href="#silva2018" title="Silva \&amp; Adorno, Whole-Body {{Control}} of a {{Mobile Manipulator Using Feedback Linearization}} and {{Dual Quaternion Algebra}}, {J Intell Robot Syst}, v(2), 249--262 (2018).">silva2018</a></sup> {#b032a7}

The papers proposes a [whole-body control]({{< relref "whole_body_control" >}}) using [Feedback Linearization]({{< relref "feedback_linearization" >}}) in a DQ framework. Experiments are made using a nonholonomic mobile ground vehicle with 5-DOF [manipulator arm]({{< relref "serial_mechanism" >}}).


## Aerospace <code>[4/4]</code> {#aerospace}


### <span class="org-todo done DONE">DONE</span> <sup id="a7397c53ce111ae612c0c747cdd4f42e"><a href="#dong2018" title="Dong, Hu \&amp; Akella, Dual-{{Quaternion}}-{{Based Spacecraft Autonomous Rendezvous}} and {{Docking Under Six}}-{{Degree}}-of-{{Freedom Motion Constraints}}, {Journal of Guidance, Control, and Dynamics}, v(5), 1150--1162 (2018).">dong2018</a></sup> {#f8feeb}

The work shows the control of a [Rendezvous and Docking]({{< relref "rendezvous_and_docking" >}}) process using dual quaternions to describe the kinematics and formulate two restrictions, one for the line of sight of the chaser to the target spacecraft and other to ensure a safe approach path from the chaser to the target in order to not hit any external equipament of the target. The authors use Artificial Potential Functions to formulate the control problem and perform a [Lyapunov Stability Analysis]({{< relref "lyapunov_stability_analysis" >}}).


### <span class="org-todo done DONE">DONE</span> <sup id="a9415d881eb3c65938675574eded8747"><a href="#valverde2018" title="Valverde \&amp; Tsiotras, Dual {{Quaternion Framework}} for {{Modeling}} of {{Spacecraft}}-{{Mounted Multibody Robotic Systems}}, {Front. Robot. AI}, v(), 128 (2018).">valverde2018</a></sup> {#59d396}

The work describes an framework to derive the dynamics of a satellite, but it can be used to a general serial mechanism (at least I think), the proposed framework works with revolute, prismatic, cylindrical, spherical and planar joints. The equations are computed using dual quaternions and [Newton-Euler formulation]({{< relref "newton_euler_method" >}}).


### <span class="org-todo done DONE">DONE</span> <sup id="961cfc7a1f3349013177b65701226deb"><a href="#sun2020" title="Sun, Wu, Chen, Hao, Mantey \&amp; Zhao, Dual Quaternion Based Dynamics Modeling for Electromagnetic Collocated Satellites of Diffraction Imaging on Geostationary Orbit, {Acta Astronautica}, v(), 52--58 (2020).">sun2020</a></sup> {#131500}

Uses dual quaternions to model an eletromagnetic force with applications in satellites. Also derives the dynamics equations of the satellites subject to this force.


### <span class="org-todo done DONE">DONE</span> <sup id="b82e61e20b87e3bbb72a4417d1e3b640"><a href="#reynolds2020" title="Reynolds, Szmuk, Malyuta, Mesbahi, A\c c\ikme\c se \&amp; Carson, Dual {{Quaternion}}-{{Based Powered Descent Guidance}} with {{State}}-{{Triggered Constraints}}, {Journal of Guidance, Control, and Dynamics}, v(9), 1584--1599 (2020).">reynolds2020</a></sup> {#ad663c}

It uses dual quaternions in the [powered descent guidance]({{< relref "powered_descent_guidance" >}}) problem. The article uses several restrictions in the control formulation, it uses a [line-of-sight]({{< relref "line_of_sight_restriction" >}}) restriction (a new type they call slant-range-triggered line-of-sight), also a restriction as a window for the allowed values of the control effort (propulsion power). The control problem is solved through a nonconvex optimization problem.


## Control <code>[0/0]</code> {#control}


### Erro <code>[1/1]</code> {#erro}


#### <span class="org-todo done DONE">DONE</span> <sup id="a666c7a16141742141ff61342199d764"><a href="#figueredo_robust_2013" title="Figueredo, Adorno, Ishihara \&amp; Borges, Robust Kinematic Control of Manipulator Robots Using Dual Quaternion Representation, 1949--1955, in in: {Robotics and {{Automation}} ({{ICRA}}), 2013 {{IEEE International Conference}} On}, edited by {IEEE} (2013)">figueredo_robust_2013</a></sup> {#943110}

Nova métrica de erro


### MPC <code>[1/1]</code> {#mpc}


#### <span class="org-todo done DONE">DONE</span> <sup id="1698b27182529f1933204f1b88e999a1"><a href="#lee_optimal_2015" title="Lee \&amp; Mesbahi, Optimal {{Power Descent Guidance}} with 6-{{DoF Line}} of {{Sight Constraints}} via {{Unit Dual Quaternions}}, in in: {{{AIAA Guidance}}, {{Navigation}}, and {{Control Conference}}}, edited by {American Institute of Aeronautics and Astronautics} (2015)">lee_optimal_2015</a></sup> {#4905c8}

Citar junto de <sup id="e5d268641d698c2ba96ef845d1523876"><a href="#lee_constrained_2017" title="Lee \&amp; Mesbahi, Constrained {{Autonomous Precision Landing}} via {{Dual Quaternions}} and {{Model Predictive Control}}, {Journal of Guidance, Control, and Dynamics}, v(2), 292--308 (2017).">lee_constrained_2017</a></sup>.


### Kinematic Control <code>[1/1]</code> {#kinematic-control}


#### <span class="org-todo done DONE">DONE</span> <sup id="33cbc6f7bc59ab3b6dddeb95d9d74a7c"><a href="#ozgur2016" title="\Ozg\ur \&amp; Mezouar, Kinematic Modeling and Control of a Robot Arm Using Unit Dual Quaternions, {Robotics and Autonomous Systems}, v(), 66--73 (2016).">ozgur2016</a></sup> {#4501f1}

Tá na parte de Serial Mechanism


### Feedback Linearization <code>[2/2]</code> {#feedback-linearization}


#### <span class="org-todo done DONE">DONE</span> <sup id="250c67f44896242e9eb11b93a1064f7e"><a href="#antonello2018" title="Antonello, Michieletto, Antonello \&amp; Cenedese, A {{Dual Quaternion Feedback Linearized Approach}} for {{Maneuver Regulation}} of {{Rigid Bodies}}, {IEEE Control Syst. Lett.}, v(3), 327--332 (2018).">antonello2018</a></sup> {#605165}

The work proposes a [Maneuver Regulation]({{< relref "maneuver_regulation" >}}) Feedback Linearization Controller using dual quaternions for a 6Dof free body. The results show better results for the Maneuver Regulation than the [Trajectory Tracking]({{< relref "trajectory_tracking" >}}).


#### <span class="org-todo done DONE">DONE</span> <sup id="747e94e6940d1d9117cd49b9b40b1669"><a href="#silva2018" title="Silva \&amp; Adorno, Whole-Body {{Control}} of a {{Mobile Manipulator Using Feedback Linearization}} and {{Dual Quaternion Algebra}}, {J Intell Robot Syst}, v(2), 249--262 (2018).">silva2018</a></sup> {#b032a7}


### Backstepping <code>[1/1]</code> {#backstepping}


#### <span class="org-todo done DONE">DONE</span> <sup id="d65d8a99efce5572c9ab01631f1051cd"><a href="#stianandersen2018" title="Stian Andersen, Johansen \&amp; Kristiansen, Dual-Quaternion Backstepping Control for a Fully-Actuated Rigid-Body, 5653--5658, in in: {2018 {{Annual American Control Conference}} ({{ACC}})}, edited by {IEEE} (2018)">stianandersen2018</a></sup> {#ab3b05}

The work proposes a Backstepping controller for a fully actuated rigid-body using Dual Quaternions. The controller is proved to be asymptotically stable using Lyapunov.


### Sliding Modes <code>[2/2]</code> {#sliding-modes}


#### <span class="org-todo done DONE">DONE</span> <sup id="69eba384118ecb36a0350ee94a5b7f82"><a href="#dong2017" title="Dong, Hu, Friswell \&amp; Ma, Dual-{{Quaternion}}-{{Based Fault}}-{{Tolerant Control}} for {{Spacecraft Tracking With Finite}}-{{Time Convergence}}, {IEEE Trans. Contr. Syst. Technol.}, v(4), 1231--1242 (2017).">dong2017</a></sup> {#efa649}

A fault-tolerant sliding modes controller using dual quaternions is proposed for a target-pursuer spacecraft tracking. The proposed controller can achieve a few desired properties as tracking error converging to zero within a choosed finite time. The faults can be partial or total actuator power loss, actuator offset and locking.
The controller is used in a simulation showing promising results.


#### <span class="org-todo done DONE">DONE</span> <sup id="00f39b5169f2732fdc4ff7583047a966"><a href="#huang2017" title="Huang, Yan, Zhou \&amp; Yang, Dual-Quaternion Based Distributed Coordination Control of Six-{{DOF}} Spacecraft Formation with Collision Avoidance, {Aerospace Science and Technology}, v(), 443--455 (2017).">huang2017</a></sup> {#6d3872}


### \\(H\_\infty\\)  <code>[1/1]</code> {#h-infty}


#### <span class="org-todo done DONE">DONE</span> <sup id="a666c7a16141742141ff61342199d764"><a href="#figueredo_robust_2013" title="Figueredo, Adorno, Ishihara \&amp; Borges, Robust Kinematic Control of Manipulator Robots Using Dual Quaternion Representation, 1949--1955, in in: {Robotics and {{Automation}} ({{ICRA}}), 2013 {{IEEE International Conference}} On}, edited by {IEEE} (2013)">figueredo_robust_2013</a></sup> {#943110}

Controle robusto do tipo \\(H\_\infty\\)

[figueredo_robust_2013 | Robust kinematic control of manipulator robots using dual quaternion representation]({{< relref "figueredo_robust_2013" >}})


### Resolved-Acceleration Control <code>[1/1]</code> {#resolved-acceleration-control}


#### <span class="org-todo done DONE">DONE</span> <sup id="6e9325dd1e4ceb41e14995834d9a3536"><a href="#chandra2020" title="Chandra, Corrales-Ramon \&amp; Mezouar, Resolved-{{Acceleration Control}} of {{Serial Robotic Manipulators Using Unit Dual Quaternions}}, {IFAC-PapersOnLine}, v(2), 8500--8505 (2020).">chandra2020</a></sup> {#a94c6b}

The authors propose a new controller using [Resolved-Acceleration Control]({{< relref "resolved_acceleration_control" >}}) (looks like a [feedback linearization]({{< relref "feedback_linearization" >}})) for the trajectory tracking of serial robotic manipulators using dual quaternions and based on screw theory.
The controller is compared to a uncoupled controller (which separates translation and orientation) getting similar results, actually performed worse on position but better on orientation.


## Serial Mechanism <code>[2/2]</code> {#serial-mechanism}


### <span class="org-todo done DONE">DONE</span> <sup id="33cbc6f7bc59ab3b6dddeb95d9d74a7c"><a href="#ozgur2016" title="\Ozg\ur \&amp; Mezouar, Kinematic Modeling and Control of a Robot Arm Using Unit Dual Quaternions, {Robotics and Autonomous Systems}, v(), 66--73 (2016).">ozgur2016</a></sup> {#4501f1}

Very interesting article of kinematic modeling and control of robotic arms. It uses a [Screw Theory]({{< relref "screw_theory" >}}) approach to model the kinematics, much like [Successive Screws]({{< relref "successive_screws" >}}), but using only one frame, doesn't need a [convenient frame]({{< relref "convenient_frame" >}}). Also the metodology is mind opening someway because the authors model the rotations from [end-effector]({{< relref "end_link" >}}) to [base]({{< relref "base_link" >}}), and not the opositte, which in my opinion is easier to understand because going from end to base the successive rotations are not carried by the previous rotations.


### <span class="org-todo done DONE">DONE</span> <sup id="79060351f34034626dee2d4aab2eb000"><a href="#amininan2017" title="Amininan, Sheikhha, Baghyari, Hosseini, Najmabadi \&amp; Akbarzadeh, Explicit {{Inverse Kinematic Solution}} for the {{Industrial FUM Articulated Arm}} Using {{Dual Quaternion Approach}}, 602--607, in in: {2017 5th {{RSI International Conference}} on {{Robotics}} and {{Mechatronics}} ({{ICRoM}})}, edited by {IEEE} (2017)">amininan2017</a></sup> {#288f9f}

The paper solves the [inverse kinematics]({{< relref "inverse_kinematics" >}}) of an specific [serial 6dof industrial arm]({{< relref "serial_mechanism" >}}) using dual quaternions. The [direct kinematics]({{< relref "direct_kinematics" >}}) equations are derived using DQ and through manipulating the equations they can solve it for the inverse kinematics problem. Nothing too fancy or new.


## Parallel Mechanism <code>[1/1]</code> {#parallel-mechanism}


### <span class="org-todo done DONE">DONE</span> <sup id="2f4765c82359a6927562149c92812fbf"><a href="#shabani2021" title="Shabani, Porta \&amp; Thomas, A Branch-and-Prune Method to Solve Closure Equations in Dual Quaternions, {Mechanism and Machine Theory}, v(), 104424 (2021).">shabani2021</a></sup> {#b87efa}

The authors uses dual quaternions to formulate closure loop equations as a system of multiaffine equations, they then introduce a new branch-and-prune method tailored to this type of equations to solve the system which can reduce computing time up to 2 orders of magnitude compared to traditional approaches.


## Dynamics <code>[2/2]</code> {#dynamics}


### <span class="org-todo done DONE">DONE</span> <sup id="a9415d881eb3c65938675574eded8747"><a href="#valverde2018" title="Valverde \&amp; Tsiotras, Dual {{Quaternion Framework}} for {{Modeling}} of {{Spacecraft}}-{{Mounted Multibody Robotic Systems}}, {Front. Robot. AI}, v(), 128 (2018).">valverde2018</a></sup> {#59d396}

The work describes an framework to derive the dynamics of a satellite, but it can be used to a general serial mechanism (at least I think), the proposed framework works with revolute, prismatic, cylindrical, spherical and planar joints. The equations are computed using dual quaternions and [Newton-Euler formulation]({{< relref "newton_euler_method" >}}).


### <span class="org-todo done DONE">DONE</span> <sup id="a88a6598a0751d7ebb8eff58fcc3bf61"><a href="#mirandadefarias2019" title="Miranda de Farias, da Cruz Figueredo \&amp; Yoshiyuki Ishihara, Performance {{Study}} on {{dqRNEA}} \textendash{} {{A Novel Dual Quaternion Based Recursive Newton}}-{{Euler Inverse Dynamics Algorithms}}, 94--101, in in: {2019 {{Third IEEE International Conference}} on {{Robotic Computing}} ({{IRC}})}, edited by {IEEE} (2019)">mirandadefarias2019</a></sup> {#2d7915}

The work do a performace study on an Recursive [Newton-Euler]({{< relref "newton_euler_method" >}}) Inverse Dynamics Algorithm using dual quaternions. The algorithm uses Newton-Euler formulation to compute the kinematics and given the desired accelerations and external forces, computes the necessary torques of the motors to drive the system.

They use dual quaternions in the kinematics and kinetics, for the inertia they create an inertia function (so not explicitily a matrix). They use a screw theory approach for the kinematics, not using DH.

The performance of the algorithm using DQ is compared to using HTM, and the result is favorable to DQ, maybe like 33% less cost in terms of number of operations.


## Desvantagens <code>[0/0]</code> {#desvantagens}


## <span class="org-todo done DONE">DONE</span> Adicionar as referências lidas. {#adicionar-as-referências-lidas-dot}


### <span class="org-todo done DONE">DONE</span> Colocar as referencias no General Overview {#colocar-as-referencias-no-general-overview}


### <span class="org-todo done DONE">DONE</span> Colocar no resto do trabalho {#colocar-no-resto-do-trabalho}


## <span class="org-todo done DONE">DONE</span> Coisas a ver no trabalho {#coisas-a-ver-no-trabalho}


### <span class="org-todo done DONE">DONE</span> Ver se no meu trabalho eu faço o uso de q1.q2 = 0 onde q = q1 + eps q2 {#ver-se-no-meu-trabalho-eu-faço-o-uso-de-q1-dot-q2-0-onde-q-q1-plus-eps-q2}


## <span class="org-todo todo TODO">TODO</span> Fazer as correções de Edson {#fazer-as-correções-de-edson}


## <span class="org-todo todo TODO">TODO</span> O que fazer sobre a parte de Geometric Modeling {#o-que-fazer-sobre-a-parte-de-geometric-modeling}

-   [ ] Tirar
-   [ ] Deixar junto
-   [ ] Deixar separado


## <span class="org-todo todo TODO">TODO</span> Após o artigo {#após-o-artigo}


### <span class="org-todo todo TODO">TODO</span> Ler trabalhos de Featherstone citados em <sup id="33cbc6f7bc59ab3b6dddeb95d9d74a7c"><a href="#ozgur2016" title="\Ozg\ur \&amp; Mezouar, Kinematic Modeling and Control of a Robot Arm Using Unit Dual Quaternions, {Robotics and Autonomous Systems}, v(), 66--73 (2016).">ozgur2016</a></sup> {#ler-trabalhos-de-featherstone-citados-em}
