#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import passcat

from setuptools import setup

setup(
    name='passcat',
    version=passcat.__version__,
    description='Passcat lets you generate cryptographically secure, memorable passphrases.',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author='Gael Gentil',
    author_email='iamcryptoki@gmail.com',
    url='https://github.com/iamcryptoki/passcat',
    license='MIT',
    keywords='passphrase, password, secret, security, words',
    packages=['passcat'],
    package_data={
        'passcat' : ['wordlists/*.txt']
    },
    install_requires=['docopt'],
    entry_points={
        'console_scripts': [
            'passcat=passcat.passcat:main',
        ]
    }
)
