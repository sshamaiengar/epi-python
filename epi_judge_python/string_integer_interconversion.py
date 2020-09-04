from test_framework import generic_test
from test_framework.test_failure import TestFailure

"""

String to int:
Do one digit at a time.
Start from front, save the sign if necessary.
Shift current total (*= 10), then add next digit.
Apply sign.

Int to string:
Keep list for string chars
Get sign
Do digit popping until int is 0
    Add each digit as string to list
Convert list to string all at once (better than repeatedly creating new strings)

"""

def int_to_string(x: int) -> str:
    s = []
    if x < 0:
        sign = "-"
        x = abs(x)
    else:
        sign = ""

    vals = {
        0: "0",
        1: "1",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9"
    }
    while x >= 0:
        d = x % 10

        # should be able to do this in O(1) if implementation is LL
        # if it's O(n) to shift list, then could just build list backwards, then reverse final str
        s.append(vals[d])
        x //= 10
        if x == 0:
            break
    s.append(sign)
    return "".join(reversed(s))


def string_to_int(s: str) -> int:
    t = 0
    sign = 1
    i = 0
    if s[0] == "-":
        sign = -1
        i = 1
    elif s[0] == "+":
        i = 1

    vals = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9
    }
    while i < len(s):
        d = s[i]
        t *= 10
        t += vals[d]
        i += 1

    return t * sign


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':

    print(int_to_string(-4176473))
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
