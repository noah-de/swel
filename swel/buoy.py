import numpy as np
from urllib.request import urlretrieve
import logging

logging.basicConfig(level=logging.DEBUG)


class Buoy:
    URL = "https://www.ndbc.noaa.gov/data/realtime2/{}.data_spec"
    DEST = "./data/{}.data_spec"

    def __init__(self, buoy):
        """ Buoy initialization method
        accepts a NOAA buoy ID and initializes
        the data types for calculations"""

        logging.debug("initializing buoy")
        self.buoy = buoy
        self.dates = []
        self.Emid = None
        self.fmid = None
        self.df = None
        self.E = np.array([])
        self.f = np.array([])
        self.dest = None

    def get_data(self, dest=None):
        logging.debug("calling get_data()")
        url = self.URL.format(self.buoy)
        if dest is None:
            dest = self.DEST.format(self.buoy)

        local_filename, headers = urlretrieve(url, dest)
        logging.debug("urlretrieve got: {}".format(headers))
        logging.debug("Saving to {}".format(local_filename))
        self.dest = dest
        return dest

    @staticmethod
    def read_data(dest):
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

            E = np.array(energies)
            f = np.array(frequencies)
        return (E, f)

    def bootstrap(self, E, f):
        logging.debug("Got E: {}".format(str(E.shape)))
        self.Emid = self.calc_midpoint(E)
        self.fmid = self.calc_midpoint(f)
        self.df = np.diff(f)

    def calc_swh(self):
        product = self.df * self.Emid
        return 4 * np.sqrt(product.sum(axis=1))

    @staticmethod
    def calc_midpoint(series):
        logging.debug("calling calc_midpoint()")
        logging.debug("series: {}".format(type(series)))
        nofirst = series[:, 1:]  # every element in a row, not the first
        nolast = series[:, :-1]  # every element in a row, not the last
        mid = 0.5 * (nolast + nofirst)
        return mid
