(defun jethro/publish (file)
  (with-current-buffer (find-file-noselect file t)
    ;; (projectile-mode -1)
    ;; (dtrt-indent-mode -1)
    (setq org-hugo-base-dir "~/Sync/Projetos/org/hugo")
    (org-hugo-export-wim-to-md)))
