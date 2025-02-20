# Configuration file for the Sphinx documentation builder.
import os
import sys

sys.path.insert(0, os.path.abspath("../.."))

# -- Project information
project = "HiddenLayer Python SDK"
copyright = "2024"
author = "HiddenLayer Integrations Team"

release = "2.0"
version = "2.0.1"

# -- General configuration

extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "myst_parser",
    "sphinx_copybutton",
]

autoclass_content = "both"
autodoc_typehints = "description"

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}
intersphinx_disabled_domains = ["std"]

templates_path = ["_templates"]

# -- Options for HTML output

html_theme = "press"

# -- Options for EPUB output
epub_show_urls = "footnote"
