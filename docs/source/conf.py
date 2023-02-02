# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Ruijin Gastrointestinal CDSS'
copyright = '2023, kangkun'
author = 'kangkun'

release = '0.1'
version = '0.1.0'

html_theme = "sphinx_rtd_theme"

# -- General configuration

extensions = [
    # 'sphinx.ext.duration',
    # 'sphinx.ext.doctest',
    # 'sphinx.ext.autodoc',
    # 'sphinx.ext.autosummary',
    # 'sphinx.ext.intersphinx',
    # 'sphinx.ext.autosectionlabel',
    "multiproject",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinxcontrib.httpdomain",
    "sphinxcontrib.video",
    "djangodocs",
    "doc_extensions",
    "sphinx_tabs.tabs",
    "sphinx-prompt",
    "notfound.extension",
    "hoverxref.extension",
    "sphinx_search.extension",
    "sphinxemoji.sphinxemoji",
    "sphinx_design",
    "myst_parser",
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
