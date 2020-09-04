from test_framework import generic_test

"""

Compute largest i such that i^2 <= k.

Ex. 16 -> 4
    300 -> 17

Brute force:
Loop over integers 1...k until answer is found...O(sqrt(k))

Cheating?:
Return floor(sqrt(k))

Search:
Do binary search starting with range 1...k and testing the mid.
Lots of values satisfy the inequality, but need to find the largest.
    Constrain search range to the right of a match.
O(log k) < O(sqrt(k))

Watch out for search ranges.
Ex. k = 1
Have to be able to consider 1 as mid, so use k + 1


"""

def square_root(k: int) -> int:
    lo, hi = 0, k
    mid = (lo + hi) // 2
    while lo <= hi:
        mid = (lo + hi) // 2
        if mid ** 2 <= k:
            lo = mid + 1
        else:
            hi = mid - 1
    return lo - 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_square_root.py',
                                       'int_square_root.tsv', square_root))
