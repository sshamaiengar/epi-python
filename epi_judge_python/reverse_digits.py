from test_framework import generic_test

"""

Brute force: convert to string, reverse, convert back
O(n) for n digits

Faster:
Use / and % to get each digit and add it to new number
Match signs
O(n) for n digits (lower multiple of n)

"""

def reverse(x: int) -> int:
    sign = 1 if x >= 0 else -1

    x = abs(x)
    nx = 0
    while x > 0:
        d = x % 10
        nx = nx * 10 + d
        x //= 10
    return nx * sign

    return 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
