#! /usr/bin/env nix-shell
#! nix-shell -i python3 -p python3 ninja

import glob
from pathlib import Path

mypath = '/Users/guto/Sync/Projetos/org/braindumpcore/'
content_path = "\\\"" + mypath + "\\\""
glob1 = mypath + 'org/*.org'
glob2 = mypath + 'org/**/*.org'

# files = glob.glob(glob1,recursive=True)
files = glob.glob(glob2,recursive=True)


with open('build.ninja', 'w') as ninja_file:
    ninja_file.write("""
rule org2md
  command = emacs --batch -l ~/.emacs -l """ + mypath + """publish.el --eval \"(jethro/publish \\"$in\\" """ + content_path + """)\"
  description = org2md $in
""")
    
    for f in files:
        path = Path(f)
        print(f)
        output_file = f"content/posts/{path.with_suffix('.md').name}"
        ninja_file.write(f"""
build {output_file}: org2md {path}
""")

import subprocess
subprocess.call(["ninja"])
