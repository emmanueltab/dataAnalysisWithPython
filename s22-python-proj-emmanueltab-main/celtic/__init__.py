from celtic.parser import *
from celtic.stats import *
from celtic.viz import *
import turtle

hard_dependencies = ['turtle']
missing_dependencies = []

for dependency in hard_dependencies:
    try:
        __import__(dependency)

    except ImportError as e:
        missing_dependencies.append(dependency)

if len(missing_dependencies) != 0:
    for dependency in missing_dependencies:
        raise ImportError("Missing required dependencies {0}".format(dependency))
    print('Missing packages error, make sure to install/import them')
    exit(-1)

__doc__ = """
celtic - a powerful document text stats library for Python
=====================================================================
**celtic** is a Python package that offers ...
Main Features
-------------
  - Collects word counts
  - Calculates
  - Parsers
  - etc, etc.
"""
