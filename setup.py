from setuptools import setup
import os

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name="ironoc-pytest",
    version="1.6.5",
    install_requires=required,
)
