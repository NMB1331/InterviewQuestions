import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    current_height = 0
    height_delta = 0
    num_valleys = 0
    for step in s:
        # Update with current step
        if step == 'D':
            height_delta = -1
        elif step == 'U':
            height_delta = 1
        
        # For debugging
        #print("Current height: {} Step delta: {} Number of valleys: {}".format(current_height, height_delta, num_valleys))
        
        # Check if we just went into a valley
        if current_height == 0 and height_delta < 0:
            num_valleys += 1
        
        # Reset for the next step
        current_height += height_delta
        height_delta = 0
    
    # Return the number of valleys
    return num_valleys



if __name__ == "__main__":
    num_steps = 8
    step_sequence = "UDDDUDUU"
    print("Number of valleys: {}".format(countingValleys(num_steps, step_sequence)))