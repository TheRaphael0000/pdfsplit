#!/usr/bin/env python
import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="multipagespdftosinglepage",
    version="0.0.1",
    author="Raphaël Margueron",
    author_email="raphael.margueron@gmail.com",
    description=(""),
    license="",
    keywords="",
    url="https://github.com/TheRaphael0000/MultiPagesPdfToSinglePage",
    packages=['multipagespdftosinglepage'],
    long_description=read('README.md'),
    classifiers=[],
    entry_points={
        'console_scripts': [
            'multipagespdftosinglepage=multipagespdftosinglepage.__main__:main'
        ]
    },
)
