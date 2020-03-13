
from setuptools import setup

import unittest
def my_tests():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests', pattern='test_*.py')
    return test_suite

setup(name='jsonobj',
      version='0.1',
      description='JSONobj - manipulation of JSON in python',
      url='http://github.com/goiosunw/jsonobj',
      author='Andre Goios',
      author_email='a.almeida@unsw.edu.au',
      license='GPL v3',
      packages=['pypevoc', 'pypevoc.speech'],
      test_suite = 'setup.my_tests',
      zip_safe=False)

