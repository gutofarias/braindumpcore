+++
title = "reynolds2020 | Dual Quaternion-Based Powered Descent Guidance with State-Triggered Constraints"
author = ["João Gutemberg Farias"]
draft = false
+++

I did not read the whole thing. It uses dual quaternions in the [powered descent guidance]({{< relref "powered_descent_guidance" >}}) problem. The article uses several restrictions in the control formulation, it uses a [line-of-sight]({{< relref "line_of_sight_restriction" >}}) restriction (a new type they call slant-range-triggered line-of-sight), also a restriction as a window for the allowed values of the control effort (propulsion power). The control problem is solved through a nonconvex optimization problem.


## Info {#info}


## Notes {#notes}


### Resumo {#resumo}

Não cheguei a ler todo. Mas é mais um que usa quatérnios duais na área de aeroespacial e nesse caso no problema de descida motorizada, onde por exemplo a aeronave tem que pousar na lua (caso desse artigo).
Esse artigo adiciona várias restrições como line-of-sight (um novo tipo que eles chamam de slant-range-triggered line-of-sight), restrição no controlador por uma janela aceitável de controle.
O problema de controle foi resolvido por meio de uma otimização não convexa.
