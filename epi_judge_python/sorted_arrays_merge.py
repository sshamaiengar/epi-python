from typing import List

from test_framework import generic_test
from heapq import *

"""

Merge n sorted arrays.
When merging just 2, picking the next element to merge is just one comparison. When merging n arrays, that would take O(n) comparisons.
Could track a min-heap of size n to constantly have the min element. O(2 log n) at each step, to push next value from a list, and pop the min. This is better than O(n).

O(nk * log n), where k is max length of any array.
Better than O(n^2 k)

Don't remove from the lists, takes O(k) time. Just use indices.

"""

def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    r = []
    pos = [0] * len(sorted_arrays)

    hp = []
    for i, l in enumerate(sorted_arrays):
        if l:
            heappush(hp, (l[0], i)) # track the value, and its parent list index
            pos[i] += 1

    while hp:
        min_val, i = heappop(hp)
        r.append(min_val)
        if pos[i] < len(sorted_arrays[i]):
            heappush(hp, (sorted_arrays[i][pos[i]], i))
            pos[i] += 1

    return r


if __name__ == '__main__':
    print(merge_sorted_arrays([[-1, 0], [-2]]))

    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
