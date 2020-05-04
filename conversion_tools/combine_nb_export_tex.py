# coding: utf-8

# ## Combine jupyter notebooks

# This script is an investigation of combining two jupyter notebooks into one.

# In[1]:


import nbconvert
import nbformat
import os
from nbconvert import LatexExporter
from nbconvert.writers import FilesWriter
from pathlib import Path
from nbformat.v4 import new_notebook, new_markdown_cell

from nb_list_tools import iter_notebook_sub_dirs_path, iter_notebook_paths


# In[2]:


# Combine two notebooks into 1:

# for nb_path in nb_paths:
# print(nb_path)


# In[3]:


# nb_path1 = nb_paths[14]
# print(nb_path1)
# nb_path2 = nb_paths[15]
# print(nb_path2)


# In[4]:


def combine_nbs(nb_path_lst):
    combined_nbnode = new_notebook()
    for nb_path in sorted(nb_path_lst):
        nb = nbformat.read(nb_path, as_version=4)
        combined_nbnode.cells.extend(nb.cells)
        if not combined_nbnode.metadata:
            combined_nbnode.metadata = nb.metadata.copy()
    return combined_nbnode


# In[5]:


def export_tex(nbnode, outfile="export_tex_out", template="classicm"):
    latex_exporter = LatexExporter()
    latex_exporter.template_file = template
    (body, resources) = latex_exporter.from_notebook_node(nbnode)
    writer = FilesWriter()
    writer.write(
        body, resources, notebook_name=outfile
    )  # will end up with .tex extension


# In[6]:


def main():
    nb_paths = iter_notebook_paths("notebooks")
    combined_nb = combine_nbs(nb_paths)
    export_tex(combined_nb, "out20180528", "book")


if __name__ == "__main__":
    main()
