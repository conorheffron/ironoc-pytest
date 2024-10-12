from setuptools import setup, find_packages
from pip.req import parse_requirements

install_reqs = parse_requirements('requirements.txt', session='hack')

reqs = [str(ir.req) for ir in install_reqs]

setup(
    name="ironoc-pytest",
    version="1.3.3",
    packages=find_packages(),
    install_requires=reqs,
)
