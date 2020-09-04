import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

MPG = 20

"""

Cities arranged on circular road. Given distance between each, and gas available at each

Compute an "ample city", one city where you can start with empty tank there, refuel, then travel to next city and repeat and make it all the way back.

Ex.
    fuel = [50, 20, 5, 30, 25, 10, 10]
    dist = [900, 600, 200, 400, 600, 200, 100]
Ample city is D.

City    Range
        0
D       600
        200
E       700
        100
F       300
        100
G       300
        200
A       1200
        300
B       700
        100
C       200
        0
D

Brute force:
Test starting at each city.
O(n^2)

Consider ranges, and whether they cover the distance?
Then need to find sequence of ranges that do cover

Ex.
        A       B       C       D       E       F       G
fuel    50      20      5       30      25      10      10
dist    900     600     200     400     600     200     100
range   1000    400     100     600     500     200     200
diff    100     -200    -100    200     -100    0       100

must pick sequence of cities such that diff (range - dist)
    stays at or above 0
    first city diff cannot be negative

greedily pick city with highest diff first?
O(n) to calculate diffs & check
O(n) space to track ranges (unless just reusing space from fuel list)

what about when multiple cities have the same highest value? depends on negative values that come in between?
    like max subarray problem?

go through diffs, track a candidate city and remaining gas
    if positive diff, add to remaining
        if negative before adding, restart and set this as candidate
    if negative diff, add to remaining
candidate at the end should be the ample city
"""


# gallons[i] is the amount of gas in city i, and distances[i] is the
# distance city i to the next city.
def find_ample_city(gallons: List[int], distances: List[int]) -> int:
    ranges = [g * MPG for g in gallons]
    diffs = [r - d for r, d in zip(ranges, distances)]
    remaining = 0
    ample_city = -1
    for i, d in enumerate(diffs):
        if d >= 0:
            if remaining <= 0:
                ample_city = i
                remaining = 0

        remaining += d
    return ample_city


@enable_executor_hook
def find_ample_city_wrapper(executor, gallons, distances):
    result = executor.run(
        functools.partial(find_ample_city, gallons, distances))
    num_cities = len(gallons)
    tank = 0
    for i in range(num_cities):
        city = (result + i) % num_cities
        tank += gallons[city] * MPG - distances[city]
        if tank < 0:
            raise TestFailure('Out of gas on city {}'.format(i))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('refueling_schedule.py',
                                       'refueling_schedule.tsv',
                                       find_ample_city_wrapper))
