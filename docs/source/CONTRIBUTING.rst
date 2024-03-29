
Contributing to pyfdc
=====================

This document provides guidelines for contributions to ``pyfdc``.

**Kinds of contribution**


* Typo fixes
* Documentation enhancements
* Pull requests

**Fixing typos and enhancing documentation**

To fix typos and/or grammatical errors, please edit the corresponding ``.py`` or ``.md`` file that 
generates the documentation. 

Please also update documentation by running ``bash scripts/mkdocs.sh`` as described also later. 

**Pull Requests**


* 
  Please raise an issue for discussion and reproducibility checks at https://github.com/Nelson-Gon/pyfdc/issues

* 
  Once the bug/enhancement is approved, please create a Git branch for the pull request.

* 
  Make changes and ensure that builds are passing the necessary checks on Travis.

* 
  Update ``changelog.md`` to reflect the changes made.

* 
  Do the following:

.. code-block::

   bash scripts/mkdocs.sh

`See also <https://samnicholls.net/2016/06/15/how-to-sphinx-readthedocs/>`_ for a guide on Sphinx documentation.

**Commit messages**

Please write commit messages in the format "Extends functionality" instead of "Extended functionality".

**Maintainers only notice**

**Releasing**

This should ideally not be run since we are auto-releasing via a GitHub action. If for some reason you would like to
release a new version manually, then:

.. code-block:: shell

   bash scripts/release.sh

The above does the following:


* Makes ``dist`` with ``python setup.py sdist`` at the very minimum. Ensure everything necessary is included in
  ``Manifest.in``. 
* Uploads ``dist`` to test.pypi.org with ``twine upload --repository-url https://test.pypi.org/legacy/ dist/*``
* If everything looks good, asks you to upload to pypi.org with ``twine upload dist/*``

Please note that the 'pyfdc' project is released with a
`Contributor Code of Conduct <https://github/com/Nelson-Gon/pyfdc/.github/CODE_OF_CONDUCT.md>`_.
By contributing to this project, you agree to abide by its terms.
