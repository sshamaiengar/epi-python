from typing import List

from test_framework import generic_test

"""

given values A=[a0...an], determine IF there is a set of three ai (duplicates allowed)
that sum to t

has_three_sum(A, t) == has_TWO_sum(A, t-a0) OR has_two_sum(A, t-a1) OR ...

Brute force:
Try all triplets -> O(n3)

Improvement:
using optimal 2-sum in O(n), try each ai with the complement two_sum target

Optimal 2-sum can be done:
    using sets and matching complement of target to a value
    by doing two pointer search (starting at ends) on SORTED input
-> O(n2)


Greedy?


"""

def has_three_sum(A: List[int], t: int) -> bool:
    def has_two_sum(A, t) -> bool:
        s = {t - a for a in A}
        return any([a in s for a in A])
    return any(has_two_sum(A, t-a) for a in A)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('three_sum.py', 'three_sum.tsv',
                                       has_three_sum))
