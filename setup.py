#/usr/bin/env python

import codecs
import os
import sys

from os.path import join, dirname
from setuptools import setup
import codecs


read = lambda filepath: codecs.open(filepath, 'r', 'utf-8').read()

if 'publish' in sys.argv:
    os.system('python -m twine upload dist/*')
    sys.exit()
if 'package' in sys.argv:
    os.system('python setup.py bdist bdist_egg')
    sys.exit()

setup(
    name='flask-session-cookie-manager',
    version='1.2.1.1',
    description="simple Python script to deal with Flask session cookie",
    long_description=read(join(dirname(__file__), 'README.md')),
    long_description_content_type='text/markdown',
    keywords='Flask session cookie',
    author='Wilson Sumanang, Alexandre ZANNI',
    maintainer='Alexandre ZANNI, TAbdiukov',
    license='MIT',
    url='https://github.com/noraj/flask-session-cookie-manager',
    include_package_data=True,
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'License :: Other/Proprietary License',
        'Topic :: Security',
        'Topic :: Utilities',
        'Environment :: Console',
        'Intended Audience :: Other Audience',
    ],
    install_requires=['itsdangerous', 'Flask'],
    # https://python-packaging.readthedocs.io/en/latest/command-line-scripts.html
    scripts=['flask_session_cookie_manager2.py', 'flask_session_cookie_manager3.py'],
)
