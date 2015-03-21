from distutils.core import setup
from setuptools import find_packages

setup(
    name='dh_carrinho',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    license='Apache 2.0',
    author='Eduardo Erlo',
    author_email='eduardo.erlo@gmail.com',
    description='App de carrinho de compras',
    long_description=open('README.rst').read(),
)
