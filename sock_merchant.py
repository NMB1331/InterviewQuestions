"""
Code for the HackerRank SockMerchant challenge.

Source:
https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
"""

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    # Build hash table with counts of each kind of socks
    sock_hash_table = {}
    for sock in ar:
        try:
            sock_hash_table[sock] += 1
        except:
            sock_hash_table[sock] = 1
    
    # For debugging
    print(sock_hash_table)

    # Count the number of pairs of each type
    pair_count = 0
    for num_socks in sock_hash_table.values():
        pair_count += int(num_socks / 2)
    
    return pair_count


if __name__ == "__main__":
    num_socks = 9
    sock_arr = [10,20,20,10,10,30,50,10,20]
    print(sockMerchant(num_socks, sock_arr))