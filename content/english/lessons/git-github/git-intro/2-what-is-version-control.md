---
title: "What Is Version Control"
subtitle: "Subtitle is here"
description: "A version control system allows you to track and manage changes to your files. Learn about the benefits of version control for open science and how git and GitHub support version control."
author: "Leah Wasser"
authors:
  - "Max Joseph"
  - "Leah Wasser"
  - "Jenny Palomino"
  - "Martha Morrissey"
categories: ["collaboration-version-control"]
date: 2023-09-04
partner: dss
estimated-time: "2 3 hours"
difficulty: "beginner"
module: "intro-git"
url: /git-intro/about-version-control.html
order: 2
---

{{< toc >}}

# Get Started With Git/GitHub.com

Learn about the benefits of version control for tracking and managing changes
to your files. You will also learn how to implement version control using
**git** and then upload changes to **Github.com**.

{{< noticeowl "learn" >}}

After completing this module, you will be able to:

-   Define **version control**.
-   Explain why **version control** is useful in a scientific workflow.
-   Implement version control using **git**.

## <i class="fa-regular fa-square-check"></i> What You Need

Be sure that you have completed the instructions on [Setting up Git, Bash, and Conda on your computer](/git/setup-git-bash) to install the tools for your operating system (Windows, Mac, Linux).

You will also need a web browser and your **GitHub.com** login (username and password).

{{< /noticeowl >}}

## What is Version Control?

A version control system maintains a record of changes to code and other content. It also allows us to revert changes to a previous point in time.

{{< image src="images/git-github/final-doc-phd-comics.gif" caption="Many of us have appended a date to a file name as a method of version control at some point in our lives. Source: Piled Higher and Deeper by Jorge Cham." alt="alter-text" width="500" position="center" command="fit" option="q100" class="img-fluid" title="image title" >}}

## Types of Version control

There are many forms of version control. Some not as good:

-   Save a document with a new date or name (we've all done it, but it isn't efficient and easy to lose track of the latest file).
-   Google Docs "history" function (not bad for some documents, but limited in scope).

Some better:

-   Version control tools like Git, Mercurial, or Subversion.

## Why Version Control is Important

Version control facilitates two important aspects of many scientific workflows:

1.  The ability to save and review or revert to previous versions.
2.  The ability to collaborate on a single project.

This means that you don't have to worry about a collaborator (or your future self) overwriting something important. It also allows two people working on the same document to efficiently combine ideas and changes.

## How Version Control Systems Works

### Simple Version Control Model

A version control system tracks what has changed in one or more files over
time. Version control systems begin with a base version of a document. Then,
they save the committed changes that you make.

You can think of version control as a tape: if you rewind the tape and
start at the base document, then you can play back each change and end
up with your latest version.

{{< image src="images/git-github/git-play-changes.png" caption="A version control system saves changes to a document, sequentially as you add and commit them to the system. Source: Software Carpentry." alt="This is a image with grey boxes representing a page of text or code. The first box has a bunch of existing lines. Then a green arrow points to the next grey box that has a new line added to the bottom which will be committed to version control. That box has a green arrow next to it pointing to the third box that has yet another set of lines that were added by someone to the file." width="800" position="center" command="fit" option="q100" class="img-fluid" title="image title" >}}

Once you think of changes as separate from the document itself, you can then think about "playing back" different sets of changes onto the base document. You can then retrieve, or revert to, different versions of the document.

Collaboration with version control allows users to make independent changes to the same document.

{{< image src="images/git-github/git-versions.png" caption="Different versions of the same document can be saved within a version control system. Source: Software Carpentry." alt="alter-text" width="600" position="center" command="fit" option="q100" class="img-fluid" title="image title" >}}

If there aren't conflicts between the users' changes (a conflict is an area where both users modified the same part of the same document in different ways), you can review two sets of changes on the same base document. If there are conflicts, they can be resolved by choosing which change you want to keep.

{{< image src="images/git-github/git-merge.png" caption="Two sets of changes to the same base document can be merged together within a version control system if there are no conflicts (areas where both users modified the same part of the same document in different ways). If there are conflicts, they can resolved by choosing which change you want to keep. After conflicts are resolved, all other changes submitted by both users can then be merged together. Source: Software Carpentry." alt="alter-text" height="425" width="500" position="center" command="fit" option="q100" class="img-fluid" title="image title" >}}

A version control system is a tool that keeps track of all of these changes for us.
Each version of a file can be viewed and reverted to at any time. That way if you
add something that you end up not liking or delete something that you need, you can
simply go back to a previous version.

### Git and GitHub - A Distributed Version Control Model

**Git** uses a distributed version control model. This means that there can be
many copies (or forks/branches in **GitHub** world) of the repository. When
working locally, **git** is the program that you will use to keep track of
changes to your repository.

**GitHub.com** is a location on the internet (a cloud web server) that acts as a remote location for your repository. **GitHub** provides a backup of your work that can be retrieved if your local copy is lost (e.g. if your computer falls off a pier). **GitHub** also allows you to share your work and collaborate with others on projects.

{{< image src="images/git-github/git-distributed-version-control-model.png" caption="One advantage of a distributed version control system is that there are many copies of the repository. Thus, if any one server or computer dies, any of the client repositories can be copied and used to restore the data! Source: Pro Git by Scott Chacon and Ben Straub" alt="alter-text" height="425" width="500" position="center" command="fit" option="q100" class="img-fluid" title="image title" >}}

## How Git and GitHub Support Version Control

Due to the functionality that each tool provides, you can use **git** and **GitHub** together in the same workflow to:

-   keep track of changes to your code locally using **git**.
-   synchronizing code between different versions (i.e. either your own versions or others' versions).
-   test changes to code without losing the original.
-   revert back to older version of code, if needed.
-   back-up your files on the cloud (**GitHub.com**).
-   share your files on **GitHub.com** and collaborate with others.

Throughout this module, you will learn about using of **git** and **GitHub**
for both version control and collaboration to support open reproducible science.
