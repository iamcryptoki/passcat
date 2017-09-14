#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from distutils.core import setup

import passcat

setup(
    name='passcat',
    version='0.1.0',
    description='Passcat lets you generate cryptographically secure, memorable passphrases.',
    long_description=open('README.txt').read(),
    author='Galou Gentil',
    author_email='hello@cryptoki.fr',
    url='https://github.com/iamcryptoki/passcat',
    license='MIT',
    keywords='passphrase, password, security, words',
    packages=['passcat'],
    package_data={
        'passcat' : ['wordlists/*.txt']
    },
    entry_points={
        'console_scripts': [
            'passcat=passcat.passcat:main',
        ]
    }
)
