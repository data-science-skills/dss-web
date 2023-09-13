# dsk

lesson website

## Hosting

netlify...

## Setup quarto

This website is created using quarto. To build locally, you
will first need to install it
[install quarto](https://quarto.org/docs/get-started/)

## Environment setup

1. Install conda envt using mamba

`mamba env create -f environment.yml`

2. use mamba
   `mamba activate dataskills`

3. To build and preview

```bash
$ cd dsk
$ quarto preview
```

Quarto callout types

- note , tip , warning , caution , and important {.callout-note}\
  https://quarto.org/docs/authoring/callouts.html
- font awesome - `{{< fa graduation-cap >}}`

## Customization

- environment - definted in \_environment.yml : `QUARTO_PYTHON=/Users/leahawasser/mambaforge/envs/dataskills/bin/python`

## theme and styles

Right now we are overriding the default styles using a pyos.scss file.
In the future it would be nice to be able build an entire sass
suite of files with subfiles. but for now all modification can happen
in that file. THe file is then declared as a part of the theme in `_quarto.yml`

template pages
