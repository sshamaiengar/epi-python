from typing import List

from test_framework import generic_test

"""

Given stock prices over time range:
Determine max profit possible from buying then selling one share of stock once.

Want to find largest prices[j] - prices[i] such that j > i

Brute force:
Calculate all possible profits from buying then selling at every pair of times i, j (i < j)
-> O(n^2)

Better:
Track current max profit, min price and time i
Go through prices
    Update max profit based on profit with previous min and current value (if > min)
    Update min price and i if current < min
Return max profit
-> O(n)


"""


def buy_and_sell_stock_once(prices: List[float]) -> float:
    max_profit = 0.0
    min_price = float('inf')
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
