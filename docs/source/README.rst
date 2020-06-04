
pyfdc: A python interface to FoodDataCentral
============================================


.. image:: https://zenodo.org/badge/DOI/10.5281/zenodo.3764453.svg
   :target: https://doi.org/10.5281/zenodo.3764453
   :alt: DOI


.. image:: https://travis-ci.com/Nelson-Gon/pyfdc.svg?branch=master
   :target: https://travis-ci.com/Nelson-Gon/pyfdc.svg?branch=master
   :alt: Travis Build


.. image:: https://github.com/Nelson-Gon/pyfdc/workflows/Test-Package/badge.svg
   :target: https://github.com/Nelson-Gon/pyfdc/workflows/Test-Package/badge.svg
   :alt: Test-Package


.. image:: https://img.shields.io/badge/Maintained%3F-yes-green.svg
   :target: https://GitHub.com/Nelson-Gon/pyfdc/graphs/commit-activity
   :alt: Maintenance


.. image:: https://badge.fury.io/py/pyfdc.svg
   :target: https://pypi.python.org/pypi/pyfdc/
   :alt: PyPI version fury.io


.. image:: https://img.shields.io/pypi/l/pyfdc.svg
   :target: https://pypi.python.org/pypi/pyfdc/
   :alt: PyPI license


.. image:: https://img.shields.io/pypi/dm/pyfdc.svg
   :target: https://pypi.python.org/pypi/pyfdc/
   :alt: PyPI download Month


.. image:: https://img.shields.io/pypi/dw/pyfdc.svg
   :target: https://pypi.python.org/pypi/pyfdc/
   :alt: PyPI download week


.. image:: https://img.shields.io/pypi/dd/pyfdc.svg
   :target: https://pypi.python.org/pypi/pyfdc/
   :alt: PyPI download day


.. image:: http://www.repostatus.org/badges/latest/active.svg
   :target: http://www.repostatus.org/#active
   :alt: Project Status
 
 
.. image:: https://img.shields.io/github/last-commit/Nelson-Gon/pyfdc.svg
   :target: https://github.com/Nelson-Gon/pyfdc/commits/master
   :alt: GitHub last commit


.. image:: https://img.shields.io/badge/Made%20with-Python-1f425f.svg
   :target: https://www.python.org/
   :alt: made-with-python


.. image:: https://img.shields.io/github/issues/Nelson-Gon/pyfdc.svg
   :target: https://GitHub.com/Nelson-Gon/pyfdc/issues/
   :alt: GitHub issues


.. image:: https://img.shields.io/github/issues-closed/Nelson-Gon/pyfdc.svg
   :target: https://GitHub.com/Nelson-Gon/pyfdc/issues?q=is%3Aissue+is%3Aclosed
   :alt: GitHub issues-closed


----

**Installation**

The simplest way to install the latest release is as follows:

.. code-block::

   pip install pyfdc

To install the development version:

Open the Terminal/CMD/Git bash/shell and enter

.. code-block::


   pip install git+https://github.com/Nelson-Gon/pyfdc.git

   # or for the less stable dev version
   pip install git+https://github.com/Nelson-Gon/pyfdc.git@develop

Otherwise:

.. code-block::

   # clone the repo
   git clone https://www.github.com/Nelson-Gon/pyfdc.git
   cd pyfdc
   python3 setup.py install

**Building documentation**

----

**Sample usage**

.. code-block::

   from pyfdc import *

**Set session api key**

To avoid providing an api key for each call, one can set a session api key as follows:

.. code-block::


   utils.set_api_key("my_api_key_here")

**Key Features**

There is now one major class ``FoodDataCentral``. 
See the `changelog <https://github.com/Nelson-Gon/pyfdc/blob/master/changelog.md>`_ 
for more details.:

To instantiate an object:

.. code-block::

   my_search = FoodDataCentral()

   `

To get details about foods for a given search term, one can do the following:

.. code-block::


   list(my_search.get_food_info(search_phrase="kung pao", target="fdc_id"))

The above will result in the following output(truncated):

.. code-block::


   [[783264],
    [783328],
    [783287],
    [783389],
    [167676],
    [668446],
    [897958],
    [736522],
    [927376],

To get descriptions of the different results:

.. code-block::


   list(my_search.get_food_info(search_phrase="kung pao", target="description"))

This will result in the following result(truncated):

.. code-block::


   [['Kung Pao beef'],
    ['Kung pao chicken'],
    ['Kung Pao pork'],
    ['Kung Pao shrimp'],
    ['Restaurant, Chinese, kung pao chicken'],
    ['KUNG PAO SAUCE, KUNG PAO'],
    ['VEGAN KUNG PAO CHICKEN, KUNG PAO'],
    ['KUNG PAO STIR FRY SAUCE, KUNG PAO'],
    ['KUNG PAO STIR FRY SAUCE, KUNG PAO'],

The simplest way to find out all available ``targets`` is to simply call:

.. code-block::


   list(my_search.get_food_info())

**This will throw an error showing what options are available.**\ :

..

   KeyError: "target should be one of dict_keys(['fdc_id', 'description', 'scientific_name', 'common_names', 'additional_descriptions', 'gtin_upc', 'ndb_number', 'published_date', 'brand_owner', 'ingredients', 'score'])"


For more details, please see the docs for each function or raise an issue.

To get a ``DataFrame`` from multiple target fields, we can use ``get_multiple_details`` as shown:

.. code-block::

   my_my_search.get_multiple_details(search_phrase="tofu",target_fields=["fdc_id","description"])
   Out[128]: 
       fdc_id                                        description
   0   496446                                               TOFU
   1   411177                                               TOFU
   2   514921                                               TOFU
   3   388749                                               TOFU
   4   498775                                               TOFU
   5   391880                                               TOFU
   6   392410                                               TOFU
   7   167722                                        Tofu yogurt

To get full details about a given ``fdcId``\ , one can do the following:

.. code-block::


   my_search.get_food_details(fdc_id=504905, target_field="ingredients")

This will give us the following output(truncated):

.. code-block::


   'MECHANICALLY SEPARATED CHICKEN, CHICKEN BROTH, WATER, CONTAINS LESS THAN 2% OF: SALT, SUGAR, SPICES, SODIUM PHOSPHATE, SODIUM ASCORBATE, SODIUM NITRITE, 
   NATURAL FLAVORS, EXTRACTIVES OF PAPRIKA.'

To get nutrient details, we can use the following which returns a list of all 
nutrient details. For brevity, only part of the first list item is shown.

.. code-block::


   my_search.get_nutrients(fdc_id=" 496446")
   Out[131]: 
         id number                            name   rank unitName
   0   1087    301                     Calcium, Ca   5300       mg
   1   1089    303                        Iron, Fe   5400       mg
   2   1104    318                   Vitamin A, IU   7500       IU
   3   1162    401  Vitamin C, total ascorbic acid   6300       mg
   4   1253    601                     Cholesterol  15700       mg
   5   1258    606    Fatty acids, total saturated   9700        g
   6   1003    203                         Protein    600        g
   7   1004    204               Total lipid (fat)    800        g
   8   1005    205     Carbohydrate, by difference   1110        g

**Credit**


#. **Original Food Data Central API**

The API interfaced is available `here <https://fdc.nal.usda.gov/api-guide.html>`_

**Thank you very much**. 

..

   To report any issues, suggestions or improvement, please do so 
   at `issues <https://github.com/Nelson-Gon/pyfdc/issues>`_. 

   “Before software can be reusable it first has to be usable.” – Ralph Johnson

