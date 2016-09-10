#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='simpletestnames',
      version='1.0',
      packages=find_packages(),
      entry_points={
          'nose.plugins': [
              'SimpleTestNames = simpletestnames:SimpleTestNames'
          ]
      },
      description="Do not allow to use docstrings and give names just simple test address e.g. module_name.test_function_name",
)
