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

Other solutions:

Lookup table:
For computing parity of many 64-bit words, can't precompute all results (2^64)
BUT can precompute all parities for smaller subwords (4 16-bit subwords)
2^16 is only 65536
Precompute all and then go through subwords of each x, looking up parity and accumulating using XOR.

XOR divide-and-conquer:
Parity of x is parity of XOR of two halves of x
Repeat down to last two bits and return result
Time: O(log n)

"""

def parity(x: int) -> int:
    # trick: x & (x-1) clears the lowest set bit in x
    # (0100) & (0011) == 0
    # Time: O(k)
    ct = 0
    while x > 0:
        x &= x - 1
        ct += 1
    return ct & 1


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
