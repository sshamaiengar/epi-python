import collections
import functools
from typing import List
from functools import reduce

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


"""

Given a set of events as time intervals, determine the max number of events that take place concurrently
Hint: focus on endpoints

*Event time intervals are inclusive

Brute force:
For each event, loop through remaining events to count total concurring
O(n^2)

Better:
Keep count with endpoints as keys -> O(2n) space
For each event, increment counter for its endpoint (and endpoints in between?)
Return max counter
O(n)? time, O(n) space


Sorting:
Sort events by (start/end?) time -> O(n log n)
    Starting? All concurring event sets must include one that occurs earliest
For each sorted event:
    Go through next events, counting how many are concurring

Only care about endpoints
    Endpoints are where the concurrence starts/stops

That one interval problem?
Remove intervals that overlap with current interval (count how many)
Repeat through rest of intervals
Would this be correct?
    NO, removing some intervals would miss the right answer

Book solution:
Endpoints need not be tied to the event.
    If 3 events have started and only 2 have ended, we know there is 1 event going on
Sort all endpoints (not as events), but maintain start/end designation
Go through these with a counter
    Start -> +1 (one more event is occurring now)
    End -> -1 (one less event is concurring now)
O(n log n) time, O(n)? space


"""


# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))


def find_max_simultaneous_events(A: List[Event]) -> int:
    start_pts = [(e.start, True) for e in A]
    finish_pts = [(e.finish, False) for e in A]
    # sort endpts first by time, then start earlier than end
    endpts = sorted(start_pts + finish_pts, key=lambda e: (e[0], ~e[1]))
    cnt = 0
    max_cnt = 0
    for e in endpts:
        _, is_start = e
        if is_start:
            cnt = cnt + 1
            max_cnt = max(max_cnt, cnt)
        else:
            cnt = cnt - 1
    return max_cnt


@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(functools.partial(find_max_simultaneous_events,
                                          events))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('calendar_rendering.py',
                                       'calendar_rendering.tsv',
                                       find_max_simultaneous_events_wrapper))
