#!/usr/bin/env python
# nb2mkdocs.py

"""
nb2mkdocs.py is a Python script used to convert a directory and subdirectories of Jupyter notebooks
and convert these notebooks into an mkdocs static site. The script runs three other main scripts to build the .md pages
and table of contents so that mkdocs can build the website.

Run from the Anaconda Prompt of the command line:

```
$ conda activate book
(book)$ cd conversion_tools
(book)$ python nb2mkdocs.py
```

The resulting .md files and mkdoc.yml file are saved to the website directory and website/docs directory.

"""

import nb2html
import copy_images_dir
import yaml_TOC
import make_mkdocs_yaml


def main():
    # convert .ipynb notebook files to .md markdown files
    nb2html.main()

    # copy any images from /images in notebook dir to website dir
    copy_images_dir.main()

    # build TOC yaml file from the directory structure and file names/markdown cell headings of the notebooks
    yaml_TOC.main()

    # combine the yaml_TOC file with the mkdocs_config yaml file to create the yaml file that mkdocs uses to build the site
    make_mkdocs_yaml.main()


if __name__ == "__main__":
    main()
