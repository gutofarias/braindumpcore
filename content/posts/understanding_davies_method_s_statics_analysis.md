+++
title = "Understanding Davies Method's statics analysis"
author = ["João Gutemberg Farias"]
draft = false
+++

When performing [Davies Method]({{< relref "davies_method" >}}), we use the [origin of the system]({{< relref "base_link" >}}) as a reference for statics calculations. This means that all the moments are computed relatively to the origin.

If we consider a system in a static condition, no element will be accelerating and the sum of forces and moments in all bodies will amount to zero. Thus we have our equations.

In Davies Method in spite of a traditional sum of forces in a body we perform a [cut in the tree graph]({{< relref "cutting_a_tree_graph" >}}) that generates the equations unambiguously.
