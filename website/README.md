# Website for Problem Solving 101 with Python

The future website will be available at:

[https://professorkazarinoff.github.io/Problem-Solving-101-with-Python/](https://professorkazarinoff.github.io/Problem-Solving-101-with-Python/)

To build for yourself:

Install **mkdocs**, **mkdcos-material** theme, **jupyter**, **fabric** and clone the repo.

```
$ pip install mkdocs
$ pip install mkdocs-material
$ pip install jupyter
$ git clone https://github.com/ProfessorKazarinoff/Problem-Solving-101-with-Python.git
```

Move into the newly created **Problem-Solving-101-with-Python** directory and run the main script in **_nb2mkdocs.py_** to convert the Jupyter notebooks (.ipynb files) in the [notebooks directory](../notebooks) into markdown files (.md files) in the [website/docs](docs/) directory.

```
$ cd Problem-Solving-101-with-Python
$ cd website
```

Move into the **website** directory and make any changes to the **mkdocs.yml** file. Run ```mkdocs build``` and ```mkdocs serve```. Point a web browser to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

```
$ cd website
# make changes to the mkdocs.yml files

$ mkdocs build
$ mkdocs serve

# browse to http://127.0.0.1:8000/
```

To deploy and host on github pages, edit the **mkdocs.yml** file to include your repo url, then use ```mkdocs gh-deploy``` command to post the site on the **gh-pages** branch of your repo.

```
# in mkdocs.yml change repo_url: 'https://github.com/username/reponame/'

$ mkdocs gh-deploy
```

If ```mkdocs gh-deploy``` throws an error try:

```
$ git push -f origin gh-pages
```
