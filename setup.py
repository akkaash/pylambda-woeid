#!/usr/bin/env python
import os
from setuptools import setup, find_packages

HERE = os.path.abspath(os.path.dirname(__file__))
VERSION = open(os.path.join(HERE, 'VERSION')).read().strip()

REQUIRED_EGGS = [
    'requests>=2.18.4',
]

setup(
    name='python.woeid',
    version=VERSION,
    description="",
    author="Akkaash Goel",
    url='',
    packages=find_packages(
        exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    # http://pythonhosted.org/distribute/setuptools.html#namespace-packages
    namespace_packages=['example'],
    package_data={'example': ['static/*.*', 'templates/*.*']},
    install_requires=REQUIRED_EGGS,
    extras_require=dict(
        test=REQUIRED_EGGS + [
            'pytest>=3.2',
        ],
        develop=REQUIRED_EGGS + [
            'ipdb>=0.10.2',
        ]),
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'index=example.index:handler'
        ],
    },
    dependency_links=[
    ],
)
