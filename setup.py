from codecs import open
from os.path import join, abspath, dirname
from setuptools import setup

here = abspath(dirname(__file__))

with open(join(here, 'README.md'), encoding='utf-8') as buff:
    long_description = buff.read()

setup(
    name="TextProcessing",
    version="1.0",
    description="Projeto 2 - TAP",
    long_description_content_type="text/markdown",
    author="Diogo Correia"
           "João Alexandre",
    install_requires=[
        'spacy',
        'cleantext',
        'nltk',
        'bs4'
    ]
)