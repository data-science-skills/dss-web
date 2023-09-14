---
title: "Install Python Using Conda & Conda-forge - Mambaforge"
subtitle: "Learn how to install Python using conda and the conda-forge channel."
description: |
  Learn how to install Python using conda and the conda-forge channel. Using conda is the best way to minimize issues when setting up Python for scientific use.
authors: 
  - "Leah Wasser"
  - "Jenny Palomino"
date: 2023-02-13
date-modified: "2/18/2023"
partner: "dss"
categories:
  - Python
  - Get-started
nav_title: "Install python with conda"
image: "/images/python/install-python-mambaforge.png"
module: "install-python"
url: /install-python-science-conda/
order: 1
---

{{< toc >}}

> **<i class="fa-solid fa-graduation-cap"></i> Learning Objectives**
>
> At the end of this activity, you will be able to:
>
> -   Install the lightweight Mambaforge **Python** distribution which uses the conda-forge channel as a default.
>
> <i class="fa fa-check-square-o fa-2" aria-hidden="true"></i> **What You Need**
>
> Before you start this lesson, be sure that you have a computer with internet access.

# How to Install a Lightweight Python Distribution Using Conda

There are numerous ways to install **Python** on your computer.
Here, you will learn how to install **Python** using `conda` and the `conda-forge` channel.

If you are a scientist, installing **Python** using conda is especially preferred as it can result in fewer environment conflicts. This is especially true if you are working with
spatial data.

Installing conda also will allow you to [create unique, curated **Python** conda environments for your projects which is a recommended way of working in Python in general.](create-conda-environment.qmd)

## What to install - mambaforge **Python** distribution

While you can install any distribution that you wish, we suggest that you
install the mambaforge distribution. Mambaforge is a light weight **Python**
distribution that installs both **Python** and a subset of the core packages. It
uses the conda-forge conda channel. This channel is ideal for installing
scientific tools and will result in cleaner, easier to use environments with
fewer conflicts.

> **The many other ways to install Python**
>
> You can also install Python by:
>
> -   Using ***Homebrew***
> -   Installing the entire **Anaconda distribution**: This is a large distribution maintained by Anaconda, Inc. It is not recommended for your initial setup as
>     1.  It has many additional packages that you might not need.
>     2.  Because it installs using the default conda channel it also could result in dependency conflicts if you have other scientific packages that you may want to install using the conda-forge channel.
> -   Using **Miniconda**: The miniconda distribution, also provided by Anaconda, Inc is a smaller distribution than Anaconda. While it hs fewer packages and is smaller in size than the Anaconda, this distribution still installs packages using the conda **defaults** channel. This means that you may still encounter environmentl conflicts if you use it. Thus we still recommend that you install mambaforge.

> **Tip**
>
> If you are a GIS user and on some versions of the MAC operating system, you will also find an existing **Python** distribution on your computer. A quick way to figure out if **Python** already exists on your computer is to open up
> terminal or bash and run:
>
>     which python

In this lesson, you will learn how to install the mambaforge **Python**
distribution on your computer.

## Why Install Mambaforge instead of Miniconda or Anaconda

You also learned that the conda package manager allows you to install `Python` packages on your computer as well as create and manage multiple `Python` environments, each containing different packages.

There are 4 different distributions that you may wish to select from. To keep
things simple, we suggest that you install mambaforge distribution. This
distribution is preferred because:

-   mamba is developed in C++ and will build your environments much faster than conda
-   the default conda channel is conda-forge which is the preferred channel for science
-   it's much smaller than the anaconda distribution

Below is a quick comparison of all 4 distributions.

| Tool                      | Mambaforge                 | Miniforge          | <a href="https://docs.anaconda.com/anaconda/" target = "_blank">Anaconda</a>     | <a href="https://conda.io/projects/conda/en/latest/user-guide/install/index.html" target = "_blank">Miniconda</a> |
|:-------------|:-------------|:-------------|:-------------|:---------------|
| **Size**                  | \~62mb                     | \~42MB             | Large \~2GB                                                                      | Small \~43MB                                                                                                      |
| **What's installed**      | Conda, Core Python + Mamba | Conda, Core Python | Installs Anaconda Navigator, Spyder, and many other tools that may not be needed | Conda, Core Python                                                                                                |
| **Default conda channel** | conda-forge                | conda-forge        | conda default                                                                    | conda default                                                                                                     |
| **Default tool manager ** | mamba                      | conda              | conda                                                                            | conda                                                                                                             |

## Install Mambaforge from the conda-forge channel

