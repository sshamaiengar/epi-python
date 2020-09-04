from typing import List
import random

from test_framework import generic_test

"""

Find kth largest value in array
Assume distinct values
Hint: Use divide and conquer, with randomization

Brute force:
Sort and get the value -> O(n log n) time

Build a max-heap of size k, then get min of it -> O(n log k) time
    Does more than required, because it gets the k largest values in order

Quick select? Similar to the partition algo for quicksort
Pick random pivot
Use partition algo around the pivot (should place pivot in correct sorted position)
If pivot ends up in kth largest position (length - k), then return it
Else, recurse on one side of this pivot
    If pivot position is too low, recurse on right
                         too high, recurse on left
O(n) time, O(1) space if partitioning in place
    O(n) because recurrence is T(n) = O(n) + T(n/2) = O(n) + O(n/2) + ... ~= O(2n)

What about the partitioning into size k subarrays (with ocnstant time sort), then doign stuff with that?



"""

# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
def find_kth_largest(k: int, A: List[int]) -> int:
    def partition(left, right, pivot_i):
        pivot = A[pivot_i]
        new_pivot_i = left
        A[pivot_i], A[right] = A[right], A[pivot_i]
        for i in range(left, right):
            if A[i] > pivot:
                A[i], A[new_pivot_i] = A[new_pivot_i], A[i]
                new_pivot_i += 1
        A[new_pivot_i], A[right] = A[right], A[new_pivot_i]
        return new_pivot_i

    left, right = 0, len(A) - 1
    while left <= right:
        pi = random.randint(left, right)
        new_pi = partition(left, right, pi)
        if new_pi == k-1:
            return A[new_pi]
        elif new_pi > k-1:
            right = new_pi - 1
        else:
            left = new_pi + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('kth_largest_in_array.py',
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))
