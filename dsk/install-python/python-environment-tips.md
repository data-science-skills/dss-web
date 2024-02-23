---
title: "Tips and tricks for checking your Python Environment"
subtitle: "Yup"
description: |
  Learn some helpful tricks to troubleshoot issues with your Python conda environment."
author:
  - "Leah Wasser"
date: 2023-02-12
categories:
  - Python
  - Get-started
  - Environment
toc: true
image: "/images/python/python-environment-tips.png"
module: "install-python"
layout: "lessons"
---

-   [Tips and tricks](#tips-and-tricks)
    -   [Print your current local environment](#print-your-current-local-environment)
    -   [Print information about a specific package](#print-information-about-a-specific-package)

We've all been there... trying to import a package and python can't find it?
Below are a few tricks to figure out what environment you are in!

This can be useful when troubleshooting code that is not running as you
expect!

# Tips and tricks

## Print your current local environment

this is a good trick for when you're working in Python and something seems
wrong with your environment. It could be that you are in a different environment
than you think you are!

Python to the rescue!

The code snippet below will print the conda environment name to help you
troubleshootz.

``` python
import os
#print(os.environ['CONDA_DEFAULT_ENV'])
os.environ.keys
```

    <bound method Mapping.keys of environ({'COLORTERM': 'truecolor', 'COMMAND_MODE': 'unix2003', 'CONDA_DEFAULT_ENV': 'dataskills', 'CONDA_EXE': '/Users/leahawasser/mambaforge/bin/conda', 'CONDA_PREFIX': '/Users/leahawasser/mambaforge/envs/dataskills', 'CONDA_PREFIX_1': '/Users/leahawasser/mambaforge', 'CONDA_PROMPT_MODIFIER': '(dataskills) ', 'CONDA_PYTHON_EXE': '/Users/leahawasser/mambaforge/bin/python', 'CONDA_SHLVL': '2', 'DENO_DOM_PLUGIN': '/Applications/quarto/bin/tools/deno_dom/libplugin.dylib', 'DENO_NO_UPDATE_CHECK': '1', 'GIT_ASKPASS': '/Applications/Visual Studio Code.app/Contents/Resources/app/extensions/git/dist/askpass.sh', 'GPG_TTY': '/dev/ttys042', 'HOME': '/Users/leahawasser', 'HOMEBREW_CELLAR': '/opt/homebrew/Cellar', 'HOMEBREW_PREFIX': '/opt/homebrew', 'HOMEBREW_REPOSITORY': '/opt/homebrew', 'INFOPATH': '/opt/homebrew/share/info:', 'LANG': 'en_US.UTF-8', 'LOGNAME': 'leahawasser', 'MANPATH': '/opt/homebrew/share/man::', 'MPLBACKEND': 'module://matplotlib_inline.backend_inline', 'MallocNanoZone': '0', 'ORIGINAL_XDG_CURRENT_DESKTOP': 'undefined', 'PATH': '/Users/leahawasser/.docker/bin:/opt/homebrew/opt/ruby@3.1/bin:/opt/homebrew/opt/ruby/bin:/Users/leahawasser/mambaforge/envs/dataskills/bin:/Users/leahawasser/mambaforge/condabin:/Users/leahawasser/.local/bin:.:/Applications/quarto/bin:/Library/Frameworks/Python.framework/Versions/3.9/bin:/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/bin:/System/Cryptexes/App/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/local/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/appleinternal/bin:/usr/local/MacGPG2/bin:/Applications/quarto/bin', 'PWD': '/Users/leahawasser/Documents/GitHub/1-lessons/dss-web', 'QUARTO_BIN_PATH': '/Applications/quarto/bin', 'QUARTO_DENO': '/Applications/quarto/bin/tools/deno-aarch64-apple-darwin/deno', 'QUARTO_FILTER_DEPENDENCY_FILE': '/var/folders/r8/3vljpqb55psbgb1ghc2qsn700000gn/T/quarto-sessionb99ab89f/082bf23a/cbe140f8', 'QUARTO_PROFILE': '', 'QUARTO_PROJECT_DIR': '/Users/leahawasser/Documents/GitHub/1-lessons/dss-web', 'QUARTO_ROOT': '/', 'QUARTO_SHARE_PATH': '/Applications/quarto/share', 'SHELL': '/bin/zsh', 'SHLVL': '2', 'SSH_AUTH_SOCK': '/private/tmp/com.apple.launchd.vWr5CKtICT/Listeners', 'STARSHIP_SESSION_KEY': '2858464106444143', 'STARSHIP_SHELL': 'zsh', 'TERM': 'xterm-color', 'TERM_PROGRAM': 'vscode', 'TERM_PROGRAM_VERSION': '1.86.2', 'TMPDIR': '/var/folders/r8/3vljpqb55psbgb1ghc2qsn700000gn/T/', 'USER': 'leahawasser', 'USER_ZDOTDIR': '/Users/leahawasser', 'VSCODE_GIT_ASKPASS_EXTRA_ARGS': '', 'VSCODE_GIT_ASKPASS_MAIN': '/Applications/Visual Studio Code.app/Contents/Resources/app/extensions/git/dist/askpass-main.js', 'VSCODE_GIT_ASKPASS_NODE': '/Applications/Visual Studio Code.app/Contents/Frameworks/Code Helper (Plugin).app/Contents/MacOS/Code Helper (Plugin)', 'VSCODE_GIT_IPC_HANDLE': '/var/folders/r8/3vljpqb55psbgb1ghc2qsn700000gn/T/vscode-git-69ac8b1d9e.sock', 'VSCODE_INJECTION': '1', 'XPC_FLAGS': '0x0', 'XPC_SERVICE_NAME': '0', 'ZDOTDIR': '/Users/leahawasser', '_': '/Applications/quarto/bin/tools/deno-aarch64-apple-darwin/deno', '_CE_CONDA': '', '_CE_M': '', '__CFBundleIdentifier': 'com.microsoft.VSCode', '__CF_USER_TEXT_ENCODING': '0x1F5:0x0:0x0', 'QUARTO_FIG_WIDTH': '8', 'QUARTO_FIG_HEIGHT': '5', 'QUARTO_FIG_DPI': '192', 'QUARTO_FIG_FORMAT': 'png', 'PYDEVD_USE_FRAME_EVAL': 'NO', 'JPY_PARENT_PID': '54760', 'CLICOLOR': '1', 'FORCE_COLOR': '1', 'CLICOLOR_FORCE': '1', 'PAGER': 'cat', 'GIT_PAGER': 'cat'})>

## Print information about a specific package

...when you are developing tools you may want to make sure your package is installed in editable mode...
