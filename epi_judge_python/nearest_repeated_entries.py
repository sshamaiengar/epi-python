from typing import List

from test_framework import generic_test

"""

Find index of first of closest repeated entries in array.
Hint: each entry in array is a candidate

Ex. [a,b,c,b,d,e,f] -> 1 (pair of b's)

Brute force:
Store all repeated entries in hash table, with list of indices as keys.
For each repeated key, find smallest consecutive pair. Return first index of global smallest.
O(n^2) time?, O(n) space

Track closest repeated as you go:
    Track last position of each val in a hash table, along with global smallest distance between repeats.
    Update things when repeat val is hit.
    Return last index of global smallest result.
O(n) time, O(d) space for d distinct entries


"""

def find_nearest_repetition(paragraph: List[str]) -> int:
    smallest_dist = float('inf')
    ht = {}
    for i, s in enumerate(paragraph):
        if not s in ht:
            ht[s] = i
        else:
            if i - ht[s] < smallest_dist:
                smallest_dist = i - ht[s]
            ht[s] = i
    if smallest_dist == float('inf'): # no repeats
        return -1
    return smallest_dist



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('nearest_repeated_entries.py',
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
