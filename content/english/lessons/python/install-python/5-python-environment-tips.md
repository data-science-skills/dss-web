---
title: "Tips and tricks for checking your Python Environment"
subtitle: "Yup"
description: |
  Learn some helpful tricks to troubleshoot issues with your Python conda environment."
author: "Leah Wasser"
date: 2023-02-12
categories:
  - Python
  - Get-started
  - Environment
partner: "dss"
toc: true
nav_title: "Python environment tips"
image: "/images/python/python-environment-tips.png"
module: "install-python"
order: 5
---

-   <a href="#tips-and-tricks" id="toc-tips-and-tricks">Tips and tricks</a>
    -   <a href="#print-your-current-local-environment" id="toc-print-your-current-local-environment">Print your current local environment</a>
    -   <a href="#print-information-about-a-specific-package" id="toc-print-information-about-a-specific-package">Print information about a specific package</a>

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

<details>
<summary>Code</summary>

``` python
import os

# print(os.environ['CONDA_DEFAULT_ENV'])
os.environ.keys
```

</details>

    <bound method Mapping.keys of environ({'COLORTERM': 'truecolor', 'COMMAND_MODE': 'unix2003', 'CONDA_DEFAULT_ENV': 'base', 'CONDA_EXE': '/Users/leahawasser/mambaforge/bin/conda', 'CONDA_PREFIX': '/Users/leahawasser/mambaforge', 'CONDA_PROMPT_MODIFIER': '(base) ', 'CONDA_PYTHON_EXE': '/Users/leahawasser/mambaforge/bin/python', 'CONDA_SHLVL': '1', 'DENO_DOM_PLUGIN': '/Applications/quarto/bin/tools/deno_dom/libplugin.dylib', 'GIT_ASKPASS': '/Applications/Visual Studio Code.app/Contents/Resources/app/extensions/git/dist/askpass.sh', 'HOME': '/Users/leahawasser', 'HOMEBREW_CELLAR': '/opt/homebrew/Cellar', 'HOMEBREW_PREFIX': '/opt/homebrew', 'HOMEBREW_REPOSITORY': '/opt/homebrew', 'INFOPATH': '/opt/homebrew/share/info:', 'LANG': 'en_US.UTF-8', 'LOGNAME': 'leahawasser', 'MANPATH': '/opt/homebrew/share/man::', 'MPLBACKEND': 'module://matplotlib_inline.backend_inline', 'MallocNanoZone': '0', 'ORIGINAL_XDG_CURRENT_DESKTOP': 'undefined', 'PATH': '/Users/leahawasser/.docker/bin:/opt/homebrew/opt/ruby@3.1/bin:/opt/homebrew/opt/ruby/bin:/Users/leahawasser/mambaforge/bin:/Users/leahawasser/mambaforge/condabin:/Users/leahawasser/.local/bin:.:/Applications/quarto/bin:/Library/Frameworks/Python.framework/Versions/3.9/bin:/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/MacGPG2/bin:/Applications/quarto/bin', 'PWD': '/Users/leahawasser/Documents/GitHub/1-lessons/dss-web', 'QUARTO_BIN_PATH': '/Applications/quarto/bin', 'QUARTO_DENO': '/Applications/quarto/bin/tools/deno-aarch64-apple-darwin/deno', 'QUARTO_FILTER_DEPENDENCY_FILE': '/var/folders/r8/3vljpqb55psbgb1ghc2qsn700000gn/T/quarto-session7ec7771e/b88cba77/aad3e5f8', 'QUARTO_PROFILE': '', 'QUARTO_PROJECT_DIR': '/Users/leahawasser/Documents/GitHub/1-lessons/dss-web', 'QUARTO_ROOT': '/', 'QUARTO_SHARE_PATH': '/Applications/quarto/share', 'SHELL': '/bin/zsh', 'SHLVL': '2', 'SSH_AUTH_SOCK': '/private/tmp/com.apple.launchd.rfQv9gEdwH/Listeners', 'STARSHIP_SESSION_KEY': '2110387036684206', 'STARSHIP_SHELL': 'zsh', 'TERM': 'xterm-color', 'TERM_PROGRAM': 'vscode', 'TERM_PROGRAM_VERSION': '1.82.0', 'TMPDIR': '/var/folders/r8/3vljpqb55psbgb1ghc2qsn700000gn/T/', 'USER': 'leahawasser', 'USER_ZDOTDIR': '/Users/leahawasser', 'VSCODE_GIT_ASKPASS_EXTRA_ARGS': '--ms-enable-electron-run-as-node', 'VSCODE_GIT_ASKPASS_MAIN': '/Applications/Visual Studio Code.app/Contents/Resources/app/extensions/git/dist/askpass-main.js', 'VSCODE_GIT_ASKPASS_NODE': '/Applications/Visual Studio Code.app/Contents/Frameworks/Code Helper (Plugin).app/Contents/MacOS/Code Helper (Plugin)', 'VSCODE_GIT_IPC_HANDLE': '/var/folders/r8/3vljpqb55psbgb1ghc2qsn700000gn/T/vscode-git-5745c959d1.sock', 'VSCODE_INJECTION': '1', 'XPC_FLAGS': '0x0', 'XPC_SERVICE_NAME': '0', 'ZDOTDIR': '/Users/leahawasser', '_': '/Applications/quarto/bin/tools/deno-aarch64-apple-darwin/deno', '_CE_CONDA': '', '_CE_M': '', '__CFBundleIdentifier': 'com.microsoft.VSCode', '__CF_USER_TEXT_ENCODING': '0x1F5:0x0:0x0', 'QUARTO_FIG_WIDTH': '8', 'QUARTO_FIG_HEIGHT': '5', 'QUARTO_FIG_DPI': '192', 'QUARTO_FIG_FORMAT': 'png', 'PYDEVD_USE_FRAME_EVAL': 'NO', 'JPY_PARENT_PID': '64318', 'CLICOLOR': '1', 'FORCE_COLOR': '1', 'CLICOLOR_FORCE': '1', 'PAGER': 'cat', 'GIT_PAGER': 'cat'})>

## Print information about a specific package

...when you are developing tools you may want to make sure your package is installed in editable mode...
