#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#### Script to convert jupyter notebook files to .md files for use by mkdocs

import os
import nbformat
from nbconvert import MarkdownExporter

def convertNotebook(notebookPath, modulePath):

  with open(notebookPath) as fh:
    nb = nbformat.reads(fh.read(), nbformat.NO_CONVERT)

  exporter = MarkdownExporter()
  source, meta = exporter.from_notebook_node(nb)

  with open(modulePath, 'w+') as fh:
    fh.writelines(str(source))


def copy_images(notebookPath='notebooks',mkdocs_docs_dir_path='docs'):
    # for os.path find direcotriess in notebooks/ called images/
    # copy images/ folder to the right location in website/docs
    # copy all images to the right folder in website/docs

    for (dirpath, dirnames, filenames) in os.walk(os.path.join(os.pardir, 'notebooks')):
        for dirname in dirnames:
            if not dirname.startswith('.ipynb_checkpoints'):
                if not os.path.exists(os.path.join(os.pardir, 'website', 'docs', dirname)):
                    os.mkdir(os.path.join(os.pardir, 'website', 'docs', dirname))
                nbnames = os.listdir(os.path.join(os.pardir, 'notebooks', dirname))
                for nbname in nbnames:
                    print(nbname)
                    if nbname.endswith('.ipynb'):
                        nbpath = os.path.join(os.pardir, 'notebooks', dirname, nbname)
                        root, ext = os.path.splitext(nbname)
                        extension = '.md'
                        mdname = os.path.join(root + extension)
                        mdpath = os.path.join(os.pardir, 'website', 'docs', dirname, mdname)
                        convertNotebook(nbpath, mdpath)

    pass

import os

f = []
for (dirpath, dirnames, filenames) in os.walk(os.path.join(os.pardir,'notebooks')):
    f.extend(dirnames)
    for dirname in dirnames:
        if not dirname.startswith('.ipynb_checkpoints'):
            if not os.path.exists(os.path.join(os.pardir, 'website', 'docs', dirname)):
                os.mkdir(os.path.join(os.pardir,'website','docs',dirname))
            nbnames = os.listdir(os.path.join(os.pardir,'notebooks',dirname))
            for nbname in nbnames:
                print(nbname)
                if nbname.endswith('.ipynb'):
                    nbpath = os.path.join(os.pardir,'notebooks',dirname,nbname)
                    root, ext = os.path.splitext(nbname)
                    extension = '.md'
                    mdname = os.path.join(root + extension)
                    mdpath = os.path.join(os.pardir,'website','docs',dirname, mdname)
                    convertNotebook(nbpath, mdpath)

#convertNotebook('00.01-Motivation_test.ipynb','00.01-Motivation_test.md')