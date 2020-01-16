from setuptools import setup, find_packages
setup(name='pyfdc',
        version='0.1.0',
        description='A python interface to FoodDataCentral',
        url='http://www.github.com/Nelson-Gon/pyfdc',
        author='Nelson Gonzabato',
        author_email='gonzabato@hotmail.com',
        license='MIT',
        packages=find_packages(),
        install_requires=['requests', 'pandas'],
        python_requires='>=3.6',
        zip_safe=False)
