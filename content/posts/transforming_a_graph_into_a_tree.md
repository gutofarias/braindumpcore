+++
title = "Transforming a graph into a tree"
author = ["João Gutemberg Farias"]
draft = false
+++

To generate a [Tree Graph]({{< relref "tree_graph" >}}) from a general [Graph]({{< relref "graph" >}}) we must choose some edges to be [branches]({{< relref "branches_in_a_tree_graph" >}}) and some to be [arcs/strings]({{< relref "strings_in_a_tree_graph" >}}). If a graph is already a tree, all its edges are then branches. Otherwise it will have too many edges and we have to choose some to be arcs. The arcs are "excluded" from the graph and by doing that the remaining graph is a tree.
The strings can be drawed in the tree graph by drawing them dashed.

It is a really simple process to do and can be easily made visually.
