from test_framework import generic_test
from test_framework.test_failure import TestFailure

"""

Implement LRU cache

Cache eviction:
When inserting, if cache size passes capacity, then evict something
LRU = evict least recently used thing

Need to be able to track this along with the key-value pairs of the cache
Space O(n) no matter what

Brute force:
Track time stamp for last use of each pair.
When evicting, find oldest pair (O(n)) and remove.
Insert O(n) when evicting, O(1) else

Could use min-heap for time stamps
Insert O(log n) when evicting

Want to be able to maintain sorted order but be able to remove any position in O(1)
Doubly linked list containing timestamps and keys
Add to head to mark newest pair.
Remove from tail to evict oldest pair.
Have hash table point to entries in the list.
Removing any other entry is just finding the entry and rearranging neighbor pointers
Insert O(1) when evicting

"""

class ListNode:
    def __init__(self, value=None):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.dummy_head = ListNode()
        self.dummy_tail = ListNode()
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head
        self.len = 0
    
    def insert_head(self, value):
        self.len += 1
        node = ListNode(value)
        if self.dummy_head.next.value is None:
            node.next = self.dummy_tail
            self.dummy_tail.prev = node
        else:
            node.next = self.dummy_head.next
            node.next.prev = node
        self.dummy_head.next = node
        node.prev = self.dummy_head
        return node
    
    def pop_tail(self):
        if self.dummy_tail.prev is not None:
            self.len -= 1
            node = self.dummy_tail.prev
            before_last = node.prev
            before_last.next = self.dummy_tail
            self.dummy_tail.prev = before_last
            return node.value
        else:
            return None
    
    def remove_node(self, node):
        self.len -= 1
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
        return node.value
    
    def __str__(self):
        s = ""
        curr = self.dummy_head.next
        s += "<-"
        while curr != self.dummy_tail:
            s += str(curr.value)
            s += "-"
            curr = curr.next
        s += "<"
        return s


class LruCache:
    def __init__(self, capacity: int) -> None:
        self.dll = DoublyLinkedList()
        self.nodes = {}
        self.cap = capacity
        return

    def lookup(self, isbn: int) -> int:
        # print(self.dll)
        if isbn in self.nodes:
            # update to most recently used
            node  = self.nodes[isbn]
            _, price = node.value
            self.dll.remove_node(node)
            self.nodes[isbn] = self.dll.insert_head((isbn, price))
            return price
        return -1

    def insert(self, isbn: int, price: int) -> None:
        # print(self.dll)
        if isbn in self.nodes:
            node = self.nodes[isbn]
            _, price = node.value
            self.dll.remove_node(node)

        node = self.dll.insert_head((isbn, price))
        self.nodes[isbn] = node

        # evict if over cap
        if self.dll.len > self.cap:

            # pop tail and clear node from hash table
            isbn, price = self.dll.pop_tail()
            del self.nodes[isbn]


    def erase(self, isbn: int) -> bool:
        # print(self.dll)
        if isbn in self.nodes:
            node = self.nodes[isbn]
            self.dll.remove_node(node)
            del self.nodes[isbn]
            return True
        return False


def lru_cache_tester(commands):
    if len(commands) < 1 or commands[0][0] != 'LruCache':
        raise RuntimeError('Expected LruCache as first command')

    cache = LruCache(commands[0][1])

    for cmd in commands[1:]:
        if cmd[0] == 'lookup':
            result = cache.lookup(cmd[1])
            if result != cmd[2]:
                raise TestFailure('Lookup: expected ' + str(cmd[2]) +
                                  ', got ' + str(result))
        elif cmd[0] == 'insert':
            cache.insert(cmd[1], cmd[2])
        elif cmd[0] == 'erase':
            result = 1 if cache.erase(cmd[1]) else 0
            if result != cmd[2]:
                raise TestFailure('Erase: expected ' + str(cmd[2]) + ', got ' +
                                  str(result))
        else:
            raise RuntimeError('Unexpected command ' + cmd[0])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lru_cache.py', 'lru_cache.tsv',
                                       lru_cache_tester))
