#/usr/bin/env python

import codecs
import os
import sys

from os.path import join, dirname
from setuptools import setup


read = lambda filepath: codecs.open(filepath, 'r', 'utf-8').read()

if 'publish' in sys.argv:
    os.system('python setup.py sdist upload')
    sys.exit()

setup(
    name='Flask Session Cookie Decoder/Encoder',
    version="1.2",
    description="simple Python script to deal with Flask session cookie"
    long_description=read(join(dirname(__file__), 'README.md')),
    keywords='Flask session cookie',
    author='Wilson Sumanang, Alexandre ZANNI',
    maintainer='Alexandre ZANNI, Tabdiukov',
    license='Unknown License',
    url='https://github.com/noraj/flask-session-cookie-manager',
    include_package_data=True,
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Security',
    ],
)