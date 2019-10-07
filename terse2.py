import matplotlib.pyplot as plt
import numpy as np

from scipy.signal import savgol_filter
np.set_printoptions(precision=2)

import requests
import arrow

"""
READ data from NOAA into memory
"""
id = '46054'
URL = "https://www.ndbc.noaa.gov/data/realtime2/{}.data_spec".format(id)
date_format = 'YYYY-MM-DD HH:mm'
date_pattern = '{}-{}-{} {}:{}'
raw_request = requests.get(URL)
raw_data = raw_request.text

# These empty lists become lists of lists (a data matrix)
dates = []
energies = []
frequencies = []

for l in raw_data.split("\n"):
    if(len(l) > 100):

        # Parse the date into localized Arrow object
        di = l.split()[0:5]
        datestr = date_pattern.format(di[0],di[1],di[2],di[3],di[4])
        a = arrow.get(datestr, date_format)
        dates.append(a.to('US/Pacific'))

        # Energies are easy to parse: 1st from every other data pair
        energies.append([float(e) for e in l.split()[6::2]])

        # Frequecies are 2nd from every other data pair, without parenthesis
        freqs = l.split()[7::2]
        frequencies.append([float(i[1:-1]) for i in freqs])

# Create numpy arrays from the arrays
E = np.array(energies)                       # E for 'Energy'
f = np.array(frequencies)                    # f for 'frequency'
df = np.diff(f)

import pandas as pd
pandE = pd.DataFrame(E, index=dates)

fmid = .5*(f[:, :-1] + f[:, 1:])               # only used to consider
                                               # frequencies by period bins
Emid = .5*(E[:, :-1] + E[:, 1:])
p = np.array([0, 5, 7, 9, 11, 13]) # arbitrary periods
pmid = .5*(p[1:] + p[:-1])                   # mid-point resolution
Pf = 1./fmid[0, :]                            # convert from freq. to period

# plotting options
fig, ax = plt.subplots()
fig.set_size_inches(11, 5)
fig.savefig('SWH.png', dpi=100)

for idx, _ in enumerate(pmid):               # loop over period mid-point
                                             # indexes
                                             # (to make bins: period and neighbor)
    print("pmid[{}] = {}".format(idx,_))
    period_mask = (Pf > p[idx]) & (Pf <= p[idx+1]) # create a boolean mask of which period data will fit in this bin
    df_subset = df[:, period_mask]            # subset of frequency 
    Emid_subset = Emid[:, period_mask]        # subset Energy
    variance = (df_subset*Emid_subset)              
    SWH = (4*np.sqrt(variance.sum(axis=1)))  # 4*(sqrt of variance) rerturns the 'crest to trough' wave height
    if idx == 0:                             # creating a legend
        label = 'less than 5'
    else:
        label = p[idx]
    
    signif = SWH[0:15]* 3.28                 # convert meters to feet
    smoothed = savgol_filter(signif, 7, 2)   # apply a Savitzky-Golay filter
    ax.plot(smoothed,label=label)            # add it to the plot 

plt.gca().invert_xaxis()                     # invert the x axis (since it is looking back in time)
ax.set(xlabel='hours', ylabel='Wave height (ft)',
       title='Significant Wave height for the last 72 hours')
ax.legend(bbox_to_anchor=(1, .95))           # add the legend
ax.grid()
plt.show()
