import nbconvert
import nbformat
from nbconvert import HTMLExporter
import os
from shutil import copyfile
import re


def copyImagesDocs(notebookdir="notebooks"):
    f = []
    REG_nb_dir = re.compile((r"(\d\d)-*"))
    for (dirpath, dirnames, filenames) in os.walk(os.path.join(os.pardir, notebookdir)):
        f.extend(dirnames)
        for dirname in dirnames:
            if not dirname.startswith(".ipynb_checkpoints") and REG_nb_dir.match(
                dirname
            ):
                if not os.path.exists(
                    os.path.join(os.pardir, "website", "docs", dirname)
                ):
                    os.mkdir(os.path.join(os.pardir, "website", "docs", dirname))
                    if not os.path.exists(
                        os.path.join(os.pardir, "website", "docs", dirname, "images")
                    ):
                        os.mkdir(
                            os.path.join(
                                os.pardir, "website", "docs", dirname, "images"
                            )
                        )
                imgs = os.listdir(
                    os.path.join(os.pardir, "notebooks", dirname, "images")
                )
                if imgs:
                    for img in imgs:
                        print(str(img))
                        if (
                            img.endswith(".png")
                            or img.endswith(".pdf")
                            or img.endswith(".jpg")
                        ):
                            src = os.path.join(
                                os.pardir, "notebooks", dirname, "images", img
                            )
                            dst = os.path.join(
                                os.pardir, "website", "docs", dirname, "images", img
                            )
                            copyfile(src, dst)


def main():
    # convertNotebooktoHTML('00.01-Motivation_test.ipynb','00.01-Motivation_test.html')
    copyImagesDocs("notebooks")


if __name__ == "__main__":
    main()
