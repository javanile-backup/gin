# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""


import re
from setuptools import setup


version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('gin/gin.py').read(),
    re.M
    ).group(1)


with open("README.md", "rb") as f:
    long_descr = f.read().decode("utf-8")


setup(
    name = "gin-cli",
    packages = ["gin"],
    entry_points = {
        "console_scripts": ['gin = gin.gin:main']
        },
    version = version,
    description = "GIN Python command line application bare bones template.",
    long_description = long_descr,
    author = "Francesco Bianco",
    author_email = "bianco@javanile.org",
    url = "https://github.com/Javanile/GIN",
    )
