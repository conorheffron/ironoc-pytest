"""
Setup Project Meta & Config
"""
from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name="ironoc-pytest",
    version="2.2.6",
    install_requires=required,
)
