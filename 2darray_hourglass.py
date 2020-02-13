#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    total = 0
    max_total = 0
    for row_num in range(0, len(arr)-2):
        for row_index in range(0, len(arr[row_num])-2):
            print("Current top left: ({},{})".format(row_num, row_index))
            print("Current top middle: ({},{})".format(row_num, row_index+1))
            print("Current top right: ({},{})".format(row_num, row_index+2))
            print("Current middle: ({},{})".format(row_num+1, row_index+1))
            print("Current bottom left: ({},{})".format(row_num+2, row_index))
            print("Current bottom middle: ({},{})".format(row_num+2, row_index+1))
            print("Current bottom right: ({},{})".format(row_num+2, row_index+2))

            total += arr[row_num][row_index] # Adds hourglass top left
            total += arr[row_num][row_index+1] # Adds hourglass top middle
            total += arr[row_num][row_index+2] # Adds hourglass top right
            total += arr[row_num+1][row_index+1] # Adds hourglass middle
            total += arr[row_num+2][row_index] # Adds hourglass bottom left
            total += arr[row_num+2][row_index+1] # Adds hourglass bottom middle
            total += arr[row_num+2][row_index+2] # Adds hourglass bottom right

            print("Total: {}\n".format(total))
            if(row_index == 0 and row_num == 0):
                max_total = total
                total = 0
            elif (total > max_total):
                max_total = total
            total = 0

    print("Max total: {}".format(max_total))
    return max_total

if __name__ == '__main__':
    arr = [[-1,-1,0,-9,-2,-2],[-2,-1,-6,-8,-2,-5],[-1,-1,-1,-2,-3,-4],[-1,-9,-2,-4,-4,-5],[-7,-3,-3,-2,-9,-9],[-1,-3,-1,-2,-4,-5]]
    _ = hourglassSum(arr)
