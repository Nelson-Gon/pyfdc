
pyfdc: A python interface to FoodDataCentral
============================================


.. image:: https://badge.fury.io/py/pyfdc.svg
   :target: https://pypi.python.org/pypi/pyfdc/
   :alt: PyPI version fury.io


.. image:: https://zenodo.org/badge/DOI/10.5281/zenodo.3764453.svg
   :target: https://doi.org/10.5281/zenodo.3764453
   :alt: DOI


.. image:: http://www.repostatus.org/badges/latest/active.svg
   :target: http://www.repostatus.org/#active
   :alt: Project Status
 

.. image:: https://codecov.io/gh/Nelson-Gon/pyfdc/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/Nelson-Gon/pyfdc?branch=master
   :alt: Codecov


.. image:: https://github.com/Nelson-Gon/pyfdc/workflows/Test-Package/badge.svg
   :target: https://github.com/Nelson-Gon/pyfdc/workflows/Test-Package/badge.svg
   :alt: Test-Package


.. image:: https://img.shields.io/pypi/l/pyfdc.svg
   :target: https://pypi.python.org/pypi/pyfdc/
   :alt: PyPI license


.. image:: https://readthedocs.org/projects/pyfdc/badge/?version=latest
   :target: https://pyfdc.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status


.. image:: https://pepy.tech/badge/pyfdc
   :target: https://pepy.tech/project/pyfdc
   :alt: Total Downloads


.. image:: https://pepy.tech/badge/pyfdc/month
   :target: https://pepy.tech/project/pyfdc
   :alt: Monthly Downloads


.. image:: https://pepy.tech/badge/pyfdc/week
   :target: https://pepy.tech/project/pyfdc
   :alt: Weekly Downloads


.. image:: https://img.shields.io/badge/Maintained%3F-yes-green.svg
   :target: https://GitHub.com/Nelson-Gon/pyfdc/graphs/commit-activity
   :alt: Maintenance


.. image:: https://img.shields.io/github/last-commit/Nelson-Gon/pyfdc.svg
   :target: https://github.com/Nelson-Gon/pyfdc/commits/master
   :alt: GitHub last commit


.. image:: https://img.shields.io/github/issues/Nelson-Gon/pyfdc.svg
   :target: https://GitHub.com/Nelson-Gon/pyfdc/issues/
   :alt: GitHub issues


.. image:: https://img.shields.io/github/issues-closed/Nelson-Gon/pyfdc.svg
   :target: https://GitHub.com/Nelson-Gon/pyfdc/issues?q=is%3Aissue+is%3Aclosed
   :alt: GitHub issues-closed


**Installation**

The simplest way to install the latest release is as follows:

.. code-block:: shell

   pip install pyfdc

To install the development version:

Open the Terminal/CMD/Git bash/shell and enter

.. code-block:: shell


   pip install git+https://github.com/Nelson-Gon/pyfdc.git

   # or for the less stable dev version
   pip install git+https://github.com/Nelson-Gon/pyfdc.git@develop

Otherwise:

.. code-block:: shell

   # clone the repo
   git clone git@github.com:Nelson-Gon/pyfdc.git
   cd pyfdc
   python3 -m pip install .

**Sample usage**

There are two ways to use ``pydfc``. In script mode, one does the following:

.. code-block:: shell

   python -m pyfdc --method "info" --phrase "cheese" | head
   #/pyfdc/pyfdc/pyfdc.py:109: UserWarning: No target_fields were provided, returning fdc_id, ingredients, and description.
   #  warn("No target_fields were provided, returning fdc_id, ingredients, and description.")
   #     fdc_id  ...                                   description
   #0    816524  ...                                        CHEESE
   #1   1463368  ...                                        CHEESE
   #2   1597534  ...                                        CHEESE
   #3   1653804  ...                                        CHEESE
   #4   1660793  ...                                        CHEESE
   #5   1497465  ...                                        CHEESE
   #6   1465399  ...                                        CHEESE
   #7    515803  ...                                        CHEESE
   #8    500370  ...                                        CHEESE
   #

The above uses the ``get_food_info`` method. To use, the ``get_food_details`` method, one simply sets method to "details" 
and provides the target FoodDataCentral ID. 

.. code-block:: shell

    python -m pyfdc --method "details" --phrase 816524  --fields "nutrients"

   #      id number                                      name   rank unitName
   #0   1004    204                         Total lipid (fat)    800        g
   #1   1257    605                  Fatty acids, total trans  15400        g
   #2   1079    291                      Fiber, total dietary   1200        g
   #3   1003    203                                   Protein    600        g
   #4   1005    205               Carbohydrate, by difference   1110        g
   #5   1110    324  Vitamin D (D2 + D3), International Units   8650       IU
   #6   1008    208                                    Energy    300     kcal
   #7   2000    269              Sugars, total including NLEA   1510        g
   #8   1089    303                                  Iron, Fe   5400       mg
   #9   1087    301                               Calcium, Ca   5300       mg
   #10  1258    606              Fatty acids, total saturated   9700        g
   #11  1093    307                                Sodium, Na   5800       mg
   #12  1253    601                               Cholesterol  15700       mg

