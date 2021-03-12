from setuptools import setup, find_packages
from pyfdc.version import __version__

setup(name='pyfdc',
      version=__version__,
      description='A python interface to FoodDataCentral',
      url="http://www.github.com/Nelson-Gon/pyfdc",
      download_url="https://github.com/Nelson-Gon/pyfdc/",
      author='Nelson Gonzabato',
      author_email='gonzabato@hotmail.com',
      license='MIT',
      keywords="nutrition food agriculture rest api",
      packages=find_packages(),
      long_description=open('README.md', encoding="utf-8").read(),
      long_description_content_type='text/markdown',
      install_requires=['requests', 'pandas'],
      python_requires='>=3.6',
      zip_safe=False)
