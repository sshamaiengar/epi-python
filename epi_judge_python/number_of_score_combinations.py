from typing import List

from test_framework import generic_test

"""

(Coin change problem)
Number of ways to get a final score given the possible scores for each play
Ex. score 12, plays [2,3,7)
6 * 2
4 * 3
2 * 3 + 3 * 2
7 + 3 + 2
--> 4 ways

Dynamic programming:
Number of ways to get X with values 0-i...................two options
    = number of ways to get X with values 0 - (i-1).......exclude coin i
    + number of ways to get X-(value i) with values 0-i...include coin i

Base case:
Assume 0 is a potential value
Can get score 0 one way (??could be infinite uses of 0 value)

  0 1 2 3 4 5 6 7 8 9 10 11 12
0 1 0 0 0 0 0 0 0 0 0 0  0  0
2 1 0 1 0 1 0 1 0 1 0 1  0  1
3 1 0 1 1 1 1 2 1 2 2 2  2  3
7 1 0 1 1 1 1 2 1 2 2 3  2  4

"""


def num_combinations_for_final_score(final_score: int,
                                     individual_play_scores: List[int]) -> int:
    R = len(individual_play_scores) + 1
    C = final_score + 1
    dp = [[0 for i in range(C)] for j in range(R)]
    
    dp[0][0] = 1 # base case

    for i in range(1,R):
        for j in range(C):
            value = individual_play_scores[i-1]
            options_including_value = dp[i][j - value] if j - value >= 0 else 0
            options_excluding_value = dp[i-1][j]
            dp[i][j] = options_including_value + options_excluding_value
    return dp[-1][-1]




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_score_combinations.py',
                                       'number_of_score_combinations.tsv',
                                       num_combinations_for_final_score))
