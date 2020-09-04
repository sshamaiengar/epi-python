from typing import Optional

from list_node import ListNode
from test_framework import generic_test

"""

Reverse sublist from node start to node finish, inclusive.
Ex. 11 -> 3 -> 5 -> 7 -> 2, reverse from 2 to 4
... 11 -> 7 -> 5 -> 3 -> 2

Brute force:
Extract sublist as separate list.
Reverse the sublist.
Replace sublist in original list.
-> O(n) time and space

Normal in-place reverse method:
    while curr != None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

Need to reverse connections in sublist, then connect start and finish node to the opposite adjacent nodes.
I.e. connect original start to node after original finish
    & connect node before original start to original finish
Store pointers to these and handle this after reversing sublist (using condition based on number of node)

Edge cases:
    Sublist is entire list: normal reverse method
    Start is head: use dummy head to connect to original finish
    Tail is finish: connect original start to None

"""

def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:
    if not L or L.next == None:
        return L

    i = 1
    head = L
    before_start : ListNode = None
    after_finish : ListNode = None
    start_node : ListNode = None
    finish_node : ListNode = None

    curr = L
    while i < start:
        if i == start-1:
            before_start = curr
        curr = curr.next
        i += 1

    start_node = curr

    prev = None
    while i <= finish:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
        i += 1

    finish_node = prev
    
    after_finish = curr

    # reconnect sublist to rest of list
    start_node.next = after_finish

    if not before_start:
        return finish_node
    else:
        before_start.next = finish_node
        return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
