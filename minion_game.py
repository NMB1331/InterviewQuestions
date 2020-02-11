"""
This code solves "The Minion Game" from HackerRank. Given a substring, it finds
all other substrings, and assigns a point for each occurence in the original 
string.
https://www.hackerrank.com/challenges/the-minion-game/problem

Algorithm:
- Compute all substrings
- Sort into whether or not they start with a vowel
- Count the number of occurences

Author: Nathaniel M. Burley
"""

import string

# Function that checks if given character is a vowel
def is_vowel(char):
    if char in ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']:
        return 1
    else:
        return 0

# Function that computes all substrings for a given string
def get_substrings(test_str):
    res = [test_str[i: j] for i in range(len(test_str)) 
          for j in range(i + 1, len(test_str) + 1)]
    res_uniq = []
    [res_uniq.append(x) for x in res if x not in res_uniq]
    print(res_uniq)
    return res_uniq

# Function that scores the substrings (1 pt. per occurence)
def score_substrings(test_str, substrings):
    vowel_score = 0
    consonant_score = 0
    for substr in substrings:
        if is_vowel(substr[0]):
            count = test_str.count(substr)
            vowel_score += count
            #print("Substring: {} Count: {}".format(substr, count))
        else:
            count = test_str.count(substr)
            consonant_score += count
            #print("Substring: {} Count: {}".format(substr, count))
    return vowel_score, consonant_score


# Main function— tests our code for the string BANANA
if __name__ == "__main__":
    game_str = "BANANA"
    score_A, score_B = score_substrings(game_str, get_substrings(game_str))
    print("Player A scored {}, Player B scored {}".format(score_A, score_B))
    if (score_A > score_B):
        print("Player A wins!")
    elif score_B > score_A:
        print("Player B wins!")
    else:
        print("It's a tie!")