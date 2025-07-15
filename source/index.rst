.. role:: python(code)
   :language: python

.. role:: cpp(code)
   :language: C++

.. highlight:: none

.. _My target:

===============================================
Welcome to Sphinx and ReStructuredText tutorial
===============================================
Sphinx 👨🦁🦅🇪🇬 is a site 🌐 generator 🤖🤖🤖 primarily 🥇 used in Python 🐍 documentation 🖹🤓. Sphinx used
**reStructuredText** (reST_) 🤔❓❓ as the default plaintext 😐🥱💤 markup ↕️ 📈 language 🦉💬. This is a
tutorial 🤓 to get everyone *comfortable* 😪😵 using both Sphinx and reST 🛏️🏨 for python ⛎
code 💻😎 documentation within the ✨✨group✨✨ as well as for preparing the code to go
🪩 public 🕺💃!

----------------
reStructuredText
----------------

Introduction
============
We will go over the capabilities of reStructuredText as well as code example.
The end goal is that we will prepare documents in a format of :code:`.rst` in
which Sphinx can read and generate a final :code:`html` file.

Section, title and subtitle
===========================
To create section, title and subtitle, reST_ uses :code:`=` and :code:`-` to
underline the title. For example, the title of this page, "Welcome to Sphinx
and ReStructuredText tutorial" is created using this command
::

  ===============================================
  Welcome to Sphinx and ReStructuredText tutorial
  ===============================================

Similarly, subtitle "reStructuredText" is generated using this command:
::

  ----------------
  reStructuredText
  ----------------

Finally, section "Section, title and subtitle" is generated using this:
::

  Section, title and subtitle
  ===========================

We also have subsection which hasn't been used up until this point. Simply
replace :code:`=` with :code:`-` to get subsection like so.

Testing subsection
------------------
testing subsection:
::

  Testing subsection
  ------------------

Do note that technically reST_ does not impose a strict rule for section
title and subtitle syntax. In fact, I could have used any of the following
symbols :code:`\`,.~*+^` either below or both above and below the title name
in any order. The reST_ will treat the first instance of the name as a section
and following instances as subsection, title, subtitle etc. The one that I
introduced is simply a convention that most people used.

Adding :code:`------------` will simply add horizontal line like so

-------------------------------

Need to be some text here to separate transitions :D

-------------------------------


Text styles and interpreted text roles
======================================
You might have noticed that I have used *Italic* and **Bold** in this document.
I have also used in-line code highlight :code:`like so`. This is all a part of
interpreted text role. Here is a list of a few useful text roles

1. literal: :literal:`:literal:`text`` will generate ``text``.

2. code: :literal:`:code:`text`` will generate :code:`text`. It might look
   similar to literal text roles but it has an option to take in language as
   an optional parameter through role directive (will cover this a bit later).
   For example, I can use :literal:`:python:`code(self,x)`` to generate
   :python:`code(self,x)` or :literal:`:cpp:`void code(int x)`` to generate
   :cpp:`void code(int x)`.

3. emphasis: :literal:`:emphasis:`text`` will generate :emphasis:`text`

4. math: ``:math:`\Sigma = iGW``` will generate :math:`\Sigma = iGW`

5. subscript/superscript: Typically white space or punctuation is required
   around interpreted text. However, that might not be desired in
   sub/superscript. For this, you can use backslash to escape the white space
   like so ``H\ :sub:`2`\ O`` will generate H\ :sub:`2`\ O. For comparison,
   this is mathmode :math:`\mathrm{H}_2\mathrm{O}`

6. Italic/ Bold: :literal:`*Italic* **BOLD**` will give *Italic* **BOLD**


See here for a full list of text roles_.

Hyperlink
=========
You can create hyperlink to external url like so reST_ using this command
:literal:`reST_` as well as defining the link associated with the target like so
:literal:`.. _reST: Your URL here`. Sphinx also allows for internal hyperlink
as well as crossreferencing (link across documents). For example,
`this <index.html#my-target>`_ will get you to the top of the :code:`index.html`
(current page). To do this, I simply put the target :literal:`.. _my-target:`
right before the section name. Then we can link the top of the page to the
word :literal:`this` by using :literal:`this <index.html#my-target>`.

.. important::
    The location of underscore is important here. Put _ before the target and after the link

Technically, the following is not reST_ but Sphinx syntax. We can instead use
:ref:`My target` to autogenerate the link (work across different source files
also). The syntax is a bit different. Here the target is defined like usual
but to generate hyperlink, use :literal:`:ref:`My target``. No :literal:`_` here!

