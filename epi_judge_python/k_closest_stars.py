import functools
import math
from typing import Iterator, List
import heapq

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

"""

Stars are points in 3D space with Earth as origin.
Total 10^12 stars.
Compute k closest stars to Earth, given stars in file/

Brute force:
Sort all stars by distance. Return k closest.
Time O(n log n), space O(n) (to get stars in memory)

Heap:
We CAN'T fit all the stars coordinates into RAM so...
We only care about stars closest to Earth.
To track candidates for this, need to know about the furthest current candidate.
If new star is closer, remove the furthest as a candidate.
Else, ignore new star.

Use max heap of size k, keyed by distance.
Pop max star if next star is closer.
In the end, the heap will contain k closest.
Time (n log n), space O(k)


"""


class Star:
    def __init__(self, x: float, y: float, z: float) -> None:
        self.x, self.y, self.z = x, y, z

    @property
    def distance(self) -> float:
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __lt__(self, rhs: 'Star') -> bool:
        return self.distance < rhs.distance

    def __repr__(self):
        return str(self.distance)

    def __str__(self):
        return self.__repr__()

    def __eq__(self, rhs):
        return math.isclose(self.distance, rhs.distance)


def find_closest_k_stars(stars: Iterator[Star], k: int) -> List[Star]:
    hp = []
    for i in range(k):
        s = next(stars)
        d = s.distance
        heapq.heappush(hp, (-d, s)) # negative key for max heap

    for s in stars:
        d = s.distance
        furthest = hp[0]
        if d < abs(hp[0][0]):
            heapq.heappushpop(hp, (-d, s))
    return list(sorted(s for _, s in hp))


def comp(expected_output, output):
    if len(output) != len(expected_output):
        return False
    return all(
        math.isclose(s.distance, d)
        for s, d in zip(sorted(output), expected_output))


@enable_executor_hook
def find_closest_k_stars_wrapper(executor, stars, k):
    stars = [Star(*a) for a in stars]
    return executor.run(functools.partial(find_closest_k_stars, iter(stars),
                                          k))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('k_closest_stars.py',
                                       'k_closest_stars.tsv',
                                       find_closest_k_stars_wrapper, comp))
