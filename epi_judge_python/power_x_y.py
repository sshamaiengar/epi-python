from test_framework import generic_test

"""

Brute force: O(y) 
x * x * ... * x (y times)

Faster:
x^1 = x
x^2 = x ** 2
x^3 = (x ** 2) * x
x^4 = (x ** 2) ** 2
x^5 = ((x ** 2) ** 2) * x

Go through binary representation of y: (Y1Y2Y3...)_2
Use shifting and masking to check each bit Yi.
If Yi set, multiply result by x^(2^i) (based on product rule of exponents)
O(log y), OR O(n) (n bits in representation of y)

"""
#
def power(x: float, y: int) -> float:

    """
    Recursive version runs into stack overflow:

    if y < 0:
        return 1.0/power(x, y)
    elif y == 0:
        return 1
    elif y % 2 == 1:
        return x * power(x, y - 1)

    return power(x, y/2) ** 2
    """

    if y < 0:
        return 1.0/power(x, -y)

    p = 1
    i = 0
    while y >> i > 0:
        if (y >> i) & 1 == 1:
            p *= x ** (2 ** i)
        i += 1
        
    return p

if __name__ == '__main__':
    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv',
                                        power))
