from distutils.core import setup
from setuptools import find_packages

setup(
    name='django-shopping-cart',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    license='Apache 2.0',
    author='Eduardo Erlo',
    author_email='eduardo.erlo@gmail.com',
    description='App de carrinho de compras',
    long_description=open('README.md').read(),
    install_requires=[
        'django>=1.5,<1.8',
        'coverage==3.7.1',
        'django-nose==1.3',
        'model-mommy==1.2.3',
        'nose==1.3.4',
        'nosexcover==1.0.10',
    ]
)
