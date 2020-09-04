from test_framework import generic_test

"""

Convert string number from first base to second base.
Either base can be from 2 to 16 (use hex chars)

Brute force:
    Convert string to number in first base.
    Convert to base 10.
    Convert to second base, and return string.
        Divide by N method?
        Ex. 74 in base 6
        74 / 6 == 12 R 2 -> 2
        12 / 6 == 2 R 0 -> 0
        2 / 6 == 0 R 2 -> 2
        0 / 6 == 0 R 0
-> O(n) or O(log n)?



"""

hex_vals = {
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15
}

hex_vals2 = {val: key for key, val in hex_vals.items()}

def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    def s2d(d: str) -> int:
        try:
            return int(d)
        except:
            return hex_vals[d]

    def d2s(d: str) -> str:
        if d in hex_vals2:
            return hex_vals2[d]
        return str(d)

    def to_base10(num: str, b: int) -> int:
        s = 0
        p = 0
        # get base 10 value
        for d in num_as_string[::-1]:
            if d == "-":
                s *= -1
            else:
                s += s2d(d) * b ** p
                p += 1
        return s

    def from_base10(num: int, b: int) -> str:
        res = []
        # divide by b method
        negative = num < 0
        num = abs(num)
        while num > 0 or not res:
            q = num // b
            r = num % b
            num = q
            res.append(r)
        return ("-" if negative else "") + "".join(list(map(d2s, res)))[::-1]
    
    if b1 == b2:
        return num_as_string

    return from_base10(to_base10(num_as_string, b1), b2)


if __name__ == '__main__':
    print(convert_base("-7345", 10, 7))
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
