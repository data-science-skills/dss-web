# Welcome to the datascienceskills.org repository!

This is a hugo-driven website that power powered by Quarto to build lessons.

## To build locally

<instructions - https://docs.gethugothemes.com/bigspring/installation/>

1. install quarto and hugo and go
2. run `npm install` to install all of the needed dependencies for the site.

````
added 84 packages, and audited 85 packages in 6s

16 packages are looking for funding
  run `npm fund` for details

found 0 vulnerabilities


2. use mamba
   `mamba activate dataskills`

3. To build and preview

```bash
$ cd dsk
$ quarto preview
````

3. update modules

`hugo mod get -u`

2. Lessons that have code that runs should be written as .qmd files.
3. Other lessons that are only text can be .md files.

## Build the site locally:

The site is setup to use quarto to build **.qmd** files. Quarto runs code
in the **.qmd** file and converts it to **.md** files. then Hugo parses the
.md files which are built into the site.

To build a live preview of the site locally, run:

`quarto preview`

This will allow you to work on lessons and it will update the lessons
in realtime.

`quarto render` will build a single static version of the site
as is at the time you run it.

- note , tip , warning , caution , and important {.callout-note}\
  https://quarto.org/docs/authoring/callouts.html
- font awesome - `{{< fa graduation-cap >}}`

## Customization

- environment - defined in \_environment.yml : `QUARTO_PYTHON=/Users/leahawasser/mambaforge/envs/dataskills/bin/python`

## theme and styles

Right now we are overriding the default styles using a pyos.scss file.
In the future it would be nice to be able build an entire sass
suite of files with subfiles. but for now all modification can happen
in that file. The file is then declared as a part of the theme in `_quarto.yml`

template pages

## A few quirks working with hugo / quarto

- quarto does NOT like a blank front-matter fields
- it also doesn't like comments in the front-matter

Both of the above will break a build.

## new lessons

All lessons are located in the `content/english/lessons` directory.

- module: module name - will allow a set of lessons to be grouped
- order: the order of the lesson in a series starting at 1

## Quarto quirks

### Working with shortcodes

If you want to add a shortcode to a page, you need to ensure you "protect"
it with a `==markdown` raw directive. This tells Quarto that it shouldn't try
to render the shortcode in some other way.

Some things that may happen if you forget to do this include - it will
translate quotes to right and left quotes making the shortcode return
an error.

````
```{=markdown}
{{< toc >}}
```
````

## GitHub action build / docker container

The github action that builds the site uses the dss-mamba container as a base.
this container contains hugo, quarto, nodejs and other needed deps

https://github.com/data-science-skills/dss-mamba

## Lesson front matter

```
title: "Install Python Using Conda & Conda-forge - Mambaforge"
subtitle: "Learn how to install Python using conda and the conda-forge channel."
description: |
  Learn how to install Python using conda and the conda-forge channel. Using conda is the best way to minimize issues when setting up Python for scientific use.
authors:
  - "Leah Wasser"
  - "Jenny Palomino"
date: 2023-02-13
date-modified: "2/18/2023"
categories:
  - Python
  - Get-started
image: "/images/python/install-python-mambaforge.png"
# Module allows us to group several lessons together
# Make sure each lesson in a module has the same module name
module: "install-python"

date: 2023-02-12
# If this is a pyopensci lesson then the name would be pyopensci
# TODO: make the partners a data json file so we can just lookup the
# appropriate info for each partner vs using the same front matter on lots of pages
partner:
  name: "Data Science Skills"
  color: "#666"
  fontColor: "#000"
  image: "images/data-science-skills-banner.png"

nav_title: "Setup git / bash"
module_title: "Git/GitHub For Version Control"
module_nav_title: "Git/GitHub For Version Control"
module_description: "A version control system allows you to track and manage changes to your files. Learn how to get started with version control using git and GitHub.com."
module: "intro-git"
url: /install-python-science-conda/
order: 1
```

## Categories

- python-packaging

- collaboration-version-control
  - git lessons
  - code-review 101
- modular-code
  - script to modules
    geospatial

avoid type= in the front matter ...

# Tags

## Quarto issues to resolve

There are some quirks to deal with them using quarto and hugo together.
I think this is because quarto uses pandoc which causes some unique rendering
outputs that quarto doesn't like.

Issues: the callout below renders with a space that causes issues

````
::: {.callout-tip}
If you are a GIS user and on some versions of the MAC operating system, you will also find an existing **Python** distribution on your computer. A quick way to figure out if **Python** already exists on your computer is to open up
terminal or bash and run:

```{bash}
which python
````

:::

````

> ``` bash
> which python
> ```

essentially no matter what i do, it adds a space which makes it hard to render



````

WARN 2023/09/13 16:13:35 Module "examplesite.com" is not compatible with this Hugo version; run "hugo mod graph" for more information.
go: upgraded github.com/gethugothemes/hugo-modules/components/preloader v0.0.0-20230705095442-1f2d5ac8b18d => v0.0.0-20230913031841-c3e6f1eb8b7b
go: upgraded github.com/gethugothemes/hugo-modules/components/cookie-consent v0.0.0-20230705095442-1f2d5ac8b18d => v0.0.0-20230913031841-c3e6f1eb8b7b
go: upgraded github.com/gethugothemes/hugo-modules/components/custom-script v0.0.0-20230705095442-1f2d5ac8b18d => v0.0.0-20230913031841-c3e6f1eb8b7b

```

i'm still getting this error regardless:
```

WARN 2023/09/13 16:14:14 Module "examplesite.com" is not compatible with this Hugo version; run "hugo mod graph" for more information.

````



Notes

* tip

```{=markdown}
{{< noticeowl "tip" >}}

**Use `git add .` with caution**. Be sure to review the results from `git status` carefully before using `git add .`. You do not want to accidentally add files to version control that you do not want to change in your **GitHub** repository!
{{< /noticeowl >}}
````
