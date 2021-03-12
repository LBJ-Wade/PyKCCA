'''
Forked from https://github.com/lorenzoriano/PyKCCA
Started modification on 12 March 2020
@author: Sambit Giri
Setup script
'''

#from setuptools import setup, find_packages
from distutils.core import setup


setup(name='PykCCA',
      version='0.0.1',
      author='Sambit Giri',
      author_email='sambit.giri@astro.su.se',
      package_dir = {'PykCCA' : 'src'},
      packages=['PykCCA'],
      #package_data={'share':['*'],},
      #install_requires=['numpy','scipy','scikit-learn','scikit-image'],
      #include_package_data=True,
)
