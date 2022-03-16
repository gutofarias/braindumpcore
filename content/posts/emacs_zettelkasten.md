+++
title = "Emacs Zettelkasten"
author = ["João Gutemberg Farias"]
draft = false
+++

Minha configuração no Emacs pra usar o método [Zettelkasten]({{< relref "zettelkasten" >}}).


## Transição para Org com Zettelkasten {#transição-para-org-com-zettelkasten}


### <span class="org-todo todo TODO">TODO</span> Pacotes para instalar e configurar {#pacotes-para-instalar-e-configurar}

1.  [X] [org-roam]({{< relref "org_roam" >}})
2.  [X] [org-noter]({{< relref "org_noter" >}})
3.  [X] [org-pdftools]({{< relref "org_pdftools" >}})
4.  [X] [org-noter-pdftools]({{< relref "org_noter_pdftools" >}})
5.  [X] [Zotero]({{< relref "zotero" >}}) + [Better Bibtex Extension (Zotero)]({{< relref "better_bibtex_extension_zotero" >}})
6.  [X] [ivy-bibtex]({{< relref "ivy_bibtex" >}})
7.  [X] [org-ref]({{< relref "org_ref" >}})
8.  [X] [Org Roam Bibtex (ORB)]({{< relref "org_roam_bibtex_orb" >}})
9.  [X] [org-roam-dailies]({{< relref "org_roam_dailies" >}})
10. [X] [Deft]({{< relref "deft" >}})
11. [X] [org-protocol]({{< relref "org_protocol" >}})
12. [X] [org-protocol instalação]({{< relref "org_protocol_instalacao" >}})
13. [X] [org-roam-protocol]({{< relref "org_roam_protocol" >}})
14. [X] [org-roam-server]({{< relref "org_roam_server" >}})
15. [ ] [org-protocol-capture-html]({{< relref "org_protocol_capture_html" >}})
16. [ ] [org-download]({{< relref "org_download" >}})
17. [ ] [org-cliplink]({{< relref "org_cliplink" >}})


### Material de estudo {#material-de-estudo}


#### EmacsConf 2020 - 17 - Org-mode and Org-Roam for Scholars and Researchers - Noorah Alhasan {#emacsconf-2020-17-org-mode-and-org-roam-for-scholars-and-researchers-noorah-alhasan}

<https://youtu.be/bTbiC6SamT4>


#### An Orgmode Note Workflow {#an-orgmode-note-workflow}

<https://rgoswami.me/posts/org-note-workflow/>


#### Blog Jethro <code>[6/6]</code> {#blog-jethro}

-   [X] <https://blog.jethro.dev/posts/org_mode_workflow_preview/>
-   [X] <https://blog.jethro.dev/posts/automatic_publishing/>
-   [X] <https://blog.jethro.dev/posts/introducing_org_roam/>
-   [X] <https://blog.jethro.dev/posts/how_to_take_smart_notes_org/>
-   [X] <https://blog.jethro.dev/posts/self_tracking_in_plain_text/>
-   [X] <https://blog.jethro.dev/posts/taking_srs_seriously/>


#### Recomendado no manual do org-roam {#recomendado-no-manual-do-org-roam}

-   [ ] <https://www.lesswrong.com/posts/NfdHG6oHBJ8Qxc26s/the-zettelkasten-method-1>
-   [ ] <https://www.reddit.com/r/RoamResearch/comments/eho7de/building_a_second_brain_in_roamand_why_you_might/>


#### <span class="org-todo done DONE">DONE</span> Configurar meu template do orb {#configurar-meu-template-do-orb}


#### <span class="org-todo done DONE">DONE</span> Ver como fica a questão do path das anotações {#ver-como-fica-a-questão-do-path-das-anotações}

No caso a anotação <sup id="ec7598990a7afe9039c646136a235687"><a href="#filipe_adaptive_2015" title="Filipe \&amp; Tsiotras, Adaptive {{Position}} and {{Attitude}}-{{Tracking Controller}} for {{Satellite Proximity Operations Using Dual Quaternions}}, {Journal of Guidance, Control, and Dynamics}, v(4), 566--577 (2015).">filipe_adaptive_2015</a></sup> está dentro da pasta do _slip-box_ mas era pra estar na pasta _refs_.


