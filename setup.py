#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=6.0', ]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
    author="Chris Ballinger",
    author_email='chris.ballinger@raizlabs.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPLv3 License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="Bluetooth Low Energy interface for SDS011 APM2.5 air quality sensor",
    entry_points={
        'console_scripts': [
            'aqi_ble=aqi_ble.cli:main',
        ],
    },
    install_requires=requirements,
    license="GPLv3 license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='aqi_ble',
    name='aqi_ble',
    packages=find_packages(include=['aqi_ble']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/Raizlabs/aqi_ble',
    version='0.1.0',
    zip_safe=False,
)
