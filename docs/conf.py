# -- Project information -----------------------------------------------------

project = 'Kaeyros Technical Handbook'
author = 'Kaeyros Analytics'
release = '0.1.0'

# -- General configuration ---------------------------------------------------

extensions = [
    'myst_parser',            # Enable Markdown support
    'sphinx.ext.autodoc',     # Automatically document Python modules
    'sphinx.ext.napoleon',    # Support for Google/NumPy docstrings
    'sphinx.ext.viewcode',    # Add links to source code
]

templates_path = ['_templates']
exclude_patterns = []

# Allow Markdown files as documentation sources
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# -- HTML output -------------------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
