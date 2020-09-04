from typing import List

from test_framework import generic_test

"""

Merge two sorted arrays in place in the first array (assume it has enough empty entries)

Brute force:
Create new result array from normal merge technique
Time O(m+n), space O(m+n) (doesn't use space already in first array)
OR
Create full array, then resort
O((m + n) log (m+n))

Hint: avoid repeatedly moving entries
E.g. shifting several entries to put another one in the right spot

Build new array starting at the end of the first array (in empty spots), then reverse

Ex. 3,13,17,_,_,_,_,_ & 3,7,11,19
_,13,17,_,_,_,_,3   3,7,11,19
_,13,17,_,_,_,3,3   _,7,11,19
_,13,17,_,_,7,3,3   _,_,11,19
_,13,17,_,11,7,3,3  _,_,_,19
_,_,17,13,11,7,3,3  _,_,_,19
"                           "
_,19,17,13,11,7,3,3 _,_,_,_

Will sorted entries in first array be cleared fast enough to be replaced?
Ex. 1,2,3,4,_,_ & 5
_,2,3,4,_,1   5
_,_,3,4,2,1   5
_,_,?,?,2,1   5

OR just build from the end of the first array, but go in reverse over the sorted values
Will never overwrite value in first array before it is processed.
    Because even if go through all values in second array first, the next value to process will be the one in the first array


"""

def merge_two_sorted_arrays(A: List[int], m: int, B: List[int],
                            n: int) -> None:
    ins = m + n-1
    a = m - 1
    b = n - 1

    while a >= 0 and b >= 0:
        if A[a] > B[b]:
            nxt = A[a]
            a -= 1
        else:
            nxt = B[b]
            b -= 1
        A[ins] = nxt
        ins -= 1
    if a < 0:
        # finish with B
        while b >= 0:
            nxt = B[b]
            A[ins] = nxt
            ins -= 1
            b -= 1
    elif b < 0:
        # finish with A
        while a >= 0:
            nxt = A[a]
            A[ins] = nxt
            ins -= 1
            a -= 1

def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('two_sorted_arrays_merge.py',
                                       'two_sorted_arrays_merge.tsv',
                                       merge_two_sorted_arrays_wrapper))
