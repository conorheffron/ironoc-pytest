from setuptools import setup
import os

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name="ironoc-pytest",
    version="2.1.3",
    install_requires=required,
)
