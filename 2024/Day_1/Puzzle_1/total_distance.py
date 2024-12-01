"""
--- Day 1: Historian Hysteria ---

"""

import pandas as pd
import numpy as np

# read input file
two_lists = pd.read_csv('input.txt', sep='\\s+', header = None)

# convert to numpy array
data_array = np.array(two_lists)

# separate the two lists, sort in ascending order
column_1 = np.sort(data_array[:, 0])  # first list
column_2 = np.sort(data_array[:, 1])  # second list

# get the distance between each location ID in the two lists
distances = np.abs(column_1 - column_2) # np.abs to avoid -ve vals

# total distance between the lists
total_distance = np.sum(distances)
print(total_distance) # 2742123

