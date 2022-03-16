+++
title = "Org Roam Bibtex (ORB)"
author = ["João Gutemberg Farias"]
draft = false
+++

source
: <https://github.com/org-roam/org-roam-bibtex>

Pelo que entendi esse pacote integra o [ivy-bibtex]({{< relref "ivy_bibtex" >}}) e [org-ref]({{< relref "org_ref" >}}) com o [org-roam]({{< relref "org_roam" >}}). Nesse caso, as citações produzidas a partir dos links criados com org-ref, aparecem no org-roam como "cite backlinks" separados dos backlinks normais.

Isso permite uma dinâmica especial separando os backlinks do que for [literature notes]({{< relref "literature_notes" >}}) e do que for [permanent notes]({{< relref "permanent_notes" >}}) no método [Zettelkasten]({{< relref "zettelkasten" >}}).

Talvez seja pertinente **citar** as _literature notes_ e **linkar** as _permanent notes_. Porém nada impede que uma nota literária seja linkada diretamente (ou até mesmo linkar uma anotação específica da nota).

O org-roam-bibtex ainda permite, por meio de um _capture template_ que se faça uma integração com o [org-noter]({{< relref "org_noter" >}}). Isso ocorre quando criamos, a partir do org-roam-bibtex, uma nota literária que já contem as informações do pdf que ela referencia. Isso deixa o org-noter já "configurado" e pronto pra ser usado.
