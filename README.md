# pyfdc: A python interface to FoodDataCentral
[![PyPI version fury.io](https://badge.fury.io/py/pyfdc.svg)](https://pypi.python.org/pypi/pyfdc/)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3764453.svg)](https://doi.org/10.5281/zenodo.3764453)
[![Project Status](http://www.repostatus.org/badges/latest/active.svg)](http://www.repostatus.org/#active) 
![Test-Package](https://github.com/Nelson-Gon/pyfdc/workflows/Test-Package/badge.svg)
![Travis Build](https://travis-ci.com/Nelson-Gon/pyfdc.svg?branch=master)
[![PyPI license](https://img.shields.io/pypi/l/pyfdc.svg)](https://pypi.python.org/pypi/pyfdc/)
[![Documentation Status](https://readthedocs.org/projects/pyfdc/badge/?version=latest)](https://pyfdc.readthedocs.io/en/latest/?badge=latest)
[![PyPI Downloads Month](https://img.shields.io/pypi/dm/pyfdc.svg)](https://pypi.python.org/pypi/pyfdc/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Nelson-Gon/pyfdc/graphs/commit-activity)
[![GitHub last commit](https://img.shields.io/github/last-commit/Nelson-Gon/pyfdc.svg)](https://github.com/Nelson-Gon/pyfdc/commits/master)
[![GitHub issues](https://img.shields.io/github/issues/Nelson-Gon/pyfdc.svg)](https://GitHub.com/Nelson-Gon/pyfdc/issues/)
[![GitHub issues-closed](https://img.shields.io/github/issues-closed/Nelson-Gon/pyfdc.svg)](https://GitHub.com/Nelson-Gon/pyfdc/issues?q=is%3Aissue+is%3Aclosed)



**Installation**

The simplest way to install the latest release is as follows:

```shell
pip install pyfdc

```

To install the development version:


Open the Terminal/CMD/Git bash/shell and enter

```shell

pip install git+https://github.com/Nelson-Gon/pyfdc.git

# or for the less stable dev version
pip install git+https://github.com/Nelson-Gon/pyfdc.git@develop

```

Otherwise:

```shell
# clone the repo
git clone git@github.com:Nelson-Gon/pyfdc.git
cd pyfdc
python3 setup.py install

```



**Sample usage**

```python

from pyfdc import *

```

**Set session api key**

To avoid providing an api key for each call, one can set a session api key as follows:

```python

utils.set_api_key("my_api_key_here")


```


**Key Features**

There is one major class `FoodDataCentral`. 
See the [changelog](https://github.com/Nelson-Gon/pyfdc/blob/master/changelog.md) 
for more details.:

To instantiate an object:

```python
my_search = FoodDataCentral()
```

To get details about foods for a given search term, one can do the following:

```python

my_search.get_food_info(search_phrase="sandwich",target_fields=["fdc_id","description","ingredients"]).head()

```

The above will result in the following output:

```shell

    fdc_id description                                        ingredients
0  485360    SANDWICH  TUSCAN BREAD (ENRICHED WHEAT FLOUR [WHEAT FLOU...
1  481873    SANDWICH  WHOLE GRAIN RYE FLOUR, VEGETABLE OIL (PALM, CA...
2  507441    SANDWICH  ONION ROLL [ENRICHED UNBLEACHED FLOUR (WHEAT F...
3  510847    SANDWICH  HONEY WHOLE WHEAT BREAD* [WHOLE WHEAT FLOUR*, ...
4  529731    SANDWICH  REDUCED FAT ICE CREAM [MILK, CREAM, FUDGE SAUC...
 


```






To get full details about a given `fdcId`, one can do the following:

```python

my_search.get_food_details(fdc_id=504905, target_field="ingredients")

```

This will give us the following output(truncated):

```shell

'MECHANICALLY SEPARATED CHICKEN, CHICKEN BROTH, WATER, CONTAINS LESS THAN 2% OF: SALT, SUGAR, SPICES, SODIUM PHOSPHATE, SODIUM ASCORBATE, SODIUM NITRITE, 
NATURAL FLAVORS, EXTRACTIVES OF PAPRIKA.'

```

To get nutrient details:

```shell

my_search.get_food_details(fdc_id= 496446,target_field="nutrients")

      id number                            name   rank unitName
0   1079    291            Fiber, total dietary   1200        g
1   1005    205     Carbohydrate, by difference   1110        g
2   1008    208                          Energy    300     kcal
3   1003    203                         Protein    600        g
4   1093    307                      Sodium, Na   5800       mg
5   1257    605        Fatty acids, total trans  15400        g
6   1004    204               Total lipid (fat)    800        g
7   1104    318                   Vitamin A, IU   7500       IU
8   1087    301                     Calcium, Ca   5300       mg
9   1162    401  Vitamin C, total ascorbic acid   6300       mg
10  1253    601                     Cholesterol  15700       mg
11  1258    606    Fatty acids, total saturated   9700        g
12  1089    303                        Iron, Fe   5400       mg


  

```


**Credit**

1. **Original Food Data Central API**

The API interfaced is available [here](https://fdc.nal.usda.gov/api-guide.html)

**Thank you very much**. 

> To report any issues, suggestions or improvement, please do so 
at [issues](https://github.com/Nelson-Gon/pyfdc/issues). 

> “Before software can be reusable it first has to be usable.” – Ralph Johnson

---

If you would like to cite this work, please use:

Nelson Gonzabato(2020) pyfdc: A python interface to FoodDataCentral, https://github.com/Nelson-Gon/pyfdc

BibTex:

```shell
@misc{Gonzabato2020,
  author = {Gonzabato, N},
  title = {pyfdc: A python interface to FoodDataCentral},
  year = {2020},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/Nelson-Gon/pyfdc}},
  commit = {ead2bef877ef28ff75b949267f95cf1ceb09c5c4}
} 
```