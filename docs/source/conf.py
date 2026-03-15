# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
import django

# Add the project root (two levels up from docs/source)
sys.path.insert(0, os.path.abspath('../..'))

# ALSO add the capstone folder explicitly
sys.path.insert(0, os.path.abspath('../../capstone'))

# Point to the settings module inside the capstone folder
os.environ['DJANGO_SETTINGS_MODULE'] = 'capstone.settings'

django.setup()

project = 'Political Profile'
copyright = '2026, Victor Sifiso Xaba'
author = 'Victor Sifiso Xaba'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
