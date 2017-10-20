#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'beautifulsoup4',
    'docopt',
    'lxml',
    'requests',
]

setup_requirements = [
    # TODO(yujinyuz): put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    'pytest',
    'tox',
    'flake8',
]

setup(
    name='pytuneteller',
    version='0.1.1',
    description="A python horoscope fortune teller made for fun.",
    long_description=readme + '\n\n' + history,
    author="Eugene Essun Oliveros",
    author_email='jinyuzprodigy@gmail.com',
    url='https://github.com/yujinyuz/pytuneteller',
    packages=find_packages(include=['pytuneteller']),
    entry_points={
        'console_scripts': ['pytuneteller = pytuneteller:main'],
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='pytuneteller',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
