# README.md

## To build website:

### Convert notebooks to html that mkdocs can read

run main script in nb2html.py

### Copy over all of the images from the notebooks/subdir to website/subdir

run main script in copy_images_dir.py

### Build the TOC yaml that goes at the end of the mkdocs config file

run main script in yaml_TOC.py

### Combine the TOC.yml file created above with the mkdocs_config file

run the main script in make_mkdocs_yaml.py

### build and serve mkdocs site

```text
$ conda activate book
(book)$ cd website
(book)$ mkdocs build
(book)$ mkdocs serve
```

### post the website

```text
(book)$ mkdocs gh-deploy
```

If ```gh-deploy``` throws an error about git histories not merging or matching

```
git push -f origin gh-pages
```

## To build a .pdf copy of the book

### Output the .tex file and combined images dir and resources dir(embeded images like matplotlib plots)

run the main script in nb2pdf.py

### Build the .pdf using TexWorks

Use the separate TexWorks program to open the .tex file outputed by nb2pdf.py

Use the XeLaTeX compiler to output a .pdf (XeLaTeX seems to output the TOC, but pdf LaTeX does not. May need more investigation)

May need to run XeLaTeX twice in order to build the Table of contents

Still have to manually exclude the Preface and Appendix from Chapter and Section numbering with

```
    \hypertarget{preface}{%
\chapter*{Preface}\label{preface}}
```
