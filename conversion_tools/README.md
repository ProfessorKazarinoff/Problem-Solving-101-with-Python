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