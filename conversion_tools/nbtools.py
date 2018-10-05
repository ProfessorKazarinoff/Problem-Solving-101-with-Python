# nbtools.py
"""
A set of functions that:
run jupyter notebooks
save jupyter notebooks
do other things needed with jupyter notebooks
"""

from pathlib import Path
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

def nbrun(notebook_Path):
    """
    nb run is a function that runs jupyter notebooks. This is useful because it will set all the In[#] numbers starting
    at In[1] for each notebook.
    :param notebook_Path: a python path object to a notebook path. Optionally a string which is a path to a notebook.
    :return: None
    """
    # need to do some sort of Path validation
    # need to do some sort of does it have an.ipynb extension check
    # need to do some sort of yes it is a valid notebook check
    #if not Path(notebook_Path).exists():
        #print(f'Notebook Path {notebook_Path} does not exist or is not a valid path')
        #return
    if Path(notebook_Path).exists():
        print(f'Running notebook: {notebook_Path}')
        # run the notebook. See: https://nbconvert.readthedocs.io/en/latest/execute_api.html#executing-notebooks-using-the-python-api-interface
        with open(notebook_Path) as f:
            nb = nbformat.read(f, as_version=4)
        ep = ExecutePreprocessor(timeout=600, kernel_name='python3') #configure the notebook executor
        ep.preprocess(nb, {'metadata': {'path': 'notebook_rundir/'}})      #run the notebook
        with open('notebook_Path', 'wt') as f:
            nbformat.write(nb, f)

