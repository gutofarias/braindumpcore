+++
title = "Cut-Set Matrix"
author = ["João Gutemberg Farias"]
draft = false
+++

The cut-set forms a matrix where each column relates to an [edge]({{< relref "graph_edge" >}}) of the [Action Graph]({{< relref "action_graph" >}}), so there are as many columns as edges.

For each row we [cut]({{< relref "cutting_a_tree_graph" >}}) one [branch]({{< relref "branches_in_a_tree_graph" >}}) and assess the [positiveness]({{< relref "positiveness_of_a_tree_graph_cut" >}}) of the cutted elements. Each column in the row is either +1 if the respective element was cutted positively, -1 if cutted negativelly and 0 if not cutted.

There is one row for each branch in the [Coupling Graph]({{< relref "coupling_graph" >}}).
