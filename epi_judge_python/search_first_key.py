from typing import List

from test_framework import generic_test

"""

Find i of first occurrence of k in list. Normal binary search will find any occurrence of k.

Naive:
    Binary search. Then traverse backwards. But if the entire list is k, this will turn out to O(n).

What about continuing on left side after first find?
We know the first occurrence is either at the first find or left of it.
Given first find at i, look left (from previous left bound to i - 1).
Continue search on this half. Keep finding next occurences and repeating search on smaller part until bounds are same value?
    That's when we have the leftmost value that could be the target

Still O(log n) time because just multiple smaller iterations of binary search.

"""

def search_first_of_k(A: List[int], k: int) -> int:
    l, r = 0, len(A) - 1
    while l <= r:
        m = (l + r) // 2
        # print(l, m, r)
        if A[m] == k: # continue search to the left
            r = m - 1
        elif A[m] < k:
            l = m + 1
        else:
            r = m - 1
    if l < len(A) and A[l] == k:
        return l
    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
