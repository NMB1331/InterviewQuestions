import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):

    num_a = s.count('a')
    sub_len = len(s)
    leftover = n % sub_len
    num_leftover_a = s[0:leftover].count('a')
    
    total_a = 0
    # Get the number of a's in "whole" strings
    total_a += num_a * int(n / sub_len)
    total_a += num_leftover_a

    return total_a

if __name__ == '__main__':
    s1 = "gfcaaaecbg"
    n1 = 547602
    print("Number of A's in 1: {}".format(repeatedString(s1, n1)))