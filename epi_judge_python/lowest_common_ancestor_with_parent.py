import functools
from typing import Optional

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

"""

Compute lowest common ancestor given nodes that have parent pointers

Without parents, can't go back up the tree.
Have to start at root, find both nodes, then compare the paths.

With parent, can go back up the tree.
Build ancestor paths to the root...O(log n) (O(n) if unbalanced)
Iterate through the path nodes to find last match...O(log n) (O(n) if unbalanced)
-> O(log n)

If both nodes are same distance from root, LCA is first corresponding node in path starting from each node.

Worst case is always going all the way to the root, which has to take O(log n) or O(n) unabalanced

"""

def path_to_root(node):
    p = []
    while node != None:
        p.append(node)
        node = node.parent
    return p


def lca(node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    p1 = path_to_root(node0)
    p2 = path_to_root(node1)

    # paths are from nodes to root, so traverse from ends
    i = -1
    while p1[i] == p2[i]:
        i -= 1
        if abs(i) > len(p1) or abs(i) > len(p2):
            break
    
    return p1[i+1]


@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(lca, must_find_node(tree, node0),
                          must_find_node(tree, node1)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lowest_common_ancestor_with_parent.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
