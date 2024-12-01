"""
--- Day 1: Historian Hysteria ---

"""

import pandas as pd
import numpy as np

def similarity_score(left_list, right_list):
    '''  
    Calculate a total similarity score by adding up each number in the left 
    list after multiplying it by the number of times that number appears in 
    the right list.
    
    inputs
    ------
    left_list: List/ Arr
        First list of location IDs
    right_list: List/ Arr
        Second list of location IDs
        
    returns
    -------
    sim_score: integer
        Similarity score between left and right list
    
    '''
    
    # running count for the similarity score
    sim_score = 0
    
    # get similarity score for each ID in the first list
    for i in range(len(left_list)):
        
        # singular location ID in first list
        current_loc_ID = left_list[i]
        
        # how many times does left list number appear in the right array
        no_appearances = np.count_nonzero(right_list == current_loc_ID)
        
        # add similarity score for current location ID to the similarity score
        sim_score += current_loc_ID*no_appearances
        
    return sim_score

# read input file
two_lists = pd.read_csv('input.txt', sep='\\s+', header = None)

# convert to numpy array
data_array = np.array(two_lists)

# separate the two lists, sort in ascending order
column_1 = np.sort(data_array[:, 0])  # first list
column_2 = np.sort(data_array[:, 1])  # second list

# get the total similarity score between the two ID lists
total_similarity_score = similarity_score(column_1, column_2) # np.abs to avoid -ve vals
print(total_similarity_score) # 21328497


        

