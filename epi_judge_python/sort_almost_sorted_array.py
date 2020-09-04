from typing import Iterator, List
from heapq import *

from test_framework import generic_test

"""

Sort almost sorted array (each number is at most k away from its sorted position).
Hint: how many nums must you read after reading the ith number to be sure you can place it in the correct position?

Ex. [3,-1,2,6,4,5,8], k=2
 -> [-1,2,3,4,5,6,8]

Brute force:
Resort the whole thing
O(n log n), or O(n) for an adaptive sort?

Heap idea:
Keep a sliding window of values in a heap.
How many values?
    Enough to be able to determine correct position.
    When at position i, the correct value could be as far as k away (i-k to i+k)
    Build heap with k values, and maintain by inserting (i+k)th value each time a value is popped.
    Eventually will shrink when all values popped.

O(n log k) time, O(n) space
Ex. 3,-1,2,6,4,5,8], k=2
 -> [-1,2,3,4,5,6,8]

i       heap        output
0       -1,3,2      -1
1       2,3,6       2
2       3,6,4       3
3       4,6,5       4
4       5,6,8       5
5       6,8         6
6       8           8

"""

def sort_approximately_sorted_array(sequence: Iterator[int],
                                    k: int) -> List[int]:

    lst = []
    hp = []
    size = k + 1
    for i in range(k + 1):
        try:
            heappush(hp, next(sequence))
        except StopIteration:
            pass
    while hp:
        val = heappop(hp)
        lst.append(val)
        try:
            heappush(hp, next(sequence))
        except StopIteration:
            pass
    return lst


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'sort_almost_sorted_array.py', 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
