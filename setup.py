#! /usr/bin/env python
#
# Copyright (C) 2018 3mission

DESCRIPTION = "Internet energy consumption simulation"
LONG_DESCRIPTION = """\
Simulation for energy consumption of the internet, and
online advertising.
"""

DISTNAME = 'energysim'
MAINTAINER = 'The Energy Guys'
MAINTAINER_EMAIL = 'no_reply@mail.com'
URL = ''
LICENSE = 'MIT'
DOWNLOAD_URL = 'https://github.com/3mission/energysim/'
VERSION = '0.1'

try:
    from setuptools import setup
    _has_setuptools = True
except ImportError:
    from distutils.core import setup

def check_dependencies():

    install_requires = []

    try:
        import numpy
    except ImportError:
        install_requires.append('numpy')
    try:
        import pandas
    except ImportError:
        install_requires.append('pandas')
    try:
        import astetik
    except ImportError:
        install_requires.append('astetik')

    return install_requires

if __name__ == "__main__":

    install_requires = check_dependencies()

    setup(name=DISTNAME,
        author=MAINTAINER,
        author_email=MAINTAINER_EMAIL,
        maintainer=MAINTAINER,
        maintainer_email=MAINTAINER_EMAIL,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        license=LICENSE,
        url=URL,
        version=VERSION,
        download_url=DOWNLOAD_URL,
        install_requires=install_requires,
        packages=['energysim'],

        classifiers=[
                     'Intended Audience :: Science/Research',
                     'Programming Language :: Python :: 3.6',
                     'License :: OSI Approved :: MIT License',
                     'Operating System :: POSIX',
                     'Operating System :: Unix',
                     'Operating System :: MacOS'],
)
