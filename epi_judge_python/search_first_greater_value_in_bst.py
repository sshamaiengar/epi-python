from typing import Optional

from bst_node import BstNode
from test_framework import generic_test

"""

Find next key greater than a given key in a BST.
I.e. next value in an inorder traversal

Brute force:
Do the inorder traversal, get the next key.
Time O(n), space O(n)?

Better:
Find node with given key
If node has a right child, the result is the leftmost child of the right subtree
If node has no right child, the result is the parent of node
Traverse from root to node and keep nodes in path
Traverse right subtree or get parent as necessary
Time O(log n) (height), space O(1)

What about duplicate value keys?
Need to find rightmost node with given value

ISSUE: value may not actually be in the tree

---------------

Solution:

Use the idea of binary search. Tree node identifies the midpoint of a search interval.
Store best candidate for result and update it while descending.
    Eliminate subtrees by comparing with target value.
    Candidate is right subtree if root <= target
                 left subtree if root > target
    

"""


def find_first_greater_than_k(tree: BstNode, k: int) -> Optional[BstNode]:
    first_greater = None
    curr = tree

    while curr:
        if curr.data > k:
            # curr is a candidate for the result
            first_greater = curr

            # go down left subtree to get better candidates (closer to k while > k)
            curr = curr.left
        else:
            # root and all values in the left subtree are <= k, so they aren't better candidates
            # go to right subtree for better candidates (something >= k0
            curr = curr.right

        
    return first_greater


def find_first_greater_than_k_wrapper(tree, k):
    result = find_first_greater_than_k(tree, k)
    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'search_first_greater_value_in_bst.py',
            'search_first_greater_value_in_bst.tsv',
            find_first_greater_than_k_wrapper))
