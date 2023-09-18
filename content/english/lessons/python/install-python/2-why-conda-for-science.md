---
title: "Why Conda is Better for Scientific Environments"
subtitle: "Learn why conda can make installing creating environments easier for scientists."
description: |
  A conda environment is a self contained Python environment that allows you to run different versions of Python (with different installed packages) on your computer. Learn how to conda environments can you help manage Python packages and dependencies.
authors:  
  - "Will Norris"
  - "Leah Wasser"
date: 2023-02-12
partner: "dss"
categories:
  - Python
  - Get-started
  - Environment
  - Conda
nav_title: "Why conda for science?"
image: "/images/python/why-use-conda.png"
module: "install-python"
order: 2
---

{{< toc >}}
{{< noticeowl "learn" >}}

After completing this page, you will be able to:

* Understand how dependency management can play a large role in **Python** programming.
* Explain how to use **conda** environments to manage your third party libraries.

{{< /noticeowl >}}

## Conda Environments in Python

### The Third Party Library Issue

Most projects written in **Python** require a certain set of third party libraries that are not in the **Python** standard library. There is a good chance you have used at least one of these libraries such as **numpy**, **matplotlib**, or **pandas**.

Third party libraries are critical to making **Python** the great tool it is. Developers and scientists all over the world are constantly improving and adding to the functionality **Python** provides by writing new packages. When you require one of these third party libraries in your workflow, they are called dependencies because your workflow depends on them to function.

While having a plethora of open source functionality available to the community is one of **Python**'s greatest strengths, dependency management is a major challenge for many **Python** programmers. This is especially true for **Python** programmers who are not dedicated software engineers!

In **Python**, regardless of what project you are working on, your computer will store third party libraries in the same location. This means that if you depend on GDAL 2.4.2 in an older project and GDAL 3.0.1 in your brand new project, you will need a way to store these dependencies separately. If they aren't stored separately, **Python** will not be able to tell the difference between the two that are both installed in the same location.

{{< image src="images/python/xkcd-python-environment-superfund.jpg" caption="Dependency conflicts can cause significant issues when working with Python. Conda allows you to install multiple environments on your computer and to address dependency issues. Image from XKCD Webcomic. Source: XKCD" alt="An image showing a spaghtee monster like web of things installed on a computer including various versions of python installed different ways. At the bottom it says my laptop has become a superfund site." width="600" position="center" command="fit" option="q100" class="img-fluid" title="image title" >}}

### Python Environments

A **Python** environment is a dedicated directory where specific dependencies can be stored and maintained. Environments have unique names and can be activated when you need them, allowing you to have ultimate control over the libraries that are installed at any given time.

You can create as many environments as you want. Because each one is independent, they will not interact or "mess up" the other. Thus, it is common for programmers to create new environments for each project that they work on.

Often times, information about your environment can assist you in debugging certain errors. Starting with a clean environment for each project can help you control the number of variables to consider when looking for bugs.

Broadly, you have two package managers to choose from when creating a Python environment:

1.  You can create a virtual environment (venv) using **pip** to install packages or
2.  You can create a **conda** environment using **mamba** installing packages for you.

On this page, you will learn about **conda** environments. For science applications
conda environments have several strengths compared to \*\*pip\* environments.

## What is Conda

<a href="https://docs.conda.io/en/latest/" target="_blank">Conda</a> is a package and environment management tool that allows you to install **Python** packages on your computer as well as create and manage multiple **Python** environments, each containing different packages.

While you will predominately use **conda** for the installation and management of **Python** libraries, it is important to note that **conda** can install and manage software of many different languages; this can be important when working with external dependencies that aren't built in **Python**.

## Why Conda

As mentioned previously, when it comes to installing packages you have two options: **pip** and **conda**.

**Pip** stands for Pip Installs Packages and is the default package manager available in **Python**. **Conda**, on the other hand, is an environment manager that aims to do what **pip** does with added functionality.

There are several reasons that make **conda** such a strong contender for managing your **Python** environments over **pip**.

### 1. Conda is Cross Platform

Libraries available on **conda** are stored on the Anaconda Cloud and can easily be installed on any system. **Conda** libraries are stored as binary files, which makes them easy for **conda** to unpack anywhere you have Anaconda, Miniforge or Mambaforge installed.

**Pip** packages, on the other hand, are stored in a more more complex way (as wheels or source distributions). This storage format requires a compiler to unpack. This means that you need to have **Python** installed to install packages with **pip**, which brings up the next point.

### 2. Conda Can Install Specific Versions of **Python**

**Conda** allows you to install and run a specific version of **Python**. Anything installed with **pip** requires a wheel or source distribution for the **Python** compiler to break down.

Unfortunately, this means that **pip** cannot directly install versions of **Python**. It also means that you have to install your preferred **Python** distribution before even starting the process of working with a new virtual environment.

### 3. Environments are Native to Conda

