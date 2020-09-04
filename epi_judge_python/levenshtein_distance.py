from test_framework import generic_test

"""

Compute Levenshtein distance:
    Min number of edits (insert, substitute, delete) needed to transform one string to another

Hint: Consider same problem for prefixes of two strings

Ex. Saturday -> Sundays == 4
Saturday
Sturday
Surday
Sunday
Sundays

Brute force:
Do BFS of possible word states with any kind of edit
    High search space with O(26n) insert options, O(26n) substitute options, O(n) delete options at each step

Using hint?

Ex. LD(Saturday, Sunday) == 3
(above minus insert "s" step)

Ex. Catch -> bark

mark sub-answers for prefixes, with grid like for LCS

    b   a   r   k
c   1   2   3   4
a   2   1   2   3
t   3   2   2   3
c   4   3   3   3
h   5   4   4   4

rules:
if same letter, get value from [i-1][j-1]
    because it requires no new edit versus the prefixes not including this same letter
if different, take (min of [i-1][j], [i][j-1]) + 1
    because it is just one insert/substitution away from these prefixes
return [-1][-1]

Ex. plan -> canal

    c   a   n   a   l
p   1   2   3   4   5
l   2   2   3   4  (4)
a   3  (2)  3  (3)  4
n   4   3  (2)  3   4

    _   c   a   n   a   l
_   0   1   2   3   4   5
p   1   1   2   3   4   5
l   2   2   2   3   4  (4)
a   3   3  (2)  3  (3)  4
n   4   4   3  (2)  3   4

rules:
if same letter, dp[i-1][j-1]
if different, min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1



"""

def levenshtein_distance(A: str, B: str) -> int:
    dp = [[0 for i in range(len(B)+1)] for j in range(len(A)+1)]

    for i in range(len(dp)):
        dp[i][0] = i
    for i in range(len(dp[0])):
        dp[0][i] = i

    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            a = A[i-1]
            b = B[j-1]
        
            dist = 0
            if a == b:
                dist = dp[i-1][j-1]
            else:
                dist = min([dp[i-1][j-1], dp[i][j-1], dp[i-1][j]]) + 1

            dp[i][j] = dist
    # print(dp)
    return dp[-1][-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('levenshtein_distance.py',
                                       'levenshtein_distance.tsv',
                                       levenshtein_distance))
