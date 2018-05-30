#from gooey import Gooey
import argparse
import logging
import os
from pathlib import Path
from tempfile import mkdtemp
from typing import Sequence
import nbconvert
import nbformat
from nbformat import NotebookNode
from nbformat.v4 import new_notebook, new_markdown_cell
from nbconvert import LatexExporter, NotebookExporter, HTMLExporter, PDFExporter
from nbconvert.writers import FilesWriter
from nbconvert.utils.pandoc import pandoc
from filter_links import convert_links
import re
import os

from nb_list_tools import iter_notebook_paths

from filter_links import convert_links

log = logging.getLogger(__name__)


class NoHeader(Exception): pass


def pandoc_convert_links(source):
    return pandoc(source, 'markdown', 'latex', extra_args=['--filter', filter_links])

###!!! Need to work on this function and make the chapter names, section names and sub section names ###
def add_sec_label(cell: NotebookNode, nbname) -> Sequence[NotebookNode]:
    """Adds a Latex \\label{} under the chapter heading.
    This takes the first cell of a notebook, and expects it to be a Markdown
    cell starting with a level 1 heading. It inserts a label with the notebook
    name just underneath this heading.
    """
    assert cell.cell_type == 'markdown', cell.cell_type
    lines = cell.source.splitlines()
    if lines[0].startswith('#'):
        header_lines = 1
    elif len(lines) > 1 and lines[1].startswith('==='):
        header_lines = 2
    else:
        raise NoHeader

    header = '\n'.join(lines[:header_lines])
    intro_remainder = '\n'.join(lines[header_lines:]).strip()
    res = [
        new_markdown_cell(header),
        new_latex_cell('\label{sec:%s}' % nbname)
    ]
    res[0].metadata = cell.metadata
    if intro_remainder:
        res.append(new_markdown_cell(intro_remainder))
    return res

def merge_notebooks(filename_lst):
    """
    a function that creates a single notebook node object from a list of notebook file paths
    :param filename_lst: lst, a list of .ipynb file paths
    :return: a single notebookNode object
    """
    merged = None
    for fname in filename_lst:
        with open(fname, 'r', encoding='utf-8') as f:
            nb = nbformat.read(f, as_version=4)
        if merged is None:
            merged = nb
        else:
            # TODO: add an optional marker between joined notebooks
            # like an horizontal rule, for example, or some other arbitrary
            # (user specified) markdown cell)
            merged.cells.extend(nb.cells)
    if not hasattr(merged.metadata, 'name'):
        merged.metadata.name = ''
    merged.metadata.name += "_merged"
    #print(nbformat.writes(merged))
    return merged

def nbnode_to_ipynb(nb_node,filename="notebookout"):
    """
    function to export a .ipynb file given a notebookNode object as input
    :param nb_node: notebookNode object
    :param filename: str, the name of the output .ipynb file. Don't need extension
    :return: nothing returned, but fuction will output a new .ipynb file
    """
    e = nbconvert.NotebookExporter()
    body, resources = e.from_notebook_node(nb_node)
    writer = FilesWriter()
    writer.write(body, resources, notebook_name=filename)

def nbnode_to_pdf(nb_node,filename="pdfout"):
    """
    function to export a .pdf  file given a notebookNode object as input
    :param nb_node: notebookNode object
    :param filename: str, the name of the output .pdf file. Don't need .pdf extension
    :return: nothing returned, but function will output a new .pdf file
    """
    e = nbconvert.PDFExporter()
    body, resources = e.from_notebook_node(nb_node)
    writer = FilesWriter()
    writer.write(body, resources, notebook_name=filename)

def nbnode_to_tex(nb_node,filename="texout"):
    """
    function to export a .tex  file given a notebookNode object as input
    :param nb_node: notebookNode object
    :param filename: str, the name of the output .tex file. Don't need .tex extension
    :return: nothing returned, but function will output a new .pdf file
    """
    e = MyLatexExporter
    body, resources = e.from_notebook_node(nb_node)
    writer = FilesWriter()
    writer.write(body, resources, notebook_name=filename)

class MyLatexExporter(LatexExporter):
    def default_filters(self):
        yield from super().default_filters()
        yield ('resolve_references', convert_links)

class MyLatexPDFExporter(PDFExporter):
    def default_filters(self):
        yield from super().default_filters()
        yield ('resolve_references', convert_links)

def convertNotebooktoLaTeX(notebookPath, outfilePath='latex_out1', template='classicm'):
    REG_nb = re.compile(r'(\d\d)\.(\d\d)-(.*)\.ipynb')
    base_nb_filename = os.path.basename(notebookPath)
    if REG_nb.match(base_nb_filename):
        with open(notebookPath) as fh:
            nbnode = nbformat.read(fh, as_version=4)

        exporter = LatexExporter()
        exporter.template_file = template  # classicm style if not specified
        exporter.file_extension = '.tex'
        body, resources = exporter.from_notebook_node(nbnode)
        writer = FilesWriter()
        writer.write(body, resources, notebook_name=outfilePath)  # will end up with .tex extension

def export(combined_nb: NotebookNode, output_file: Path, pdf=False,
           template_file=None):
    resources = {}
    resources['unique_key'] = 'combined'
    resources['output_files_dir'] = 'combined_files'

    #log.info('Converting to %s', 'pdf' if pdf else 'latex')
    exporter = MyLatexPDFExporter() if pdf else MyLatexExporter()
    if template_file is not None:
        exporter.template_file = str(template_file)
    writer = FilesWriter(build_directory=str(output_file.parent))
    output, resources = exporter.from_notebook_node(combined_nb, resources)
    writer.write(output, resources, notebook_name=output_file.stem)

def main():

    #notebooks_dir = os.path.join(os.path.basename(os.getcwd()),'notebooks')
    nb_path_lst = iter_notebook_paths('notebooks')
    print(len(nb_path_lst))
    for nb in nb_path_lst:
        print(nb)
    nbnode = merge_notebooks(nb_path_lst)
    print(type(nbnode))
    # export notebooknode to .ipynb file
    #nbnode_to_ipynb(nbnode,'combined')
    # export notebooknode to .pdf
    pdf_filepath = os.path.join(os.pardir, 'pdf','pdfout')
    #nbnode_to_pdf(nbnode,pdf_filepath)
    #print(f"combined .pdf available in {pdf_filepath}.pdf")
    #nbnode_to_tex(nbnode,pdf_filepath)
    # try with bookbook export function
    # consider copying over all images from notebooks/subdir/images to /pdf/images all images in one dir
    outfile_Path = Path(pdf_filepath)
    export(nbnode,outfile_Path,pdf=False,template_file=None)

if __name__ == '__main__':
    main()
