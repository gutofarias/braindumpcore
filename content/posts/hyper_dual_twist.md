+++
title = "Hyper-Dual Twist"
author = ["João Gutemberg Farias"]
draft = false
+++

It is an enlarged [twist]({{< relref "twist" >}}) that carries the information of both velocity and acceleration using [Hyper-Dual Vectors]({{< relref "hyper_dual_vectors" >}}). Or a movement and its derivative. It uses the [Automatic Differentiation]({{< relref "automatic_differentiation" >}}) property of [Dual Numbers]({{< relref "dual_numbers" >}})/[Hyper-Dual Numbers]({{< relref "hyper_dual_numbers" >}}).

If we have an velocity twist:
\\[ \hat{\nu} = \vec{\omega} + \epsilon \\, \vec{v} = (\omega + \epsilon \\, v) \hat{s} = |\hat\nu| \\, \hat{s} \\]

The hyper-dual velocity twist will be:

k\\[ \check{\nu} = [\hat{\omega} + \epsilon \\, \hat{v} + \check{\epsilon} ( \dot{\hat{\omega}} + \epsilon \\, \dot{\hat{v}})] = [\omega + \epsilon \\, v + \check{\epsilon}(\dot{\omega} + \epsilon \\, \dot{s})] ( \hat{s} + \check{\epsilon} \\, \dot{\hat{s}} ) \\]

\\[ \check{\nu} = (|\nu| + \check{\epsilon} \\, |\dot{\nu}|) ( \hat{s} + \check{\epsilon} \\, \dot{\hat{s}} ) = \hat{\nu} + \check{\epsilon} \\, \dot{\hat{\nu}} = |\check{\nu}| \\, \check{s}\\]
