from codecs import open
from os.path import join, abspath, dirname
from setuptools import setup, find_packages
import os

here = abspath(dirname(__file__))

with open(join(here, 'README.md'), encoding='utf-8') as buff:
    long_description = buff.read()

setup(
    name="TextProcessing",
    version="1.0",
    description="Projeto 2 - TAP",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/diogocorreia01/PublicNewsArchive.git",
    author="Diogo Correia"
           "João Alexandre",
    author_email="diogo.correia01@outlook.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'spacy',
        'cleantext',
        'nltk',
        'bs4'
    ]
)