Other syntax
============
As shown above, reST_ is versatile markup language. It allows not only list as
I have shown above, I can also insert image or add a table.

.. image:: sloth.gif

Image can be inserted via link or embed (through image option). Here's the
syntax for this image: :literal:`.. image:: sloth.gif`.

We can also add table

+------------------------+------------+----------+----------+
| Header row, column 1   | Header 2   | Header 3 | Header 4 |
+========================+============+==========+==========+
| body row 1, column 1   | column 2   | column 3 | Column 4 |
+------------------------+------------+----------+----------+
| body row 2             | Cells may span multiple columns  |
+------------------------+----------------------------------+

A syntax for this is a bit more complex, however:
::

    +------------------------+------------+----------+----------+
    | Header row, column 1   | Header 2   | Header 3 | Header 4 |
    +========================+============+==========+==========+
    | body row 1, column 1   | column 2   | column 3 | Column 4 |
    +------------------------+------------+----------+----------+
    | body row 2             | Cells may span multiple columns  |
    +------------------------+----------------------------------+

Directives
==========

This natually leads to reST_'s directives which simplify a lot of our problems.
A directive is similar to a function in a sense that you can add arguments to
modify the way it works. For example, the image I added was also a directive.
I can adjust it so that it is smaller, has alternate text (for text-to-speech
for visually impaired), align to center and is a clickable link:


.. image:: sloth.gif
   :scale: 50
   :align: center
   :alt: Sloth gif
   :target: https://www.stanford.edu/


Here is the literal text

::

   .. image:: sloth.gif
     :scale: 50
     :align: center
     :alt: Sloth gif
     :target: https://www.stanford.edu/


Here are some essential directives along with syntax:

Code:

.. code:: python
   :number-lines:

   class DirectKernel(KernelBase):
       def __init__(self, fname_wfn, **kwargs):
           self.fname_wfn = fname_wfn

           super(DirectKernel, self).__init__(fname_wfn, **kwargs)

   @staticmethod
   def load(fname):
       f = h5py.File(fname, 'r')
       kern = pickle.loads(f['pickled'][()])

       return kern

::

  .. code:: python
     :number-lines:
  
     class DirectKernel(KernelBase):
         def __init__(self, fname_wfn, **kwargs):
             self.fname_wfn = fname_wfn
  
             super(DirectKernel, self).__init__(fname_wfn, **kwargs)
  
     @staticmethod
     def load(fname):
         f = h5py.File(fname, 'r')
         kern = pickle.loads(f['pickled'][()])
  
         return kern
  

CSV-table:

.. csv-table:: Monthly transatlantic airtravel, in thousands of passengers, for 1958-1960 [CIT]_
   :file: airtravel.csv

.. [CIT] Burkardt, John. “CSV Files.” CSV files. Accessed October 7, 2024. https://people.sc.fsu.edu/~jburkardt/data/csv/csv.html. 

::

  .. csv-table:: Monthly transatlantic airtravel, in thousands of passengers, for 1958-1960 [CIT]_
     :file: airtravel.csv


Sphinx
======
Given that we can already generate html from plaintext, why do we need sphinx? Sphinx
essentially makes our life easier by setting the theme, and put together multiple html
files generated by reST_ as well as providing utility such as autogenerated doc from
python docstrings.

The main usage of Sphinx is called table-of-content (TOC) directives. As the name
suggests, toc generate a table of content which allows multiple pages of documentations
to be cohesively collected and neatly presented. Here we will outline out toc contents
and work on building necessary pages required for the content

TOC contents
============
Example toc contents to outline the structure of this sphinx tutorial

::

  crawler (maxdexpth: 2)
  ├── Installing Sphinx
  └── Getting started
      ├── Overview
      ├── Autodoc
      ├── Conf
      └── Example 

To generate toctree, I use the following commands
::

    .. toctree::
       :maxdepth: 2

       install
       tutorial/start

where maxdepth tells the crawler how far to traverse the tree. In this case, I need to create 2 files named
:literal:`install.rst` and :literal:`start.rst`.

.. toctree::
   :maxdepth: 2
   :titlesonly:

   install
   tutorial/start

.. _reST: https://docutils.sourceforge.io/docs/user/rst/quickstart.html
.. _roles: https://docutils.sourceforge.io/docs/ref/rst/roles.html