#### <span class="org-todo done DONE">DONE</span> Ver se coloca ou não o cite-key no título {#ver-se-coloca-ou-não-o-cite-key-no-título}

Coloquei


#### <span class="org-todo done DONE">DONE</span> Definir quais funções fazer o quê e quais usar. {#definir-quais-funções-fazer-o-quê-e-quais-usar-dot}

<!--list-separator-->

-  orb-insert

    Insere referência criando uma nota literária se preciso. É útil pra inserir referências e ao mesmo tempo criar as notas literárias. Configurei pra inserir as referências como citação do org-ref. Customizável em orb-insert-link-description. Outra opção seria usar esse comando pra fazer link do org-roam das notas literárias enquanto que usaria o org-ref-insert-link pra fazer citações.

<!--list-separator-->

-  org-ref-insert-link

    Insere referência sem criar uma nota literária. O padrão do org-ref é um link dado por `cite:citekey`.

<!--list-separator-->

-  orb-insert-non-ref

    Seria a mesma coisa do org-roam-insert porém exclui as notas literárias. Termina ficando mais útil do que o org-roam-insert porque separa as notas permanentes das notas literárias.

<!--list-separator-->

-  org-roam-insert

    Insere um link do org-roam pra uma nota dentro da pasta do zettelkasten. Pode ser qualquer nota. Acho que orb-insert-non-ref terminará sendo mais útil a não ser que se queira inserir um link do org-roam de uma nota literária (sem ser um link de citação).

<!--list-separator-->

-  ivy-bibtex

    Leva para o pdf a partir de uma entrada de citação. Mostra todos as suas citações e quando você seleciona ele leva pra o respectivo pdf.


#### <span class="org-todo done DONE">DONE</span> Ver se faz sentido as coisas de refs ficarem dentro da pasta vigiada pelo org-roam {#ver-se-faz-sentido-as-coisas-de-refs-ficarem-dentro-da-pasta-vigiada-pelo-org-roam}

Faz sim


#### <span class="org-todo done DONE">DONE</span> Configurar org-roam-dailies {#configurar-org-roam-dailies}


#### <span class="org-todo done DONE">DONE</span> Configurar meu template do org-roam {#configurar-meu-template-do-org-roam}


#### <span class="org-todo done DONE">DONE</span> Consertar o título das notas já criadas. Cuidar para que não seja quebrado nenhum backlink {#consertar-o-título-das-notas-já-criadas-dot-cuidar-para-que-não-seja-quebrado-nenhum-backlink}


#### <span class="org-todo done DONE">DONE</span> Ver as funções orb-persp-project e orb-switch-persp {#ver-as-funções-orb-persp-project-e-orb-switch-persp}

Pelo que entendi tem que usar o projectile tbm pra isso funcionar


#### <span class="org-todo done DONE">DONE</span> Configurar meus keybindings {#configurar-meus-keybindings}

(("C-c n i" . orb-insert-non-ref))
(("C-c n I" . org-roam-insert-immediate))
(("C-c n c" . orb-insert))
(("C-c n C" . org-ref-insert-link))
(("C-c n n" . org-noter))
(("C-c n b" . ivy-bibtex))


#### <span class="org-todo done DONE">DONE</span> Configurar faces {#configurar-faces}

<!--list-separator-->

- <span class="org-todo done DONE">DONE</span>  Nano Face Critical

    [testedjoifjsdfioj](hfuidshfu)

    ```emacs-lisp
    (set-face-attribute 'nano-face-critical nil :foreground "#ff757f" :weight 'bold :background 'unspecified)
    ```

<!--list-separator-->

- <span class="org-todo done DONE">DONE</span>  Org Roam Tags

    ```emacs-lisp
    ;; mudei pra isso pq usando o set-face-attribute tava cagando o carregamento de tudo que vinha depois
    ;; Apesar disso, nao vi diferença nessa face. Porém deixei aqui a forma de colocar pelo custom no lugar do set-face-attribute
    (custom-theme-set-faces
     'user
     '(org-roam-tag ((t (:weight bold)))))
    ```
