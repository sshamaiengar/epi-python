from typing import List, Set

from test_framework import generic_test, test_utils

"""

Generate all possible permutations of sequence of distinct ints
No duplicates in the result

Brute force:
Build lists recursively by adding on each in each possible position, starting from slot 0.

Ex. 1,2,3
1
2
3
->
1 2
1 3
2 1
2 3
3 1
3 2
->
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1

n! permutations, and O(n) to make each one
O(n * n!) time

Could cache repeated sub results, but no savings on time complexity (?)

"""

def permutations(A: List[int]) -> List[List[int]]:
    perms = []
    def perm_builder(lst: List[int], other_vals: Set[int]):
        nonlocal perms
        if not other_vals:
            perms.append(lst)
        for v in other_vals:
            perm_builder(lst[:] + [v], other_vals - {v})
    perm_builder([], set(A))
    return perms


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('permutations.py', 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))
