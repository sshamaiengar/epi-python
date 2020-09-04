from typing import List

from bst_node import BstNode
from test_framework import generic_test, test_utils

"""

Return k largest values in binary search tree.

Brute force:
Do inorder traversal to get sorted list. Return k largest
O(n)

Better:
Don't care about the smaller values in the tree
Only do part of the traversal?
    But need to know how many values are under each subtree
        Requires O(n) counting
    Start traversal on right side, and only count as much as is needed to get to k
    Store list of parents down to largest value -> O(h) space ~ O(log n)
    Get largest value, then go back up the parents and to the left as necessary to get more values

Ex. 
                                        108
                108                                             285
    -10                108                                243         285
-14     2                                                                   401

k = 4

Go to 401
    parents [108, 285, 285]
    count = 1
Go to 285
    parents = [108, 285]
    count = 2
    No left child
Go to other 285
    parents = [108]
    count = 3
    Has left child
Go to 243
    parents = [108, 285]
    count = 4

Time O(k + h)
Space O(h)

Recursive:
Take right children plus (j < k) largest in left subtrees as necessary

"""


def find_k_largest_in_bst(tree: BstNode, k: int) -> List[int]:
    def find_largest(tree: BstNode, j: int) -> List[BstNode]:
        if j <= 0:
            return []
        if not tree:
            return []
        
        rights = find_largest(tree.right, j)
        lefts = find_largest(tree.left, j-1-len(rights))
        return lefts + [tree] + rights


    return [t.data for t in find_largest(tree, k)[-k:]][::-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('k_largest_values_in_bst.py',
                                       'k_largest_values_in_bst.tsv',
                                       find_k_largest_in_bst,
                                       test_utils.unordered_compare))
