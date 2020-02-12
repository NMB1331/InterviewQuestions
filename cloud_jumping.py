import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    num_jumps = 0
    level_length = len(c)
    current_position = 0
    while (current_position != level_length-1):
        try:
            if c[current_position + 2] == 0:
                num_jumps += 1
                current_position += 2
            elif c[current_position + 1] == 0:
                num_jumps += 1
                current_position += 1
            #print("Array length: {} Current position: {}  Number of jumps: {}".format(level_length, current_position, num_jumps))
        except:
            #print("FAILING AT Array length: {} Current position: {}  Number of jumps: {}".format(level_length, current_position, num_jumps))
            return num_jumps+1
    return num_jumps


if __name__ == "__main__":
    clouds = [0,0,0,1,0,0]
    clouds1 = [0,0,1,0,0,1,0]
    print("Minimum number of jumps: {}".format(jumpingOnClouds(clouds)))
    print("Minimum number of jumps: {}".format(jumpingOnClouds(clouds1)))