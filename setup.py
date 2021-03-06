#!/usr/bin/env python
import os, sys
from setuptools import find_packages, setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit(0)

with open('README.rst', 'r') as f:
    long_description = f.read()

# Dynamically calculate the version based on picker.VERSION.
version=__import__('picker').get_version()

setup(
    name='picker',
    url='https://github.com/dakrauth/picker',
    author='David A Krauth',
    author_email='dakrauth@gmail.com',
    description='A Django sports picker app',
    version=version,
    long_description=long_description,
    platforms=['any'],
    license='MIT License',
    classifiers=(
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ),
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