.. code-block:: python


   from pyfdc.pyfdc import FoodDataCentral
   from pyfdc.utils import set_api_key

**Set session api key**

To avoid providing an api key for each call, one can set a session api key as follows:

.. code-block:: python


   set_api_key("my_api_key_here")

**Key Features**

There is one major class ``FoodDataCentral``. 
See the `changelog <https://github.com/Nelson-Gon/pyfdc/blob/master/changelog.md>`_ 
for more details.:

To instantiate an object:

.. code-block:: python

   my_search = FoodDataCentral()

To get details about foods for a given search term, one can do the following:

.. code-block:: python


   my_search.get_food_info(search_phrase="cheese").head(6)

The above will result in the following output:

.. code-block:: shell


   #
   #UserWarning: No target_fields were provided, returning fdc_id, ingredients, and description.
   #    fdc_id                                        ingredients description
   #0   816524  BELLAVITANO CHEESE (PASTEURIZED MILK, CHEESE C...      CHEESE
   #1  1210322  BELLAVITANO CHEESE (PASTEURIZED MILK, CHEESE C...      CHEESE
   #2  1291586  CHEDDAR CHEESE (PASTEURIZED MILK, CHEESE CULTU...      CHEESE
   #3  1305389   PASTEURIZED COWS' MILK, SALT, CULTURES, ENZYMES.      CHEESE
   #4  1361608  CULTURED PASTEURIZED MILK, SALT, NON-ANIMAL EN...      CHEESE
   #5  1420013  FRESH PART-SKIM COW'S MILK, CHEESE CULTURE SAL...      CHEESE

In the above, we got a warning message because we used defaults out-of-the-box. To customize, we can set 
the ``target_fields`` we wish to have.

.. code-block:: shell

   my_search.get_food_info(search_phrase="cheese", target_fields=["description"]).head(4)

   # description
   # 0      CHEESE
   # 1      CHEESE
   # 2      CHEESE
   # 3      CHEESE

To get full details about a given ``fdcId``\ , one can do the following:

.. code-block:: shell


   my_search.get_food_details(168977)

This will give us the following output(truncated):

.. code-block:: shell

   # UserWarning: No target_field was provided, returning low level results.
   #           0                                                  1
   #0                      fdcId                                             168977
   #1                description  Agutuk, meat-caribou (Alaskan ice cream) (Alas...
   #2            publicationDate                                           4/1/2019
   #3              foodNutrients  [{'nutrient': {'id': 2045, 'number': '951', 'n...
   #4                   dataType                                          SR Legacy

The above is a low-level result that may be useful for development purpises. 

To get nutrient details:

.. code-block:: shell


   my_search.get_food_details(fdc_id= 496446,target_field="nutrients")

   # nutrient.id nutrient.unitName                   nutrient.name  \
   #0         1089                mg                        Iron, Fe   
   #1         1258                 g    Fatty acids, total saturated   
   #2         1253                mg                     Cholesterol   
   #3         1162                mg  Vitamin C, total ascorbic acid   
   #4         1087                mg                     Calcium, Ca   
   #5         1104                IU                   Vitamin A, IU   
   #                  foodNutrientDerivation.description       id  amount  \
   #0  Calculated from a daily value percentage per s...  3992103    3.39   
   #1  Calculated from a daily value percentage per s...  3992107    0.47   
   #2  Calculated from a daily value percentage per s...  3992106    0.00   
   #3  Calculated from a daily value percentage per s...  3992105    0.00   
   #4  Calculated from a daily value percentage per s...  3992102  118.00   
   #5  Calculated from a daily value percentage per s...  3992104    0.00   
   #  nutrient.number  nutrient.rank  
   #0             303           5400  
   #1             606           9700  
   #2             601          15700  
   #3             401           6300

One can also get label nutrients (if they exist):

.. code-block:: shell

   my_search.get_food_details(504905, target_field="label_nutrients")

   #    fat  saturatedFat  transFat  cholesterol  sodium  ...  calcium  iron  potassium  addedSugar  calories
   #0  15.0           4.5       0.0         84.5  1060.0  ...     80.6  1.08       70.2        1.04       179

   #[1 rows x 14 columns]

**Credit**


#. **Original Food Data Central API**

The API interfaced is available `here <https://fdc.nal.usda.gov/api-guide.html>`_

**Thank you very much**. 

..

   To report any issues, suggestions or improvement, please do so 
   at `issues <https://github.com/Nelson-Gon/pyfdc/issues>`_. 

   “Before software can be reusable it first has to be usable.” – Ralph Johnson


----

If you would like to cite this work, please use:

Nelson Gonzabato(2020) pyfdc: A python interface to FoodDataCentral, https://github.com/Nelson-Gon/pyfdc

BibTex:

.. code-block:: shell

   @misc{Gonzabato2021,
     author = {Gonzabato, N},
     title = {pyfdc: A python interface to FoodDataCentral},
     year = {2021},
     publisher = {GitHub},
     journal = {GitHub repository},
     howpublished = {\url{https://github.com/Nelson-Gon/pyfdc}},
     commit = {20923d9dbea9dcf1b5cba741625b01f6637a6d7b}
   }
