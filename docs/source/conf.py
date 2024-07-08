from datetime import date
from importlib.metadata import metadata

meta = metadata("dummy")
project = meta["Name"]
author = meta["Author"]
copyright = f"{date.today().year}, {author}"  # noqa: A001
release = meta["Version"]
version = release

# General configuration
extensions = ["sphinx.ext.autodoc", "sphinx.ext.napoleon"]
templates_path: list[str] = []
exclude_patterns: list[str] = []

# HTML options
html_theme = "sphinx_rtd_theme"
html_theme_options = {"navigation_depth": 2}
html_static_path: list[str] = []

# Autodoc options
autodoc_default_options = {"show-inheritance": True}
