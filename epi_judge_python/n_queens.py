from typing import List

from test_framework import generic_test

"""

Find all non-attacking placements of n queens on nxn board

Return format:
[q1, q2, q3, ..., qn]           qi = row containing queen in ith column

Brute force:
Generate all possible placements of n queens, then check which are valid.
Very bad runtime! O(n!), because n^2 C n possible placements

Better:
Know that one queen will be in each row/col
Consider all options for placing first queen (any square in first row/col)
Find all possible options for second queen ( valid squares in second row/col)
Continue for queens up to nth

Build results from all possible options for each queen (like phone keypad to word problem)
Max n^2?

Ex. n = 3

[0,__]:
    [0,2,_]:
        [0,2,1]
[1,__]:
    X
[2,__]:
    [2,0,_]:
        [2,0,1]

"""

def n_queens(n: int) -> List[List[int]]:
    placements = []
    def n_queens_helper(prev: List[int], n_left):
        if n_left == 0:
            placements.append(prev)
        else:
            # can't be in same row as any prev
            remaining = set(range(n))
            remaining -= set(prev)

            # can't be in same diagonal (+- i rows above or below row of queen i cols away)
            for i, r in enumerate(prev):
                diff_cols = len(prev) - i
                remaining -= {r + diff_cols, r - diff_cols}

            for r in remaining:
                n_queens_helper(prev + [r], n_left - 1)

    n_queens_helper([], n)

    return placements


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('n_queens.py', 'n_queens.tsv', n_queens,
                                       comp))
