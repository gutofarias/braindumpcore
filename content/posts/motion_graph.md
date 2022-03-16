+++
title = "Motion Graph"
author = ["João Gutemberg Farias"]
draft = false
+++

Start with the [Tree Graph]({{< relref "tree_graph" >}}) with the [strings]({{< relref "strings_in_a_tree_graph" >}}) included as dashed [edges]({{< relref "graph_edge" >}}). Replace each edge by f_i edges in series (you can create virtual nodes just to acomodate the edges in series), one for each [degree of freedom]({{< relref "degrees_of_freedom" >}}) that the joint i allows. The replaced edges carry a [twist]({{< relref "twist" >}}) also related to the movement it allows.

The twits can be constructed by [Twist of a Joint]({{< relref "twist_of_a_joint" >}}), but at the motion graph they should be only refered by a symbol.
