#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""
import os

from pytuneteller.version import get_version

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'beautifulsoup4',
    'docopt',
    'requests',
]

setup_requirements = [
    # TODO(yujinyuz): put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    'pytest',
    'tox',
    'flake8',
    'vcrpy-unittest',
]

setup(
    name='pytuneteller',
    version=get_version(),
    description="A python horoscope fortune teller made for fun.",
    long_description=readme + '\n\n' + history,
    author="Eugene Oliveros",
    author_email='eevoliveros@gmail.com',
    url='https://github.com/yujinyuz/pytuneteller',
    packages=find_packages(include=['pytuneteller']),
    package_data={
        'pytuneteller': [os.path.join('words', 'adjectives.txt'), os.path.join('words', 'nouns.txt')],
    },
    entry_points={
        'console_scripts': ['pytuneteller = pytuneteller.cli:main'],
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='pytuneteller, horoscope, astrology, fun',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
    python_requires='>=3',
)
