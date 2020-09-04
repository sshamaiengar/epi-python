from typing import Optional

from list_node import ListNode
from test_framework import generic_test

"""

Two pointers at head of each list, and pointer for head of result list.
Build result by picking lower of each list pointer, then moving forward.

"""

def merge_two_sorted_lists(L1: Optional[ListNode],
                           L2: Optional[ListNode]) -> Optional[ListNode]:
    r = ListNode()
    dummy_head = r
    while not (L1 == None and L2 == None):
        if L1 is not None and (L2 is None or L1.data <= L2.data):
            r.next = L1
            L1 = L1.next
        else:
            r.next = L2
            L2 = L2.next
        r = r.next

    return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_lists_merge.py',
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
