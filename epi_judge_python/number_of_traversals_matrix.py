from test_framework import generic_test

"""

count ways to traverse mxn grid from top left to bottom right
Only moving down and right

Brute force:
generate all paths in grid from top left
Count those that end at bottom right
O(??)

DP:
# of ways to get to (i,j) = sum of #s of ways to get to (i-1, j) and (i, j-1)
Fill out DP array in row-major order using this.
O(mn) time and space

Also:
Use combinatorial formula of Pascal's triangle
O(1)

"""


def number_of_ways(n: int, m: int) -> int:
    # analytical O(1) solution
    # from math import factorial
    # return factorial(n+m-2)/factorial(n-1)/factorial(m-1)

    # DP solution
    dp = [[0 for i in range(m)] for j in range(n)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(m):
            if j > 0:
                dp[i][j] += dp[i][j-1]
            if i > 0:
                dp[i][j] += dp[i-1][j]
    return dp[-1][-1]

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_traversals_matrix.py',
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways))
