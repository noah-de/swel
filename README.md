# swel - wave analysis from spectral data
[![PyPI](https://img.shields.io/pypi/v/swel.svg?maxAge=2592000?style=plastic)](https://pypi.python.org/pypi/swel)
[![Build Status](https://travis-ci.org/noah-de/swel.svg?branch=master)](https://travis-ci.org/noah-de/swel)
[![Coverage Status](https://coveralls.io/repos/github/noah-de/swel/badge.svg?branch=master)](https://coveralls.io/github/noah-de/swel?branch=master)

[Spectral analysis](https://upcommons.upc.edu/bitstream/handle/2099.1/6034/06.pdf?sequence=7) of [real time raw spectral wave information](https://www.ndbc.noaa.gov/data_spec.shtml) from [NOAA](https://www.ndbc.noaa.gov/), calculating trends by plotting spectral moments. Data definitions are found on the [NOAA data spec page](https://www.ndbc.noaa.gov/data_spec.shtml).

![Significant Wave Height](https://github.com/noah-de/surf-report/blob/master/References/SWH.png)


![live image](https://github.com/noah-de/swel/raw/master/swel.png)
This is a python package that can be downloaded with [pip](https://pypi.org/project/swel/).
    
    pip install swel

## Testing included
This package was built with some tests:

    nosetests  --with-coverage --cover-package=swel -v

or
    
    pytest -v --cov=swel
    
[![DeepSource](https://static.deepsource.io/deepsource-badge-light.svg)](https://deepsource.io/gh/noah-de/swel/?ref=repository-badge)
