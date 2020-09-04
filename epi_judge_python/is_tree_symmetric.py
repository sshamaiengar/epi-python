from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

"""

Is binary tree symmetric?

Ex.     2
    3       3

NOT symmetric (only structurally symmetric, but needs matching keys):
    2
4       3

Hint: definition of symmetry is recursive

Given root, need to check that right and left are same value
    BUT right and left subtrees do not need to be symmetric themselves
    Ex.     2
        3       3
          4   4

Left-side values of right subtree must equal right-side values of left subtree (at each level)



"""

def is_symmetric(tree: BinaryTreeNode) -> bool:
    def symmetry_helper(a: BinaryTreeNode, b: BinaryTreeNode) -> bool:
        if not a or not b:
            return not a and not b
        return a.data == b.data\
            and symmetry_helper(a.left, b.right)\
            and symmetry_helper(a.right, b.left)
    return not tree or symmetry_helper(tree.left, tree.right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
