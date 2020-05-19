from typing import List

from test_framework import generic_test

"""

Brute force: convert to ints, multiply, convert back to lists
Problem of overflow

Better:
Use hand multiplication algorithm with multiplying, carrying, and adding

"""

def multiply(num1: List[int], num2: List[int]) -> List[int]:
    carry = 0
    result = [0] * (len(num1) + len(num2))
    sign = -1 if (num1[0] < 0) ^ (num2[0] < 0) else 1
    for i in range(-1, -1*len(num1) - 1, -1):
        carry = 0
        for j in range(-1, -1*len(num2) - 1, -1):
            prod = abs(num1[i]) * abs(num2[j]) + carry
            power1 = abs(i) - 1
            power2 = abs(j) - 1
            place = -1 - power1 - power2
            # print(num1[i], "*", num2[j], "+", carry, "=", prod, "->", -1-power1-power2)
            result[place] += prod
            carry = result[place] // 10
            result[place] %= 10

            # print(result)

        if carry > 0:
            last_place =  -abs(i) -len(num2)
            result[last_place] = carry

    # remove extra 0s
    i = 0
    while result[i] == 0 and i < len(result) - 1:
        i += 1

    return [sign * result[i]] + result[i+1:]


if __name__ == '__main__':
    # print(multiply([1,2,3], [9,8,7]))

    exit(
        generic_test.generic_test_main('int_as_array_multiply.py',
                                       'int_as_array_multiply.tsv', multiply))
