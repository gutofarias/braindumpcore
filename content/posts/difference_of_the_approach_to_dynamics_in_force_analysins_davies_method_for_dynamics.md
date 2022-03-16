+++
title = "Difference of the approach to Dynamics in Force Analysins - Davies Method for Dynamics"
author = ["João Gutemberg Farias"]
draft = false
+++

Check out [Understanding Davies Method's statics analysis]({{< relref "understanding_davies_method_s_statics_analysis" >}}) first.

In dynamics calculations we need to perform the sum of forces and moments acting in each individual body. So for each [link]({{< relref "links_mechanism" >}})/[node]({{< relref "graph_node" >}}) we compute the sum of forces and moments acting in the link.

Also, we need to chose a point in order to calculate the external moments. For simplicity, the point should be the center of mass of the link.

In order to do that, we first build an [Action Graph]({{< relref "action_graph" >}}) and make a "circular cut" in every node to account for all efforts acting on the node/link. Each node will generate one equation.
