from test_framework import generic_test

"""

Ex.
10010101 => 10101001

Brute force: O(n)
Shift each bit off and Shift it onto a new word
OR swap each of least significant half of bits with most significant bits


O(n/L)
Lookup table? Store reversed versions of subwords. Lookup and combine


"""

def reverse_16(x):
    res = 0
    
    for i in range(16):
        bit = x & 1
        res <<= 1
        res |= bit
        x >>= 1
    return res

# build lookup table of reversed 16-bit words
revs = []
for i in range(2**16):
    revs.append(reverse_16(i))

def reverse_bits(x: int) -> int:
    mask = 0xffff
    mask_size = 16
    res = 0
    for i in range(4):
        subword = x & mask
        x >>= mask_size
        rev = revs[subword]
        res <<= mask_size
        res |= rev
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
