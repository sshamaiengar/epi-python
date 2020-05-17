from test_framework import generic_test

"""

If negative, not palindromic

Brute force: O(n) for n digits
Convert to string and check if palindrome

Faster:
Could do by building new number and checking equality
O(n) time, O(n) space

Extract least significant digit repeatedly, comparing to most significant digit
How to extract MSD?
238 = 200 + 30 + 8.
2 = floor(log(238)/log(10^2)), but how to get exponent i for 10?
-> i = floor(log10(x))
-> num_digits = i + 1
Iterate over num_digits //2, checking MSD == LSD
MSD = x % 10**i
After each check, remove MSD and LSD using %
O(n) time, O(1) space

"""

def is_palindrome_number(x: int) -> bool:
    xr = 0
    orig_x = x
    while x > 0:
        xr = xr*10 + x % 10
        x //= 10
    return xr == orig_x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_number_palindromic.py',
                                       'is_number_palindromic.tsv',
                                       is_palindrome_number))
