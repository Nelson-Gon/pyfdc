from setuptools import setup
setup(name='pyfdc',
        version='0.1',
        description='A python interface to FoodDataCentral',
        url='http://www.github.com/Nelson-Gon/pyfdc',
        author='Nelson Gonzabato',
        author_email='gonzabato@hotmail.com',
        license='MIT',
        packages=['python-fdc'],
        install_requires=['requests']
        zip_safe=False)
