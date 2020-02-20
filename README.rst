
pyfdc: A python interface to FoodDataCentral
============================================


.. image:: https://travis-ci.com/Nelson-Gon/pyfdc.svg?branch=master
   :target: https://travis-ci.com/Nelson-Gon/pyfdc.svg?branch=master
   :alt: Travis Build


.. image:: https://img.shields.io/badge/Maintained%3F-yes-green.svg
   :target: https://GitHub.com/Nelson-Gon/pyfdc/graphs/commit-activity
   :alt: Maintenance


.. image:: https://badge.fury.io/py/pyfdc.svg
   :target: https://pypi.python.org/pypi/pyfdc/
   :alt: PyPI version fury.io


.. image:: https://img.shields.io/pypi/l/pyfdc.svg
   :target: https://pypi.python.org/pypi/pyfdc/
   :alt: PyPI license


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

The simplest way to install is as follows:

.. code-block::

   pip install pyfdc

Alternatively,

Open the Terminal/CMD/Git bash/shell and enter

.. code-block::

   # You should use your default python interpreter
   python3.7 -m pip install git+https://github.com/Nelson-Gon/pyfdc.git

Otherwise:

.. code-block::

   # clone the repo
   git clone https://www.github.com/Nelson-Gon/pyfdc.git
   cd pyfdc
   python3 setup.py install

----

**Sample usage**

.. code-block::

   from pyfdc import *

**Set session api key**

To avoid providing an api key for each call, one can set a session api key as follows:

.. code-block::


   utils.set_api_key("my_api_key_here")

**Key Features**

There are two key classes defined in ``pyfdc``\ : 


#. ``FoodSearch`` implements the class for objects aimed at querying the database with a search term.
   To get details about foods for a given search term, one can do the following:

.. code-block::

   my_search = pyfdc.FoodSearch(search_phrase="nugget")
   list(my_search.get_food_info(target="fdcId"))

The above will result in the following output(truncated):

.. code-block::


   [[337348], [337394], [170725], [340673], [337347], [173721], [173722], [337346].....]]

To get descriptions of the different results:

.. code-block::


   list(my_search.get_food_info(target="description"))

This will result in the following result(truncated):

.. code-block::


   [['Chicken nuggets'], ['Turkey, nuggets'], ["WENDY'S, Chicken Nuggets"], ['Nutty Nuggets, Ralston Purina']]]

The simplest way to find out all available ``targets`` is to simply call:

.. code-block::


   list(my_search.get_food_info())

**This will throw an error showing what options are available.**\ :

.. code-block::


   target should be one of ['fdcId', 'description', 'scientificName', 'commonNames', 'additionalDescriptions', 'dataType', 'foodCode', 'gtinUpc', 'ndbNumber', 'publishedDate', 'brandOwner', 'ingredients', 'allHighlightFields', 'score']

For more details, please see the documentation of each of these classes and the
associated documents.

To get a ``DataFrame`` from multiple target fields, we can use ``get_multiple_details`` as shown:

.. code-block::

   my_search.get_multiple_details(["fdcId","foodCode","description"])
        fdcId  foodCode                                        description
   0   337348  24198740                                    Chicken nuggets
   1   337394  24208000                                    Turkey, nuggets
   2   170725  57316200                           WENDY'S, Chicken Nuggets
   3   340673  24198735                      Nutty Nuggets, Ralston Purina
   4   337347  24198730                 Chicken nuggets, from school lunch
   5   173721  26100260            Salmon nuggets, breaded, frozen, heated
   6   173722  13120310      Salmon nuggets, cooked as purchased, unheated


#. ``FoodDetails``

The ``FoodSearch`` class has an important advantage: it can allow us to obtain
FoodDataCentral(fdcId) IDs using a simple search term. To get full details about a given 
fdcId, one can do the following:

.. code-block::

   my_details = pyfdc.FoodDetails(fdc_id=504905)
   my_details.get_food_details("ingredients")

This will give us the following output(truncated):

.. code-block::


   MECHANICALLY SEPARATED CHICKEN, CHICKEN BROTH,

To get nutrient details, we can use the following which returns a list of all 
nutrient details. For brevity, only part of the first list item is shown.

.. code-block::


   list(my_details.get_nutrients())

   [      id number                  name  rank unitName
    0   1079    291  Fiber, total dietary  1200        g
    1   1079    291  Fiber, total dietary  1200        g
    2   1079    291  Fiber, total dietary  1200        g
    3   1079    291  Fiber, total dietary  1200        g
    4   1079    291  Fiber, total dietary  1200        g
    5   1079    291  Fiber, total dietary  1200        g
    6   1079    291  Fiber, total dietary  1200        g

To return a merge of the above results, we can use ``merge_food_nutrients`` as follows:

.. code-block::

   my_details.merge_nutrient_results()
        number                          name  rank unitName
   id                                                      
   1079    291          Fiber, total dietary  1200        g
   1079    291          Fiber, total dietary  1200        g
   1079    291          Fiber, total dietary  1200        g
   1079    291          Fiber, total dietary  1200        g
   1079    291          Fiber, total dietary  1200        g
        ...                           ...   ...      ...
   1258    606  Fatty acids, total saturated  9700        g
   1258    606  Fatty acids, total saturated  9700        g
   1258    606  Fatty acids, total saturated  9700        g
   1258    606  Fatty acids, total saturated  9700        g
   1258    606  Fatty acids, total saturated  9700        g
   [225 rows x 4 columns]
