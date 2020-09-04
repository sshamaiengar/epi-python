import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

NUM_PEGS = 3

"""

Move n rings from peg 0 to peg 1:
    Move top n-1 rings to peg 2 (recurse)
    Move nth ring to peg 1
    Move top n-1 rings to peg 1 (recurse)

"""

def compute_tower_hanoi(num_rings: int) -> List[List[int]]:
    def move_stack(n, a, b):
        if n == 1:
            return [[a, b]]
        pegs = set(range(NUM_PEGS))
        other_peg = list(pegs - {a,b})[0]
        return move_stack(n-1, a, other_peg) + move_stack(1, a, b) + move_stack(n-1, other_peg, b)
    return move_stack(num_rings, 0, 1)


@enable_executor_hook
def compute_tower_hanoi_wrapper(executor, num_rings):
    pegs = [list(reversed(range(1, num_rings + 1)))
            ] + [[] for _ in range(1, NUM_PEGS)]

    result = executor.run(functools.partial(compute_tower_hanoi, num_rings))

    for from_peg, to_peg in result:
        if pegs[to_peg] and pegs[from_peg][-1] >= pegs[to_peg][-1]:
            raise TestFailure('Illegal move from {} to {}'.format(
                pegs[from_peg][-1], pegs[to_peg][-1]))
        pegs[to_peg].append(pegs[from_peg].pop())
    expected_pegs1 = [[], [], list(reversed(range(1, num_rings + 1)))]
    expected_pegs2 = [[], list(reversed(range(1, num_rings + 1))), []]
    if pegs not in (expected_pegs1, expected_pegs2):
        raise TestFailure('Pegs doesn\'t place in the right configuration')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('hanoi.py', 'hanoi.tsv',
                                       compute_tower_hanoi_wrapper))
