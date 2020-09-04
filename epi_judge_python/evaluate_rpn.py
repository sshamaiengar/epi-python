from test_framework import generic_test
import operator

"""

Brute force:
Base case just number
Otherwise, do recursion
    Get operator from last spot
    Find and evaluate operands (go left to right and fill slots)
    Apply operation
    Return result
O(n) time, O(n) space (in call stack)

Using stacks:
Stack contains operands
When operator hit, combine top 2 operands using it, and replace them on stack with that value
Final value is result
Ex. 3,4,+,2,x,1,+

3
3 4
7
7 2
14
14 1
15

"""

def apply(op: str, stack):
    """
    Pop two operands off stack and evaluate them using the operator.
    Then, add result to stack
    """
    op1 = int(stack.pop())
    op2 = int(stack.pop())
    ops = {
        "+": operator.add,
        "-": operator.sub,
        "/": operator.floordiv,
        "*": operator.mul
    }
    stack.append(ops[op](op2, op1)) # watch the order here
    return stack

def evaluate(expression: str) -> int:
    s = []
    toks = expression.split(",")
    for t in toks:
        try:
            s.append(int(t))
        except:
            s = apply(t, s)
    if s:
        return s[0]
    return 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
