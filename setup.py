#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = [
    'selenium==3.141.0',
    'urllib3==1.25.9',
]

setup_requirements = []

test_requirements = []

setup(
    author="joao heron",
    author_email='joao.heron@indicium.tech',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Base crawler is an Python based tool which facilitates Selenium Framework usage",
    entry_points={
        'console_scripts': [
            'extract=src.cli:cli',
        ],
    },
    install_requires=requirements,
    license="Apache Software License 2.0",
    long_description=readme,
    include_package_data=True,
    package_dir={'base_crawler': 'base_crawler'},
    package_data={'base_crawler': ['res/assets/*', 'res/assets/*/*', 'res/assets/*/*/*', 'res/assets/*/*/*/*', 'res/assets/*/*/*/*/*']},
    keywords='base_crawler',
    name='base_crawler',
    packages=find_packages(include=['base_crawler', 'base_crawler.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/joaoheron/base_crawler',
    version='0.0.1',
    zip_safe=False,
)
