
from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="parsons",
    version="0.1",

    description="Generate Parsons programming problems out of source code.",
    long_description=long_description,

    url='https://github.com/Limpan/parsons',

    author='Linus Törngren',
    author_email='linus@etnolit.se',

    license='MIT',

    classifiers=[
        'Development status :: 3 - Alpha',
        'Intended Audience :: Education',
        'Topic :: Education',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='parsons programming problem exercise',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=['click'],

    extras_requires={
        'dev': ['pytest, coverage'],
    },

    entry_points={
        'console_scripts': [
            'parsons=parsons:cli'
        ]
    },

    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)
