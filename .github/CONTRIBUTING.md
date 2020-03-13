# Contributing to pyfdc

This document provides guidelines for contributions to mde.

**Kinds of contribution**

* Typo fixes
* Documentation enhancements
* Pull requests


**Fixing typos and enhancing documentation**

To fix typos and/or grammatical errors, please edit the corresponding `.py` or `.md` file that generates the documentation. 

Please also update the docs using `sphinx`

**Pull Requests**

* Please raise an issue for discussion and reproducibility checks at [issues](https://github.com/Nelson-Gon/pyfdc/issues)

* Once the bug/enhancement is approved, please create a Git branch for the pull request.

* Make changes and ensure that builds are passing the necessary checks on Travis.

* Update `NEWS.md` to reflect the changes made.

* Do the following:

```

# The Makefile here is Windows specific

cd docs
python -m m2r ../README.md
# answer yes to overwrite
sphinx-build source build
# use make on *nix 
make.bat html

```
Please note that the 'pyfdc' project is released with a
[Contributor Code of Conduct](.github/CODE_OF_CONDUCT.md).
By contributing to this project, you agree to abide by its terms.
