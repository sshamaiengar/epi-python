import functools
from typing import List
import random

from test_framework import generic_test
from test_framework.random_sequence_checker import (
    binomial_coefficient, check_sequence_is_uniformly_random,
    compute_combination_idx, run_func_with_retries)
from test_framework.test_utils import enable_executor_hook

"""

Return random sample of size k of input list A.
A contains distinct elements.

All outputs should be equally likely (uniform randomness).
Return result in the input array itself.

Solution:
Pick k unique values in the array, making sure not to pick duplicates.

For each value:
    pick random index (excluding sample being formed at the beginning of array)
    Swap value at that index with a value near the front of the array
O(k) time, O(1) space

"""


def random_sampling(k: int, A: List[int]) -> None:
    for i in range(k):
        rng = len(A) - i
        j = random.randint(0, rng-1)
        A[i], A[i+j] = A[i+j], A[i]
    A = A[:k]


@enable_executor_hook
def random_sampling_wrapper(executor, k, A):
    def random_sampling_runner(executor, k, A):
        result = []

        def populate_random_sampling_result():
            for _ in range(100000):
                random_sampling(k, A)
                result.append(A[:k])

        executor.run(populate_random_sampling_result)

        total_possible_outcomes = binomial_coefficient(len(A), k)
        A = sorted(A)
        comb_to_idx = {
            tuple(compute_combination_idx(A, len(A), k, i)): i
            for i in range(binomial_coefficient(len(A), k))
        }

        return check_sequence_is_uniformly_random(
            [comb_to_idx[tuple(sorted(a))] for a in result],
            total_possible_outcomes, 0.01)

    run_func_with_retries(
        functools.partial(random_sampling_runner, executor, k, A))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('offline_sampling.py',
                                       'offline_sampling.tsv',
                                       random_sampling_wrapper))
