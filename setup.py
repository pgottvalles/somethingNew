#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from shutil import rmtree
from setuptools import find_packages, setup, Command

# ------------------------------
# Parameters [edit]
# ------------------------------
NAME            = 'vendingmachine'
DESCRIPTION     = 'vendingmachine'
URL             = 'https://github.com/pgottvalles/somethingNew'
AUTHOR          = 'Patrick Gottvalles'
AUTHOR_EMAIL    = 'patrick.gottvalles@hotmail.com'
REQUIRES_PYTHON = '>=3.6.0'

# ------------------------------
# Required packages [edit]
#
# Only add what is required to launch the EMR job here, e.g., from Jenkins
# Do not add EMR job requirements here (pandas etc.).
# Put them in setup_emr.sh instead
# ------------------------------
REQUIRED = [
    'sqlite3'
]

# ------------------------------
# Set up tests [edit]
# By default there are not tests and no requirements for them. Add your own.
# ------------------------------
TEST_REQUIRED = [
    'sqlite3'
]

# ------------------------------
# Optional packages
# ------------------------------

EXTRAS = {}

# ------------------------------
# Do not edit from here onwards!
# ------------------------------

here = os.path.abspath(os.path.dirname(__file__))

def read_base_version_file():
    with open(os.path.join(here, 'BASE_VERSION'), 'r') as version_file:
            VERSION = version_file.read().strip()
    return VERSION

def read_version_file():
    with open(os.path.join(here, 'VERSION'), 'r') as version_file:
            VERSION = version_file.read().strip()
    return VERSION

def get_version_number():
    try:
        VERSION = read_version_file()
    except FileNotFoundError:
        VERSION = read_base_version_file()
    return VERSION

class DynamicVersionCommand(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        with open(os.path.join(here, 'BASE_VERSION')) as version_file:
            BASE_VERSION = version_file.read().strip()
        BUILD_SUFFIX = os.environ.get('BUILD_SUFFIX')
        if not BUILD_SUFFIX:
            VERSION = BASE_VERSION
        else:
            VERSION = BASE_VERSION + BUILD_SUFFIX
        with open(os.path.join(here, 'VERSION'), 'w') as version_file:
                version_file.write(VERSION)

class CleanCommand(Command):
    """Custom clean command to tidy up the project root."""
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        print('Removing previous builds…')
        try:
            os.remove(os.path.join(here, 'VERSION'))
        except OSError:
            pass
        rmtree(os.path.join(here, 'build'), ignore_errors=True)
        rmtree(os.path.join(here, 'dist'), ignore_errors=True)
        rmtree(os.path.join(here, NAME.replace("-", "_") + '.egg-info'), ignore_errors=True)

class PackageCommand(Command):
    """Build package."""
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        print('Building Source distribution…')
        os.system('{0} setup.py sdist --formats=zip'.format(sys.executable))

# Where the magic happens:
setup(
    name=NAME,
    version=get_version_number(),
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=('tests',)),
    install_requires=REQUIRED,
    tests_require=TEST_REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation :: CPython'
    ],
    # $ setup.py commands
    cmdclass={
        'clean': CleanCommand,
        'package': PackageCommand,
        'finalize_version': DynamicVersionCommand
    }
)
