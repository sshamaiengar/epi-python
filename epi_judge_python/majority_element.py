from typing import Iterator

from test_framework import generic_test

"""

Find majority element of input sequence with one pass
Hint: Use the existence of a majority element to eliminate options

Brute force:
Put everything into Counter
Return element with majority count
O(n) time and space

O(1) space?
Greedy?
Track a candidate and its count
First character is candidate, count 1
Candidate must be majority element (if present) at every step
If candidate count <= n/2 then reset candidate



"""


def majority_search(stream: Iterator[str]) -> str:
    cnd_cnt = 0
    for it in stream:
        if cnd_cnt == 0:
            cnd, cnd_cnt = it, cnd_cnt + 1
        elif cnd == it:
            cnd_cnt += 1
        else:
            cnd_cnt -= 1
    return cnd


def majority_search_wrapper(stream):
    return majority_search(iter(stream))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('majority_element.py',
                                       'majority_element.tsv',
                                       majority_search_wrapper))
