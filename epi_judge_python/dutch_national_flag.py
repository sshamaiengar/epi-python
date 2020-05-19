import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)

"""

Normal quicksort partition:
    Iterate over j = 0 to end (of sublist)
    Track i = highest index of elements <= pivot (starts as -1)
    For each elem j <= pivot, i++ and swap(a[i], a[j])
        Moves each smaller elem onto the right side
    For each elem j > pivot, do nothing
        when i is increased, it will move to swap a small elem with this bigger elem
Result is all elements <= pivot to the left, > to the right

DNF partitioning:
Result is all elements < pivot first (leftmost), then all elements == pivot, then all elements > pivot (rightmost)

Normal: (j=0, i=-1) (pivot = 0)
0 1 2 (0) 2 1 1 (j=1, i=0)
0 1 2 0 2 1 1 (j=2, i=0)
0 0 2 1 2 1 1 (j=3, i=1)

(pivot = 1, j=0, i=-1)
0 1 2 0 2 1 1 (j=0, i=0)
0 1 2 0 2 1 1 (j=1, i=1)
0 1 2 0 2 1 1 (j=2, i=1)
0 1 0 2 2 1 1 (j=3, i=2)
0 1 0 2 2 1 1 (j=4, i=2)
0 1 0 1 2 2 1 (j=5, i=3)
0 1 0 1 1 2 2 (j=6, i=4)

Correct DNF parition would be:
0 0 1 1 1 2 2

Brute force:
3 lists: elems >, =, and < pivot
Iterate through array and place elems in each list
Join lists for result
O(n) time, O(n) space

Better:
Do normal paritioning, then repeat on result with pivot = (previous pivot) - 1
Ex. pivot = 0(see above)
0 1 0 1 1 2 2 (j=0, i=-1)
0 1 0 1 1 2 2 (j=0, i=0)
0 1 0 1 1 2 2 (j=1, i=0)
0 0 1 1 1 2 2 (j=2, i=1)
...(all elems j >= 3 are greater than 0, do nothing)
0 0 1 1 1 2 2
Time: O(n) (one extra pass)
Space: O(1) (use same array)

Alternative:
Do normal partition step but only i++ and swap when elem j < pivot
Then, do reverse of this starting from end of array
    i = leftmost index of elems greater than pivot
    j = end to 0
    If elem j > pivot, i -= 1 and swap
Time: O(n)
Space: O(1)


"""

def normal_partition(pivot_val, a):
    # print()
    # print("start: ", pivot_val, a)
    p = pivot_val
    i = -1
    for j, v in enumerate(a):
        if a[j] <= p:
            i += 1
            a[j], a[i] = a[i], a[j]
    # print("partition: ", a)
    return a


def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    pivot_val = A[pivot_index]
    A = normal_partition(pivot_val, A)
    return normal_partition(pivot_val - 1, A)


@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure('Some elements are missing from original array')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('dutch_national_flag.py',
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
