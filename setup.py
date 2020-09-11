#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_namespace_packages

###################################################################

VERSION = '0.2.0'
KEYWORDS = []
CLASSIFIERS = [
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Programming Language :: Python :: 3 :: Only',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
]

###################################################################


with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = [
    'numpy',
    'scipy',
    'nibabel',
    'numba',
    'six',
    'loguru',
    'fslpy',
    'zarr',
    'h5py',
]

setup(
    name='mcot.core',
    author='Michiel Cottaar',
    author_email='MichielCottaar@pm.me',
    version=VERSION,
    description="core utilities to work with my code",
    long_description=readme,
    long_description_content_type="text/x-rst",
    license="MIT",
    url="https://git.fmrib.ox.ac.uk/ndcn0236/mcutils",
    keywords=KEYWORDS,
    classifiers=CLASSIFIERS,
    install_requires=requirements,
    include_package_data=True,
    entry_points={'console_scripts': [
        'mcot=mcot.core.scripts:run',
    ]},
    packages=find_namespace_packages(include=['mcot.core']),
)
