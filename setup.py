# coding: utf-8

from setuptools import setup, find_packages


ENTRY_POINTS = {
    'console_scripts': ['armin-build=armin.console:build', ],
}

DEPENDENCIES = ['click', 'pyapi-gitlab', ]


setup(
    name='armin',
    version='0.0.1',
    author='tonic',
    zip_safe=False,
    author_email='tonic@e.hunantv.com',
    description='build rpm',
    install_requires=DEPENDENCIES,
    packages=find_packages(),
    entry_points=ENTRY_POINTS,
)
