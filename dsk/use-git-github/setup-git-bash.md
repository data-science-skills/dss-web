---
title: "Setup Bash on Windows, Mac and Linuxs Operating Systems"
subtitle: " Learn how to install bash on Windows, Mac and Linux operating systems. You will need the bash commandline to use Python and conda."
author: "leah wasser"
date: 2023-02-12
categories:
  - Python
  - Get-started
  - Environment
toc: true
img: "featured-photo.jpeg"
---

-   [Setup Bash / Terminal](#setup-bash-terminal)
    -   [Bash Setup](#bash-setup)
    -   [Git Setup](#git-setup)

-   "Leah Wasser"
-   "Jenny Palomino"

# Setup Bash / Terminal

> **Important**
>
> -   Install `Bash` and `Git`.
> -   Open a terminal and test that `Bash`, `Git`, and Conda are ready for use on your computer.

## Bash Setup

## Mac OS X

The default shell in all versions of Mac OS X is `Bash`, so no need to install
anything. You access `Bash` from the Terminal (found in /Applications/Utilities).
You may want to keep Terminal in your dock for this workshop.

## Linux

The default shell is usually `Bash` but if your machine is set up differently
you can run it by opening the Terminal and typing: `bash`. There is no need to
install anything.

## Windows

Download the <a href="https://git-scm.com/download/win" target = "_blank">Git for Windows installer</a>.

Run the installer by double-clicking on the downloaded file and by following the steps below:

1.  Click on "Run".
2.  Click on "Next".
3.  Click on "Next".
4.  Click on "Next".
5.  Click on "Next".
6.  Click on "Next".
7.  **Leave the selection on "Git from the command line and also from 3rd party software"** and click on "Next". NOTE: If you forgot to do this, the programs that you need for the workshop will not work properly. If this happens, rerun the installer and select the appropriate option.
8.  Click on "Next".
9.  **Leave the selection on "Checkout Windows-style, commit Unix-style line endings"** and click on "Next".
10. Select the second option for **Use Windows' default console window** and click on "Next".
11. Click on "Next".
12. Click on "Install".
13. When the install is complete, click on "Finish".

This installation will provide you with both `Git` and `Bash` within the
`Git Bash` program.

## Git Setup

`Git` is a version control system that lets you track who made changes to what and when, and it has options for easily updating a shared or public version of your code on <a href="https://github.com/" target="_blank">GitHub</a>.

You will need a <a href="https://help.github.com/articles/supported-browsers/" target="_blank">supported web browser</a> (current versions of Chrome, Firefox or Safari, or Internet Explorer version 9 or above).

`Git` installation instructions borrowed and modified from <a href="http://software-carpentry.org/" target="_blank">Software Carpentry</a>.

## Mac OS X

<a href="https://www.youtube.com/watch?v=9LQhwETCdwY" target="_blank">Video Tutorial</a>

Install `Git` on Macs by downloading and running the most recent installer for "mavericks" if you are using OS X 10.9 and higher -or- if using an earlier OS X, choose the most recent "snow leopard" installer, from <a href="http://sourceforge.net/projects/git-osx-installer/files/" target="_blank">this list</a>.

After installing `Git`, there will not be anything in your /Applications folder, as `Git` is a command line program.

> **Data Tip**
>
> If you are running Mac OSX El Capitan, you might encounter errors when trying to use `Git`. Make sure you update XCODE. <a href="http://stackoverflow.com/questions/32893412/command-line-tools-not-working-os-x-el-capitan" target="_blank">Read more - a Stack Overflow Issue</a>.

## Git on Linux

If `Git` is not already available on your machine, you can try to install it via your distro's package manager. For Debian/Ubuntu, run `sudo apt-get install git` and for Fedora run `sudo yum install git`.

## Git for Windows

`Git` was installed on your computer as part of your `Bash` install.
