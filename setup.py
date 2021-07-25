from setuptools import setup, find_packages

DISTNAME = 'aditiplot'
DESCRIPTION = 'aditiplot: Applies an Aditi filter to your plots!'
MAINTAINER = 'Ryan Lane'
MAINTAINER_EMAIL = 'r.i.lane@tudelft.nl'
LICENSE = 'LICENSE.txt'
URL = 'https://github.com/hoogenboom-group/aditiplot'
VERSION = '0.1.dev'
PACKAGES = [
    'aditiplot',
]
INSTALL_REQUIRES = [
    'numpy',
    'pandas',
    'matplotlib',
    'seaborn',
]

if __name__ == '__main__':

    setup(
        name=DISTNAME,
        version=VERSION,
        author=MAINTAINER,
        author_email=MAINTAINER_EMAIL,
        packages=PACKAGES,
        include_package_data=True,
        url=URL,
        license=LICENSE,
        description=DESCRIPTION,
        long_description=open('README.md').read(),
        install_requires=INSTALL_REQUIRES,
    )
