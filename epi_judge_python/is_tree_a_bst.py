from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

"""

Check if binary tree is BST.
For node root, all node in left subtree are < root key
    and all nodes in right subtree are >= root key

**Not enough to check left and right children for each node
Ex. 3
   / \
  2   5
     /
   (1)

Need to also track a range to compare at each node, that is updated based on that node.

"""

def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    def check_node(node, lo=-float('inf'), hi=float('inf')):
        if not node:
            return True
        return lo <= node.data <= hi\
                and check_node(node.left, lo, node.data)\
                and check_node(node.right, node.data, hi)
    return check_node(tree)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
