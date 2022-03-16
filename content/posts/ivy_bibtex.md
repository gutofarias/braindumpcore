+++
title = "ivy-bibtex"
author = ["João Gutemberg Farias"]
draft = false
+++

source
: <https://github.com/tmalsburg/helm-bibtex>

O pacote permite procurar pelas suas referências a partir de um .bib especificado, encontrar os pdfs (a partir de uma pasta ou a bibkey "File"), encontrar o arquivo de anotações relativo (tem que ver como integrar com [org-noter]({{< relref "org_noter" >}})), gerar as citações, entre outros.

Irei usar em conjunto com o [Zotero]({{< relref "zotero" >}}). Esse vai gerar os .bib com o campo de "File" que vão alimentar o ivy-bibtex.

Eu uso o storage padrão do zotero, então os pdfs ficam organizados numa estrutura própria do zotero. Mas como tem o campo "File" nos bibkeys, o ivy-bibtex consegue achar! Não sei se é a melhor solução.
