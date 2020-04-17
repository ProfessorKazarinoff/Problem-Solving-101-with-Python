# README.md

## To build website:

Run the main script in nb2mkdocs.py

```
$ conda activate book
(book101)$ cd conversion_tools
(book101)$ python nb2mkdocs.py
```

### build and serve mkdocs site

```text
$ conda activate book
(book101)$ cd website
(book101)$ mkdocs build
(book101)$ mkdocs serve
```

### post the website

```text
(book101)$ mkdocs gh-deploy
```

If ```gh-deploy``` throws an error about git histories not merging or matching

```
(book101)$ git push -f origin gh-pages
```

## To build a .pdf copy of the book

### Output the .tex file and combined images dir and resources dir (embedded images like matplotlib plots)

run the main script in nb2tex.py

```text
$ cd conversion_tools
$ conda activate book101
(book101)$  python nb2tex.py
```

### Build the .pdf using TeXworks

Use the separate TeXworks program to open the .tex file outputted by nb2tex.py

Use the XeLaTeX compiler to output a .pdf (XeLaTeX seems to output the TOC, but pdf LaTeX does not. May need more investigation).

May need to run XeLaTeX twice in order to build the Table of Contents.

Still have to manually exclude the Preface and Appendix from Chapter and Section numbering(but keep the Preface and Appendix in the TOC) with

To take out the Chapter 0 Preface label but keep the Preface in the TOC modify:

```text
\hypertarget{preface}{%
\chapter*{Preface}\label{preface}}
\addcontentsline{toc}{chapter}{Preface}
```

Set chapter counter to start at zero, so that Preface is unlabeled chapter 0 and What is Python is labeled Chapter 1.

```text
\setcounter{chapter}{0}
```

Set section numbers within the Preface and the appendix to no be shown, but to still show up in the TOC

```text
        \hypertarget{motivation}{%
\section*{Motivation}\label{motivation}}
\addcontentsline{toc}{section}{Motivation}
```
