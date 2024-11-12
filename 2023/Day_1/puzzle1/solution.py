# -*- coding: utf-8 -*-
"""
DAY 1 - PUZZLE 1

You try to ask why they can't just use a weather machine ("not powerful enough") 
and where they're even sending you ("the sky") and why your map looks mostly 
blank ("you sure ask a lot of questions") and hang on did you just say the sky 
("of course, where do you think snow comes from") when you realize that the 
Elves are already loading you into a trebuchet ("please hold still, we need 
                                                to strap you in").

As they're making the final adjustments, they discover that their calibration 
document (your puzzle input) has been amended by a very young Elf who was 
apparently just excited to show off her art skills. Consequently, the Elves are 
having trouble reading the values on the document.

The newly-improved calibration document consists of lines of text; each line 
originally contained a specific calibration value that the Elves now need to 
recover. On each line, the calibration value can be found by combining the 
first digit and the last digit (in that order) to form a single two-digit 
number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

In this example, the calibration values of these four lines are 12, 38, 15, 
and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the 
calibration values?
"""

# imports 
import pandas as pd
import numpy as np
from pathlib import Path

def find_calibration_value(calibration_scribbling):
    '''
    Find the calibration value of an altered calibration value.
    
    A calibration value is determined as the combined 2 digit number of the 
    first and last number from the calibration scribbling, if only 1 number is 
    present both digits in the calibration value are assigned that number.

    Parameters
    ----------
    calibration_scribbling : STRING
        Amended calibration code.

    Returns
    -------
    calibration_code : INT.
        Calibration code found within the calibration_scribbling
    '''
    
    # break string into list containing each digit
    split_string = list(calibration_scribbling)
    #print(split_string)
    
    # find any integers in the calibration scribbling
    digits = [int(word) for word in split_string if word.isdigit()]
    #print(digits)
    
    # if only 1 digit found, calibration code is digit_digit
    if len(digits) == 1:
        calibration_code = int(f'{digits[0]}{digits[0]}')
        #print(calibration_code, type(calibration_code))
    
    # otherwise the code is made of the first and last digits found
    else:
        calibration_code = int(f'{digits[0]}{digits[-1]}')
        
    return calibration_code
        

# get input file path to messed up calibration codes
parent_directory = Path(__file__).resolve().parent
input_path = f'{parent_directory}/input.txt'

# read in the messed up calibration codes as pandas dataframe
read_input = pd.read_csv(input_path, header = None)

# convert data frame to numpy array and flatten array from 2D -> 1D
calibration_scribblings = np.array(read_input).flatten() # np.arr(str)
#print(calibration_scribblings[0])

#find_calibration_value(calibration_scribblings[0])

calibration_values_sum = 0

# find calibration code for each line in input file
for i in range(len(calibration_scribblings)):
    
    # add calibration code to running sum
    calibration_values_sum += find_calibration_value(calibration_scribblings[i])
    
print(f'The total sum of the calibration values is {calibration_values_sum}')
    


