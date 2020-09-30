#!/usr/bin/env python
import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="splitpdf",
    version="0.0.1",
    author="Raphaël Margueron",
    author_email="raphael.margueron@gmail.com",
    description=(""),
    license="",
    keywords="",
    url="https://github.com/TheRaphael0000/splitpdf",
    packages=["splitpdf"],
    long_description=read("README.md"),
    classifiers=[],
    install_requires=read("requirements.txt"),
    entry_points={
        "console_scripts": [
            "pdfsplit=splitpdf.__main__:main"
        ]
    },
)
