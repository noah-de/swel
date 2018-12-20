import numpy as np
from urllib.request import urlretrieve

def calc_midpoint(series):
    nofirst = series[:,1:]       # every element in a row, except for the first
    nolast  = series[:,:-1]      # every element in a row, except for the last
    mid = .5 * (nolast + nofirst)
    return mid

def get_buoy_data(station = 46054):
    url = 'https://www.ndbc.noaa.gov/data/realtime2/{}.data_spec'.format(station)
    dest = './{}.data_spec'.format(station)
    urlretrieve(url, dest)
    return dest

def read_data(dest):
    '''Read the data file from NDBC (NOAA) and put it into a usable data
    structure
    https://www.ndbc.noaa.gov/data_spec.shtml
    @params:
      dest - the location of the file that has been saved to disk
    @returns:
      Energy
      frequency
    '''
    dates = []
    energies = []
    frequencies = []

    with open(dest) as fp:
        for _ in range(3):
            next(fp)

        for l in fp:
            # not using dates in matlab code, but it may be helpful here
            dates.append(l.split()[0:5])

            # [E] get wave energy data as E (meters squared per second)
            energies.append([float(e) for e in l.split()[6::2]])

            # [f] get frequency data as collection (1/seconds) measure of cycles per second
            freqs=l.split()[7::2]
            frequencies.append([float(i[1:-1]) for i in freqs])

        fp.close()
        # print("{}\t{}\t{}".format(len(dates), len(energies), len(frequencies)))

        # convert the lists to numpy arrays
        E = np.array(energies)    # E for 'Energy'
        f = np.array(frequencies) # f for 'frequency'
    return (E,f)

def calc_swh(E,f):
    # Average of frequency pairs comparing each frequency with the one after it
    df = np.diff(f)

    # calculate the energy mid-point
    Emid = calc_midpoint(E)

    # calculate the frequency mid-point
    fmid = calc_midpoint(f) # .5*(f[:,:-1] + f[:,1:])

    # significant wave height
    product = (df*Emid)
    return 4*np.sqrt(product.sum(axis=1));

def get_swh(list):
    '''
    params: list
    returns: dictionary that maps significant wave height data to a buoy number
    '''
    locations = {}

    for buoy in list:
        dest = get_buoy_data(buoy)
        E, f = read_data(dest)
        SWH = calc_swh(E,f)

        SWHflipped = SWH[::-1]
        print(SWHflipped)
        locations[buoy] = SWHflipped
    return locations

if __name__ == "__main__":
    buoys = [
            46053, # E. Santa Barbara
            46054, # W. Santa Barbara
            46217, # Anacapa Passage
            46086, # San Clemente Basin
            46219, # San Nicolas Island
            46025, # Santa Monica Basin
            46069, # South Santa Rosa Island
            ]

    locations = get_swh(buoys)
    print(type(locations))

    import matplotlib.pyplot as plt
    import numpy as np
    import seaborn as sns
    sns.set_style("darkgrid")
    for b, data in locations.items():
        plt.plot(data)
        print(b, data)
    plt.show()

# define period second intervals
# p = np.array([0,5,7,9,11,13,15,17,19,21,35])
#
# # period mid-point
# notfirst = p[1:]       # every element in a row, except for the first
# notlast  = p[:-1]      # every element in a row, except for the last
# pmid = .5*(notfirst + notlast)
#
# # shift the focus from frequencies to periods
# pf = 1./fmid

#print("pf:\n",pf)
