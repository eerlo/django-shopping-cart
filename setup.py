from distutils.core import setup
from setuptools import find_packages

setup(
    name='dh_carrinho',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    license='Dark Horse License',
    author='Eduardo Erlo',
    author_email='eduardo@darkhorse.com.br',
    description='App de carrinho de compras',
    long_description=open('README.rst').read(),
)
