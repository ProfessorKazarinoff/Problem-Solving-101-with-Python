from fabric.api import *
import fabric.contrib.project as project
import os
import shutil
import sys
import socketserver


def publishsite():
    #local('pelican content -s publishconf.py')
    #local('git add .')
    #local('git commit -m "published changes"')
    #local('git push origin master')
    #local('ghp-import output')
    local('git push -f origin gh-pages')