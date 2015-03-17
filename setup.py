#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from setuptools import setup, find_packages
from pip.req import parse_requirements
import csvexport

if sys.argv[-1] == "publish":
    os.system("python setup.py sdist upload")
    sys.exit()


with open('README.md') as f:
    readme = f.read()

requires = parse_requirements("requirements/install.txt")
install_requires = [str(ir.req) for ir in requires]

requires = parse_requirements("requirements/tests.txt")
tests_require = [str(ir.req) for ir in requires]

long_description = """
Simple csv to model parsing for Django.

---

%s

""" % readme


setup(
    name="django-csvexport",
    version=csvexport.__version__,
    description=("Simple csv to model parsing for Django."),
    long_description=long_description,
    author="Martin Sandström",
    author_email="martin@marteinn.se",
    url="https://github.com/marteinn/django-csvexport",
    packages=find_packages(exclude=('tests*',)),
    include_package_data=True,
    install_requires=install_requires,
    tests_require=tests_require,
    license="MIT",
    zip_safe=False,
    classifiers=(
        "Development Status :: 4 - Beta",
        'Environment :: Web Environment',
        "Intended Audience :: Developers",
        "Natural Language :: English",
        'Intended Audience :: Developers',
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        'Programming Language :: Python :: 2',
        "Programming Language :: Python :: 2.7",
        'Framework :: Django',
        'Topic :: Utilities',
    ),
)
