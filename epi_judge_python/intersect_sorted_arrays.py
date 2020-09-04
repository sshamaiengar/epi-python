from typing import List
import bisect

from test_framework import generic_test

"""

Brute force:
Go through shorter list (O(n))
    Check for each character present in longer list (O(m))
O(nm)

...doesn't take advantage of sorting

Faster:
    Use binary search to search longer list
O(n log m)
Best if m >> n

Alternative:
Build sets and intersect them.
O(n + m)
Better if n ~= m

How to avoid duplicates?
Use set
...But need final answer sorted.
Sort in O(n) time, doesn't affect final complexity.

"""

def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
    shorter, longer = (A, B) if len(A) < len(B) else (B, A)
    res = []
    last_x = None # track last x to avoid duplicates in result
    for x in shorter:
        if x == last_x:
            continue
        i = bisect.bisect_left(longer, x) # roughly binary search
        if i < len(longer) and longer[i] == x:
            res.append(x)
            last_x = x
    return list(res)



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intersect_sorted_arrays.py',
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
