import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

"""

Replace/remove up to <size> entries of the array following rules:
    Replace a with 2 d's
    Remove b
Return size of result
Assume array is big enough
Ignore entries past <size>
Hint: consider multiple passes on s

Ex. [a,b,a,c,...], size 4
-> [d,d,d,d,c]

Ex. [a,d,b,d,c,...] size 5
-> [d,d,d,d,c]

Brute force:
Go through and follow rules, doing inserts and deletes
    **Each insert and delete is O(n) (to shift array)
O(n^2)

Better:
Don't do actual inserts and deletes in input array
Build result array with appends while going through input array (O(n) time and space)
OR
Constant space?

Book solution:
Forward pass to delete (ignore) b's
    Use two pointers, one for reading and one for writing changed string
    Copy each character except b's
Backward pass to turn a into double d's
    First count number of a's to get final string length (size - number of b's + number of a's)
    Start with read pointer at the end of the substring, and write pointer at the end of computed length string
    For each a, write in 2 d's
    Write pointer won't get ahead of read pointer


"""


def replace_and_remove(size: int, s: List[str]) -> int:
    # print(s[:size])
    # forward pass: remove b's
    w = 0
    for r in range(size):
        c = s[r]
        if c != "b":
            s[w] = c
            w += 1
        else:
            size -= 1
    
    # print(s[:size])

    # backward passes: count a's and build with replacement from back
    a_count = 0
    for i in range(size):
        if s[i] == 'a':
            a_count += 1

    w = size + a_count - 1
    for r in range(size - 1, -1, -1):
        c = s[r]
        if c == "a":
            s[w] = 'd'
            s[w-1] = 'd'
            w -= 2
        else:
            s[w] = c
            w -= 1

    # print(s[:size + a_count])

    return size + a_count


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
