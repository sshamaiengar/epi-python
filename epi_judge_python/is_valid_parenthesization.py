from test_framework import generic_test

"""

Test if string of {}[]() is well-formed, i.e. each character matches with its closing char in the right order.

Ex. {(}) -> NO
    [{}]([]) -> YES

Use a stack
Add each opening character to the stack
Closing characters must match whats on the top of the stack
Stack must be empty after processing all chars
"""

def is_well_formed(s: str) -> bool:
    stack = []
    match = {
        "{": "}",
        "(": ")",
        "[": "]"
    }
    for c in s:
        if c in match:
            stack.append(c)
        else:
            if len(stack) > 0 and c == match[stack[-1]]:
                stack.pop()
            else:
                return False
    return not stack


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_parenthesization.py',
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
