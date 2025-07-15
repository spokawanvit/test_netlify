Conf file
=========
Sphinx handles extensions and theme through :code:`conf.py` file. Here I will
list a few useful sphinx extensions as well as the current theme used.

1. autodoc :code:`'sphinx.ext.autodoc'` for automatic conversion of python
   docstring to sphinx document. The doc string must still be written in
   reST_ format for this to work

2. napoleon :code:`'spinx.ext.napoleon'` which further simplify the reST_
   syntax. You might notice that the syntax can be quite heavy and confusion
   especially when written in plaintext inside your python code's docstring.
   This extension simply convert numpy and google docstring convention and
   automatically make it readable to reST_ code.

3. mathjax :code:`'sphinx.ext.mathjax'` make the math directive appears as-is
   in html. Note that `make pdf` would work without this extension. It is
   simply HTML does not support math mode natively and this extension first
   call LaTeX and convert the math to SVG images for the HTML to be able to
   handle math.

Current theme used is :code:`classic`. Here is a link to more themes to choose
from sphinx_theme_. 


.. _reST: https://docutils.sourceforge.io/docs/user/rst/quickstart.html
.. _sphinx_theme: https://sphinx-themes.org/#themes