As discussed previously, when using **pip**, you must use a virtual environment
as your environment for managing dependencies. However, **virtualenv** is a
**Python** library itself. With some configuration and other wrappers, virtual
environments can provide a satisfactory development environment. However,
when you use **conda**, environments are available to you without needing
to install an additional tool.

### 4. Conda is Better at Dependency Management

**Pip** makes no attempt to check if all of your dependencies are satisfied at once. Instead, **pip** may allow incompatible dependencies to be installed depending on the order you install packages.

**Conda** instead uses what they call a "satisfiability solver", which checks that all dependencies are met at all times. This comes with a performance hit due to having to comb through every dependency on each install, but will save you headaches down the road.

### 5. Conda Manages External Dependencies

**Pip** is lacking when it comes to managing and tracking external dependencies and accessing all of the available libraries out there.

**GDAL** is a prime example of a package that can be installed easily through **conda**, but is difficult to install any other way. Part of this is due to the fact that **GDAL** is not a native **Python** application, and **conda** has a much easier time dealing with that.

While you may prefer using **conda**, there is no clear consensus whether **pip** or **conda** are better.

While they both install packages, **conda** is very different than **pip**. **Conda** can do much more than **pip** at the cost of increased complexity.

For a simple workflow, the benefits of **conda** may not be worth the extra effort to get up and running. For working with geospatial libraries, **conda** is definitely preferred, given it's ability to resolve
dependency issues associated with **GDAL**.

{{< noticeowl "tip" >}}

Sometimes **Python** libraries are on Github and not on a repository like PyPI. In this case, or in the case that you want to install a specific development version of a package, you can install **Python** libraries from Github using `pip install git+git://github.com/path-to-github-user/repo-name.git`

{{< /noticeowl >}}

## Channels in Conda

Above you learned about the differences between using **pip** vs **conda** to install **Python** packages. However, there are also different channels available in **conda** that you can use to install packages into your **conda** environment.

Below, you will learn about the **conda-forge** channel which is an alternative to the default **conda** channel. This is the channel that you should use as your primary "go to" installation channel, when setting up your **Python** environment for scientific applications.

There are two main **conda** channels that you should consider:
\* **conda:** this is the default repository that is used and maintained for the Anaconda distribution of **Python**. To install libraries from **conda**, you use the syntax `conda install package-name` at the command line.
\* **conda-forge:** This channel is community maintained, and we have found that installing many of the spatial packages using **conda-forge** will minimize conflicts between packages. To install libraries from **conda-forge**, you use the syntax `conda install -c conda-forge package-name` at the command line.

> **Note**
>
> Note: bioconda is another channel that is widely used in science but we are
> not going to discuss that channel in this tutorial.

For consistency, we suggest that always use the **conda-forge** repository
when you install packages in a conda environment. However in some cases, a
package may not be on conda. In these instances you may be forced to use
pip.

<img src="../images/python/conda-channels-geohackweek.jpeg" title="You can think about a channel as a bucket of tools that are all located on the same server / in the same main directory. The three main Python channels are conda default (managed by Anaconda), conda-forge and bioconda. Image Source: https://geohackweek.github.io/datasharing/01-conda-tutorial/." data-fig-alt="Hand drawn image showing the various buckets or channels available in the anaconda cloud." alt="You can think about a channel as a bucket of tools that are all located on the same server / in the same main directory. The three main Python channels are conda default (managed by Anaconda), conda-forge and bioconda. Image Source: https://geohackweek.github.io/datasharing/01-conda-tutorial/." />

### Default Channels

**Conda** doesn't just have a single repository where all uploaded packages live. When a package is uploaded to **conda**, it must be uploaded to a specific channel, which is just a separate URL where packages published to that channel reside.

There is a `default` **conda** channel where the stock **conda** packages live. These packages are maintained by **conda** and are generally very stable. If you do not specify channels in your configuration settings, whenever you run `conda install x`, **conda** will search its `default` channel for that package; if the package isn't on that channel, it will throw an error.

You want to specify one channel (e.g. **conda-forge**) as often as you can to avoid problems that arise with mixing channels. Much like having two different versions of **GDAL** installed in the same place, mixing channels can confuse **conda's** satisfiability solver for managing dependencies.

The resulting errors can make it look like you have a package installed; however, **Python** will fail to find dependencies when you run it.

### Conda-Forge

The **Python** community has responded to this mixing channel issue and created a community managed channel that solves the channel mixing issues associated with default **conda** channels. This community managed channel is called **conda-forge**.

**Conda-forge** has thousands of contributors and functions very similar to PyPi (pip's central package repository). **Conda-forge** mandates that your dependencies all be installed via `conda-forge` or the `default` channels. By requiring packages to be installed via `conda-forge` by default, any package installed via `conda-forge` should not have issues with mixing channels of dependencies.

**Conda-forge** aims to do better than **PyPi** by providing an automated testing suite along with more peer review of code before it is published. These extra rules make **conda-forge** an ideal choice for creating **Python** environments for science.

If you are a scientist, we suggest that you use **conda-forge** to install all
needed packages. Using a consistent conda channel will save time in the long run
as you list of packages and associated dependencies grows.
