import numpy as np
import logging
from urllib.request import urlretrieve

logging.basicConfig(level=logging.DEBUG)

'''
This is a mockup of running a calculation for multiple buoys
'''


def calc_midpoint(series):
    ''' Calculate the midpoint of a pair-wise numpy array (by row).
    the resulting series will have one fewer data-points (width)
    per row.

    :param series: a numpy 2D array

    :returns: a new numpy array containing the midpoint of each row
    '''
    nofirst = series[:, 1:]  # every element in a row, not the first
    nolast = series[:, :-1]  # every element in a row, not the last
    mid = 0.5 * (nolast + nofirst)
    return mid


def get_buoy_data(station=46054):
    url = "https://www.ndbc.noaa.gov/data/realtime2/{}.data_spec".format(station)
    dest = "./{}.data_spec".format(station)
    urlretrieve(url, dest)
    return dest


def read_data(dest):
    """
    Read the data file from NDBC (NOAA) and put it into a usable data
    structure
    https://www.ndbc.noaa.gov/data_spec.shtml

    :param dest: the location of the file that has been saved to disk

    :returns: tuple (Energy, frequency)
    """
    dates = []
    energies = []
    frequencies = []

    with open(dest) as fp:
        for _ in range(3):
            next(fp)

        for l in fp:
            dates.append(l.split()[0:5])
            energies.append([float(e) for e in l.split()[6::2]])
            freqs = l.split()[7::2]
            frequencies.append([float(i[1:-1]) for i in freqs])

        fp.close()
        # print("{}\t{}\t{}".format(len(dates), len(energies), len(frequencies)))

        E = np.array(energies)
        f = np.array(frequencies)
    return (E, f)


def calc_swh(E, f):
    df = np.diff(f)
    Emid = calc_midpoint(E)

    product = df * Emid
    return 4 * np.sqrt(product.sum(axis=1))


def get_swh(list):
    """
    params: list
    returns: dictionary that maps significant wave height data to a buoy number
    """
    locations = {}

    for buoy in list:
        dest = get_buoy_data(buoy)
        E, f = read_data(dest)
        SWH = calc_swh(E, f)

        SWHflipped = SWH[::-1]
        locations[buoy] = SWHflipped
    return locations


if __name__ == "__main__":
    buoys = [
        46053,  # E. Santa Barbara
        46054,  # W. Santa Barbara
        46217,  # Anacapa Passage
        46086,  # San Clemente Basin
        46219,  # San Nicolas Island
        46025,  # Santa Monica Basin
        46069,  # South Santa Rosa Island
    ]

    locations = get_swh(buoys)

    print(type(locations))

    import matplotlib.pyplot as plt
    import numpy as np
    import seaborn as sns

    sns.set_style("darkgrid")
    for b, data in locations.items():
        plt.plot(data)
        logging.debug(b)
    plt.show()

# define period second intervals
# p = np.array([0,5,7,9,11,13,15,17,19,21,35])
#
# # period mid-point
# notfirst = p[1:]   # every element in a row, except for the first
# notlast  = p[:-1]  # every element in a row, except for the last
# pmid = .5*(notfirst + notlast)
#
# # shift the focus from frequencies to periods
# pf = 1./fmid

# print("pf:\n",pf)
