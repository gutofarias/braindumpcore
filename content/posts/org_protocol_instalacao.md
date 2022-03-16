+++
title = "org-protocol instalação"
author = ["João Gutemberg Farias"]
draft = false
+++

source
: <https://www.orgroam.com/manual.html>


## Configuração no Sistema {#configuração-no-sistema}

Segue os passos:

1.  Abre o Editor de Scripts e coloca o seguinte script (alterando o path do [emacsclient]({{< relref "emacsclient" >}}))

    ```applescript
    on open location this_URL
      set EC to "/usr/local/bin/emacsclient --no-wait "
      set filePath to quoted form of this_URL
      do shell script EC & filePath
      tell application "Emacs" to activate
    end open location
    ```

2.  Salva o script com o nome de "org-protocol.app" (o nome não é importante). Tem que ser salvo na pasta "/Applications" e deve ser salvo como app e não como script.

3.  Edita "/Applications/OrgProtocolClient.app/Contents/Info.plist" adicionando antes do ULTIMO tag `</dict>`

    ```plist
    <key>CFBundleURLTypes</key>
    <array>
      <dict>
        <key>CFBundleURLName</key>
        <string>org-protocol handler</string>
        <key>CFBundleURLSchemes</key>
        <array>
          <string>org-protocol</string>
        </array>
      </dict>
    </array>
    ```

4.  Salva o arquivo e executa o app uma vez pra registrar o protocolo.


## Configuração no navegador {#configuração-no-navegador}

Pra usar o um protocolo do [org-protocol]({{< relref "org_protocol" >}}) a partir do navegador é preciso adicionar [bookmarklet]({{< relref "bookmarklet" >}})s.

Eu adicionei os seguintes bookmarklets abaixo. Para acioná-los basta estar na página desejada e clicar no respectivo item nos favoritos.


### [org-protocol-store-link]({{< relref "org_protocol_store_link" >}}) {#org-protocol-store-link--org-protocol-store-link-dot-md}

<a id="code-snippet--Org Store Link"></a>
```javascript
   javascript:location.href ='org-protocol://store-link?url=' + encodeURIComponent(location.href)
+ '&title=' + encodeURIComponent(document.title);
```


### [org-protocol-capture]({{< relref "org_protocol_capture" >}}) {#org-protocol-capture--org-protocol-capture-dot-md}

<a id="code-snippet--Org Capture"></a>
```javascript
javascript:location.href = 'org-protocol://capture?url=' + encodeURIComponent(location.href)
+ '&title=' + encodeURIComponent(document.title);
```

sources
: <https://jingsi.space/post/2017/04/30/org-protocol/>, <http://www.diegoberrocal.com/blog/2015/08/19/org-protocol/>


### Brave prompt de confimação {#brave-prompt-de-confimação}

Tem que fazer algum comando pra que o brave pare de pedir o prompt de confirmação cada vez que tenta-se executar um protocolo.

Tem essa configuração pra Chrome, testei e pelo visto não funcionou. A não ser que funcione após reiniciar.

```sh
defaults write com.google.Chrome ExternalProtocolDialogShowAlwaysOpenCheckbox -bool true
```


## [org-roam-protocol]({{< relref "org_roam_protocol" >}}) {#org-roam-protocol--org-roam-protocol-dot-md}

Não precisei adicionar nenhum [bookmarklet]({{< relref "bookmarklet" >}}) porque o [roam-file protocol]({{< relref "roam_file_protocol" >}}) já funciona com os links que vem no grafo. Já o [roam-ref protocol]({{< relref "roam_ref_protocol" >}}) precisaria adicionar o bookmarklet pra usar. Mas ainda não o fiz.
