from setuptools import setup, find_packages


setup(name='pyfdc',
      version='0.1.3',
      description='A python interface to FoodDataCentral',
      url='http://www.github.com/Nelson-Gon/pyfdc',
      download_url="https://github.com/Nelson-Gon/pyfdc/archive/v0.1.2.zip",
      author='Nelson Gonzabato',
      author_email='gonzabato@hotmail.com',
      license='MIT',
      keywords="nutrition food agriculture rest api",
      packages=find_packages(),
      long_description=open('README.md').read(),
      long_description_content_type='text/markdown',
      install_requires=['requests', 'pandas'],
      python_requires='>=3.6',
      zip_safe=False)
