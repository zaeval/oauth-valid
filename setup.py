import setuptools
import os

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="oauth-valid",
    version="0.1.8",
    author="zaeval",
    author_email="zaeval@among.software",
    description="oauth valid and it serve some utility",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zaeval/oauth-valid",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    zip_safe=False,
    install_requires=[
        "requests",
        "bs4",
    ],
)
