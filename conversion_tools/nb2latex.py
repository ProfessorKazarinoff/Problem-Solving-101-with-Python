#from gooey import Gooey
import argparse
import logging
import os
from pathlib import Path
from tempfile import mkdtemp
from typing import Sequence

import nbformat
from nbformat import NotebookNode
from nbformat.v4 import new_notebook, new_markdown_cell
from nbconvert import LatexExporter, NotebookExporter  # , #HTMLExporter #PDFExporter,
from nbconvert.writers import FilesWriter
from nbconvert.utils.pandoc import pandoc
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


def new_latex_cell(source=''):
    return NotebookNode(
        cell_type='raw',
        metadata=NotebookNode(raw_mimetype='text/latex'),
        source=source,
    )


def combine_notebooks(nb_path_lst):
    """
    function combines a list of notebooks from a list of notebook paths and returns a nbnode of all combined
    :param nb_path_lst: lst, list of notebook file paths
    :return:
    """
    combined_nb = new_notebook()
    for nb_path in sorted(nb_path_lst):
        with open(nb_path) as fh:
            nb = nbformat.read(fh, as_version=4)
        combined_nb.cells.extend(nb.cells)
        if not combined_nb.metadata:
            combined_nb.metadata = nb.metadata.copy()

    return combined_nb


# def export(combined_nb: NotebookNode, output_file: Path, pdf=False, template_file='classicm'):
#     resources = {}
#     resources['unique_key'] = 'combined'
#     resources['output_files_dir'] = 'combined_files'
#
#     log.info('Converting to %s', 'pdf' if pdf else 'latex')
#     exporter = MyLatexPDFExporter() if pdf else MyLatexExporter()
#     if template_file is not None:
#         exporter.template_file = str(template_file)
#     writer = FilesWriter(build_directory=str(output_file.parent))
#     output, resources = exporter.from_notebook_node(combined_nb, resources)
#     writer.write(output, resources, notebook_name=output_file.stem)


class MyLatexExporter(LatexExporter):
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


def main():

    nb_path_lst = iter_notebook_paths('notebooks')
    print(len(nb_path_lst))
    nbnode = combine_notebooks(nb_path_lst)
    print(type(nbnode))
    exporter = NotebookExporter
    body, resources = exporter.from_notebook_node(nbnode)
    #writer = FilesWriter()
    #writer.write(body, resources, notebook_name='whole_book')

if __name__ == '__main__':
    main()
