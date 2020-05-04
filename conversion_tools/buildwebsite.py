import nb2html
import copy_images_dir
import yaml_TOC
import make_mkdocs_yaml


def main():
    nb2html.main()
    copy_images_dir.main()
    yaml_TOC.main()
    make_mkdocs_yaml.main()


if __name__ == "__main__":
    main()
