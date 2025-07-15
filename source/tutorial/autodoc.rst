Autodoc
=======
One of the advantage of Sphinx code is the tool to autogenerate documentation
from python docstring (as long as your docstring is compatible with rst syntax)

To get it going, add :code:`'sphinx.ext.autodoc'` extension to the :code:`extensions`
list in :code:`conf.py`. Then import sys and add path to your code as the first index
like so:

.. code::

     import sys
     sys.path.insert(0, path_to_your_code_here)

Then you can simply add code documentation in your code by using automodule directive

::

  .. automodule:: fiss
     :members:

As an example, here is the result:

.. automodule:: fiss
   :members:
