from test_framework import generic_test

"""
Ex.

10011010 => 0
10011000 => 1
01100010 => 1

Brute force: O(n) (n is length of binary word)
Shift each bit off and count number of 1s

For very large number of words, need to do better.
Hint: Use a lookup table, but don't use 2^64 entries

Use OR across halves? But this depends on position of 1s


"""

def parity(x: int) -> int:
    # trick: x & (x-1) clears the lowest set bit in x
    # (0100) & (0011) == 0
    ct = 0
    while x > 0:
        x &= x - 1
        ct += 1
    return ct & 1


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
