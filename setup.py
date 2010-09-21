import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "nw-nwgeolocation",
    version = "0.1",
    url = 'http://github.com/un33k/nw-nwgeolocation',
    license = 'BSD',
    description = "Use geopy to get a lat/long of a location from google API",
    long_description = read('README'),

    author = 'Val Lee',
    author_email = 'uneekvu@gmail.com',

    packages = find_packages('src'),
    package_dir = {'': 'src'},
    
    install_requires = ['setuptools', 'geopy'],

    classifiers = [
        'Development Status :: 1 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet',
    ]
)
