#!/usr/bin/env python

from distutils import log
from distutils.core import Command
import os
import sys
from subprocess import check_output

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__)))


execfile('bro/version.py')


with open('requirements.txt') as requirements:
    required = requirements.read().splitlines()


kwargs = {
    'name': 'bro',
    'version': str(__version__),
    'packages': find_packages(exclude=['tests*']),
    'include_package_data': True,
    'description': 'Bro - Semantic Source of Truth for Infrastructure',
    'author': 'Jathan McCollum',
    'maintainer': 'Jathan McCollum',
    'author_email': 'jathan@gmail.com',
    'maintainer_email': 'jathan@gmail.com',
    'license': 'Apache',
    'install_requires': required,
    'url': 'https://github.com/jathanism/bro',
    'tests_require': ['pytest'],
    # 'entry_points': """
    #     [console_scripts]
    #     nsot-server=nsot.util:main
    # """,
    'classifiers': [
        'Programming Language :: Python',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
}

setup(**kwargs)
