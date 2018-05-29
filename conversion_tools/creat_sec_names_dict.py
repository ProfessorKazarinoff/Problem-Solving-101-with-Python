# coding: utf-8

# ## Tool to remove dashes from names of files and put in a dictionary where:
#
# Key: Filename-with-dashes-and-extensions, Value: Name with no dashes or extensions

# In[86]:


import os

# In[87]:


os.getcwd

# In[88]:


os.getcwd()

# In[89]:


os.pardir

# In[90]:


os.listdir(os.path.join(os.pardir, 'notebooks'))

# In[91]:


notebookdir = os.path.join(os.pardir, 'notebooks')

# In[92]:




# In[93]:


filenameslst = []
for dirpath, dirnames, filenames in os.walk(notebookdir):
    for filename in filenames:
        filenameslst.append(filename)

# In[94]:


filenameslst

# In[95]:


notebook_file_names = [x for x in filenameslst if
                       x.endswith('.ipynb') and not x.startswith('TOC') and not x.endswith('-checkpoint.ipynb')]
notebook_file_names

# In[96]:


notebook_file_names_no_numbers = [''.join([i for i in s if not i.isdigit()]) for s in notebook_file_names]

# In[97]:


notebook_file_names_no_numbers

# In[98]:


notebook_file_names_no_numbers_no_ext = [s.replace('.ipynb', '') for s in notebook_file_names_no_numbers]

# In[99]:


notebook_file_names_no_numbers_no_ext_no_dot = [s.replace('.', '') for s in notebook_file_names_no_numbers_no_ext]

# In[100]:


notebook_file_names_no_numbers_no_ext_no_dot_no_start_dash = []
for s in notebook_file_names_no_numbers_no_ext_no_dot:
    if s.startswith('-'):
        s = s[1:]
    notebook_file_names_no_numbers_no_ext_no_dot_no_start_dash.append(s)

# In[101]:


notebook_file_names_no_numbers_no_ext_no_dot_no_start_dash

# In[102]:


section_names = [s.replace('-', ' ') for s in notebook_file_names_no_numbers_no_ext_no_dot_no_start_dash]

# In[103]:


section_names

# In[104]:


notebook_file_name_section_name_dict = dict(zip(section_names, notebook_file_names))

notebook_file_name_section_name_dict

print(notebook_file_name_section_name_dict)