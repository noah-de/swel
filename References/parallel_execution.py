import timeit
from concurrent import futures
import requests

URL_string = "https://www.ndbc.noaa.gov/data/realtime2/{}.data_spec"

def get_raw_data(buoy_id):
    URL = "https://www.ndbc.noaa.gov/data/realtime2/{}.data_spec".format(buoy_id)
    raw_request = requests.get(URL)
    lines = raw_data.split("\n")
    return(lines[:100])
    

buoys = [
    46053,  # E. Santa Barbara
    46054,  # W. Santa Barbara
    46086,  # San Clemente Basin
    46219,  # San Nicolas Island
    46025,  # Santa Monica Basin
    46069,  # South Santa Rosa Island
]

def find_all_lines(ids):
    all_lines = []
    with futures.ProcessPoolExecutor() as pool:
        for lines in pool.map(get_raw_data, buoys):
            all_lines.append(lines)
    return all_lines

timeit.timeit(find_all_lines(buoys))
