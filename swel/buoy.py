import numpy as np
from urllib.request import urlretrieve


URL = "https://www.ndbc.noaa.gov/data/realtime2/{}.data_spec"
DEST = "./data/{}.data_spec"

class Buoy:

    def __init__(self, buoy):
        self.buoy = buoy
        self.dates = []
        self.E = np.array([])
        self.f = np.array([])

    def get_data(self):
        url = URL.format(self.buoy)
        dest = DEST.format(self.buoy)
        urlretrieve(url,dest)
        self.dest = dest
        return dest

    def read_data(self, dest):
        dates = []
        energies = []
        frequencies = []

        with open(dest) as fp: 
            for _ in range (3):
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
