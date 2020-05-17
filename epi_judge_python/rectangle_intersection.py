import collections

from test_framework import generic_test
from test_framework.test_failure import PropertyName

Rect = collections.namedtuple('Rect', ('x', 'y', 'width', 'height'))

"""

Hint: think of each axis independently
Must intersect on both axes for rectangles to intersect

Rect A is one with most bottom-left corner.
Rect B is other one.
Intersect if bottom-left B x and y <= top-right A x and y

Runtime: O(1) for 2 rectangles (comparing coordinates, sorting 4 points)

"""

def intersect_rectangle(r1: Rect, r2: Rect) -> Rect:
    # intersection conditions
    x_intersect = False
    y_intersect = False
    if r1.x <= r2.x:
        if r2.x <= r1.x + r1.width:
            x_intersect = True
    else:
        if r1.x <= r2.x + r2.width:
            x_intersect = True

    if r1.y <= r2.y:
        if r2.y <= r1.y + r1.height:
            y_intersect = True
    else:
        if r1.y <= r2.y + r2.height:
            y_intersect = True


    intersect = Rect(0,0,-1,-1)
    if x_intersect and y_intersect:
        # intersection coords are two midpoints of all vertices along each axis
        # x_verts = sorted([r1.x, r1.x + r1.width, r2.x, r2.x + r2.width])
        # y_verts = sorted([r1.y, r1.y + r1.height, r2.y, r2.y + r2.height])
        # intersect = Rect(x=x_verts[1], y=y_verts[1], width=x_verts[2] - x_verts[1], height=y_verts[2] - y_verts[1])

        # can simplify based on intersection conditions
        intersect = Rect(x=max(r1.x, r2.x),
                y=max(r1.y, r2.y),
                width=min(r1.x + r1.width, r2.x + r2.width) - max(r1.x, r2.x),
                height=min(r1.y + r1.height, r2.y + r2.height) - max(r1.y, r2.y))


    return intersect


def intersect_rectangle_wrapper(r1, r2):
    return intersect_rectangle(Rect(*r1), Rect(*r2))


def res_printer(prop, value):
    def fmt(x):
        return [x[0], x[1], x[2], x[3]] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('rectangle_intersection.py',
                                       'rectangle_intersection.tsv',
                                       intersect_rectangle_wrapper,
                                       res_printer=res_printer))
