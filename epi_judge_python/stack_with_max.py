from test_framework import generic_test
from test_framework.test_failure import TestFailure

"""

Use an additional stack to keep track of the max at each level.

Ex. (left is bottom, right is top)

1
-> max = 1

1 2
-> max = 2

1 2 1
-> max = 2

pop(1)
1 2
-> max = 2
    (because 1 was not greater than current max, next max is still 2)

Update max stack with every push and pop. Watch out for empty stacks.

"""



class Stack:
    def __init__(self):
        self.s = []
        self.maxes = []

    def empty(self) -> bool:
        return len(self.s) == 0

    def max(self) -> int:
        if not self.empty():
            return self.maxes[-1]
        return 0

    def pop(self) -> int:
        if not self.empty():
            self.maxes.pop()
            v = self.s.pop()
            return v
        return 0

    def push(self, x: int) -> None:
        if self.empty():
            self.s.append(x)
            self.maxes.append(x)
        else:
            curr_max = self.max()
            if x >= curr_max:
                new_max = x
            else:
                new_max = curr_max
            self.s.append(x)
            self.maxes.append(new_max)
        return


def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == 'Stack':
                s = Stack()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure('Pop: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure('Max: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure('Empty: expected ' + str(arg) +
                                      ', got ' + str(result))
            else:
                raise RuntimeError('Unsupported stack operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('stack_with_max.py',
                                       'stack_with_max.tsv', stack_tester))
