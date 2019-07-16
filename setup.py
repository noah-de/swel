from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    author='Noah Spahn',
    author_email='noah.de@gmail.com',
    classifiers=[
    'Environment :: Console',
    'Intended Audience :: Developers',
    'Intended Audience :: Information Technology',
    'Intended Audience :: Science/Research',
    'Topic :: Scientific/Engineering',
    'License :: OSI Approved :: Apache Software License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules',
],
    description='A python utility to work with raw buoy data from NOAA.',
    include_package_data=True,
    keywords=['NOAA', 'NBDC', 'oceanography', 'earth science', 'waves'],
    license='Apache License, Version 2.0',
    long_description=long_description,
    name='swel',
    packages=find_packages(),
    test_suite='swel.tests',
    url='https://github.com/noah-de/swel',
    version='0.1.5.1',
    zip_safe=False,
)