> **For Anaconda Users**
>
> If you want to use mambaforge, we strongly suggest that you uninstall Anaconda.
> If you have environments that you are woried about losing, then you can install
> mambaforge following the instructions listed below to overwrite the default
> conda channels.

### Installation instructions by operating system

## Mac

> **For homebrew Users**
>
> If you have homebrew installed, then the easiest way to install mambaforge is
> to use:
>
> `brew install mambaforge`
>
> [Find directions for installing homebrew here.](https://brew.sh/)

If you don't have homebrew, you can download a mamba installer and use bash
to install it.

1.  Download the installer: <a href="https://github.com/conda-forge/miniforge#mambaforge" target="_blank">Mambaforge installer for Mac</a>. Note that if you have a newer
    mac with a m1 or m2 chip, then you will want to install the Apple Silicon
    version:

`OS X   arm64 (Apple Silicon)   Mambaforge-MacOSX-arm64`

If you have an older mac use

`OS X   x86_64  Mambaforge-MacOSX-x86_64`

1.  In your Terminal window, cd to the location of the download file. Run:

`bash Mambaforge3-latest-MacOSX-modify-filename-here.sh`.

1.  Follow the prompts on the installer screens.

2.  If you are unsure about any setting, accept the defaults. You can change them later.

3.  To make sure that the changes take effect, close and then re-open your Terminal window.

Once you are done you can test that the install worked.

### Test your install on Mac

1.  Search for and open the Terminal program (found in /Applications/Utilities). In this `Terminal` window, type `bash` and hit enter.
    If you do not get a message back, then `Bash` is available for use.

2.  Next, type `git` and hit enter.
    If you see a list of commands that you can execute, then `Git` has been installed correctly.

3.  Next, type `conda` and hit enter.
    Again, if you see a list of commands that you can execute, then Mambaforge `Python` has been installed correctly.

4.  Close the `Terminal` by typing `exit`.

## Linux

1.  Download the installer: <a href="https://github.com/conda-forge/miniforge#mambaforge" target="_blank">Mambaforge installer for Linux</a>.

2.  In your Terminal window, run making sure to modify the file name to match the file that you downloaded:

`bash Mambaforge3-latest-Linux-modify-file-name-here.sh`.

1.  Follow the prompts on the installer screens.

2.  If you are unsure about any setting, accept the defaults. You can change them later.

3.  To make sure that the changes take effect, close and then re-open your Terminal window.

Once you are done, you can test that your install worked.

### Test your install on Linux

1.  Search for and open the Terminal program. In this `Terminal` window, type `bash` and hit enter.
    If you do not get a message back, then `Bash` is available for use.

2.  Next, type `git` and hit enter.
    If you see a list of commands that you can execute, then `Git` has been installed correctly.

3.  Next, type `conda` and hit enter.
    Again, if you see a list of commands that you can execute, then Mambaforge `Python` has been installed correctly.

4.  Close the `Terminal` by typing `exit`.

## Windows

> **Tip**
>
> **Windows Users:** if you already have Anaconda installed, then you will be
> asked to confirm that you want to make the Mambaforge installation the default
> conda on your computer when you follow step 6 of the Mambaforge installation.

Download the <a href="https://github.com/conda-forge/miniforge#mambaforge" target="_blank">Mambaforge installer for Windows</a>.

Run the installer by double-clicking on the downloaded file and follow the steps
below.

1.  Click "Run".
2.  Click on "Next".
3.  Click on "I agree".
4.  Leave the selection on "Just me" and click on "Next".
5.  Click on "Next".
6.  **Select the first option for "Add Anaconda to my PATH environment variable"** and also **leave the selection on "Register Anaconda as my default Python 3.x".** Click on "Install".
    -   Note that even though the installation is for Mambaforge, the installer uses the word Anaconda in these options.
    -   You will also see a message in red text that selecting "Add Anaconda to my PATH environment variable" is not recommended; continue with this selection to make using conda easier in Git Bash. If you have questions or concerns, please contact your instructor.
7.  When the install is complete, Click on "Next".
8.  Click on "Finish".

Once you are done, you can test that the installation worked.

### Test your install on Windows

1.  Search for and open the `Git Bash` program. In this `Terminal` window, type `bash` and hit enter.
    If you do not get a message back, then `Bash` is available for use.

2.  Next, type `git` and hit enter.
    If you see a list of commands that you can execute, then `Git` has been installed correctly.

3.  Next, type `conda` and hit enter.
    Again, if you see a list of commands that you can execute, then Mambaforge `Python` has been installed correctly.

4.  Close the `Terminal` by typing `exit`.

<!-- Note that there are five types of callouts, including:
`note`, `warning`, `important`, `tip`, and `caution`. -->
