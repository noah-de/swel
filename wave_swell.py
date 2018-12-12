import numpy as np
from urllib.request import urlretrieve

# the address to the buoy data (should pass in as argument)
# 46053 = E. Santa Barbara
# 46054 = W. Santa Barbara
# 46217 = Anacapa Passage
# 46086 = San Clemente Basin
# 46219 = San Nicolas Island

filename = '46054' # the buoy name
url = 'https://www.ndbc.noaa.gov/data/realtime2/{}.data_spec'.format(filename)
dest = './{}.data_spec'.format(filename)
urlretrieve(url, dest)

dest = './{}.data_spec'.format(filename)

dates = []
energies = []
frequencies = []

with open(dest) as fp:
    for _ in range(3):
        next(fp)
    
    for l in fp:

        dates.append(l.split()[0:5])
        # separation_frequency = l.split()[5] # this value is ignored
        
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

# Average of frequency pairs comparing each frequency with the one after it
df = np.diff(f)

# calculate the energy mid-point
notfirst = E[:,1:]       # every element in a row, except for the first
notlast  = E[:,:-1]      # every element in a row, except for the last
Emid = .5 * (notlast + notfirst)

# calculate the frequency mid-point
fmid = .5*(f[:,:-1] + f[:,1:])

# significant wave height
product = (df*Emid)
SWH = 4*np.sqrt(product.sum(axis=1));
SWHflipped = SWH[::-1]
print(SWHflipped)

# define period second intervals
p = np.array([0,5,7,9,11,13,15,17,19,21,35])

# period mid-point
notfirst = p[1:]       # every element in a row, except for the first
notlast  = p[:-1]      # every element in a row, except for the last
pmid = .5*(notfirst + notlast)

# shift the focus from frequencies to periods
pf = 1./fmid

#print("pf:\n",pf)
