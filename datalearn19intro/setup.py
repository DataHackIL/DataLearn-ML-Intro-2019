"""Setup for the datalearn19intro package."""

# !/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools


INSTALL_REQUIRES = [
    'numpy',
    'pandas'
]

with open('README.rst') as f:
    README = f.read()

setuptools.setup(
    author="Shay Palachy",
    author_email="shay.palachy@gmail.com",
    name='datalearn19intro',
    license="MIT",
    description='Helper code for DataLearn 2019 ML Intro Workshop.',
    version='v0.0.1',
    # cmdclass=versioneer.get_cmdclass(),
    long_description=README,
    url='https://github.com/DataHackIL/DataLearn-ML-Intro-2019',
    packages=setuptools.find_packages(),
    include_package_data=True,
    python_requires=">=3.5",
    install_requires=INSTALL_REQUIRES,
    # extras_require={
    #     'test': TEST_REQUIRES + INSTALL_REQUIRES,
    # },
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
    ],
)
