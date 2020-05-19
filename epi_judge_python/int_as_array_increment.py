from typing import List

from test_framework import generic_test

"""

Brute force:
Turn array into int, add 1, then turn back into list
O(n) for n digits (but multiple passes)
O(1) space?

Better:
Manual add and carry
While a digit is greater than 9, mod and add remainder to previous digit
If an extra digit needs to be added (e.g. 99), need to shift whole list
    (but this is necessary no matter what)
Time: O(n)
Space: O(1)


Ex.
129
1 2 9
1 2 10
1 3 0

99
9 9
9 10
10 0
1 0 0


"""

def plus_one(A: List[int]) -> List[int]:
    carry = 1
    i = -1

    while i >= -1 * len(A):
        A[i] += carry
        carry = A[i] // 10
        A[i] %= 10
        i -= 1
    if carry == 1:
        A.insert(0, carry)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
