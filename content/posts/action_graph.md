+++
title = "Action Graph"
author = ["João Gutemberg Farias"]
draft = false
+++

Start with the [Tree Graph]({{< relref "tree_graph" >}}) with the [strings]({{< relref "strings_in_a_tree_graph" >}}) included as dashed [edges]({{< relref "graph_edge" >}}). Replace each edge by c_i edges in **parallel**, one for each [Constraints of Motion]({{< relref "constraints_of_motion" >}}) of the relative joint.
The replaced edges carry a [wrench]({{< relref "wrench" >}}) related to the constraint it adds.

If the original edge was a [branch]({{< relref "branches_in_a_tree_graph" >}}), only one parallel edge remains a branch, all the others become strings. If the original edge was a string, all the parallel edges become strings.

External forces and moments should be added as [strings]({{< relref "strings_in_a_tree_graph" >}}) going from the [support link]({{< relref "base_link" >}})  to the link where the force/moment is being applied.

The wrenchs can be constructed by [Wrench of a Joint]({{< relref "wrench_of_a_joint" >}}), but at the action graph they should be only refered by a symbol.
