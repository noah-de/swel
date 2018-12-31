import os.path
from setuptools import find_packages, setup

# Package data
# ------------
_author = 'Noah Spahn'
_author_email = 'noah.de@gmail.com'
_classifiers = [
    'Environment :: Console',
    'Intended Audience :: Developers',
    'Intended Audience :: Information Technology',
    'Intended Audience :: Science/Research',
    'Topic :: Scientific/Engineering',
    'License :: OSI Approved :: Apache Software License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules',
]
_description = 'SWEL'
_download_url = 'http://pypi.python.org/pypi/swel/'
_requirements = ["beautifulsoup4", "future", "requests", "configparser"]
_keywords = ['NOAA', 'NBDC', 'oceanography', 'earth science', 'waves']
_license = 'Apache License, Version 2.0'
_long_description = 'A python utility'
_name = 'swel'
_namespaces = []
_test_suite = 'swel.tests'
_url = 'https://github.com/noah-de/swel'
_version = '0.0.1'
_zip_safe = False

# Setup Metadata
# --------------


def _read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

_header = '*' * len(_name) + '\n' + _name + '\n' + '*' * len(_name)
_longDescription = '\n\n'.join([
    _header,
    _read('README.md')
])
open('doc.txt', 'w').write(_longDescription)


setup(
    author=_author,
    author_email=_author_email,
    classifiers=_classifiers,
    description=_description,
    download_url=_download_url,
    include_package_data=True,
    install_requires=_requirements,
    keywords=_keywords,
    license=_license,
    long_description=_long_description,
    name=_name,
    namespace_packages=_namespaces,
    packages=find_packages(),
    test_suite=_test_suite,
    url=_url,
    version=_version,
    zip_safe=_zip_safe,
)

# setup(name='swel',
#       version='0.1',
#       description='calculate significant wave height periods from raw NOAA buoy data',
#       url='https://github.com/noah-de/swel',
#       author='Noah Spahn',
#       author_email='noah.de@gmail.com	',
#       license='MIT',
#       packages=['swel'],
#       zip_safe=False)
