from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

"""

Recurse on each subtree. Calculate height (0 for None, 1 for node). Check balance. Propagate heights up the tree to check for root.

Don't need to store all heights the whole time. Only need to know heights for children of current node

"""


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    def get_height(node: BinaryTreeNode) -> int:
        if not node:
            return 0
        lheight, rheight = get_height(node.left), get_height(node.right)
        if abs(lheight-rheight) > 1:
            return -float('inf') # use -inf to indicate imbalance
        return 1 + max(lheight, rheight)

    return get_height(tree) > -float('inf')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
