import os
from setuptools import setup

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst', format='md')
except(IOError, ImportError):
    long_description = open('README.md').read()

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = 'pyencodetools',
    packages=['pyencodetools'],
    version = '0.1.0',
    author = 'Christopher DeBoever',
    author_email = 'cdeboever3@gmail.com',
    description = ('Wraps ENCODE API and provides useful tools for working '
                   'with the ENCODE data.'),
    license = 'MIT',
    keywords = 'bioinformatics ENCODE wrapper API',
    url = 'https://github.com/cdeboever3/pyencodetools',
    download_url = 'https://github.com/cdeboever3/pyencodetools/tarball/0.1.0',
    long_description=long_description,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
   ]
)
