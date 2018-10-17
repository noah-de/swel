#function H = get_wave_data;
#
# the address to the buoy data (should pass in as argument)
# 46053 = E. Santa Barbara
# 46054 = W. Santa Barbara
# 46217 = Anacapa Passage
# 46086 = San Clemente Basin
# 46219 = San Nicolas Island
filename = '46054' # the buoy name
url = 'https://www.ndbc.noaa.gov/data/realtime2/{}.data_spec'.format(filename)
dest = './{}.data_spec'.format(filename)
from urllib.request import urlretrieve
urlretrieve(url, dest)
import pandas as pd
data = pd.read_csv(dest, sep='\s+')

# [f] get frequency data as collection (1/seconds) measure of cycles per second

# [E] get wave energy data as E (meters squared per second)

# [df] Average of frequency pairs comparing each frequency with the one after it

# [Emid] calculate the Energy mid-point

# [fmid] calculate the frequency mid-point

# [SWF] Significant wave height integrating across the entire range of frequencies
# as a function of wave periods

# [p] define the arbitrary period second intervals
p = [0,5,7,9,11,13,15,17,19,21,35]

# [Pmid] calculate the mid-point (between frequencies) Making plots nicer.

# [pf] shift the focus from frequencies to periods

# [SWHmid] # integrate the calculations: 4* sqrt(sum(df*Emid))

# PLOT the results
