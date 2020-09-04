from test_framework import generic_test
from collections import Counter

"""

Constructible if
    for each char in letter:
        count of char in letter <= count of char in magazine

Brute force:
For each char in letter
    Count occurrences of char in mag, and compare
O(nm)

Hash table:
Get counts of chars in letter (O(n))
Get counts of chars in magazine (O(m))
Compare counts (O(k) for k unique chars), basically O(26) = O(1))
O(n + m)

"""

def is_letter_constructible_from_magazine(letter_text: str,
                                          magazine_text: str) -> bool:
    letter_counts = Counter(letter_text)
    mag_counts = Counter(magazine_text)
    mag_counts.subtract(letter_counts)
    for k, v in mag_counts.items():
        if v < 0: # higher count in letter
            return False
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_anonymous_letter_constructible.py',
            'is_anonymous_letter_constructible.tsv',
            is_letter_constructible_from_magazine))
