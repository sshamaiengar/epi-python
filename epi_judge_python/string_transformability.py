from typing import Set

import string

from test_framework import generic_test

"""

Given strings a and b, and dictionary (set) of words
Determine if a can be transformed into b through words in the dictionary differing by one letter (same length) ateach step
Output shortest number of steps, or -1 if not possible

All words are lowercase alphabet

Ex. cat, dog {bat, cot, dog, dag, dot, cat}
cat
cot
dot
dog

BFS:
Verts are words
Edges are between words that have one letter different

Runtime O(V + E)
    O(E) ~ O(V^2), so can take O(V^2) to generate edges
    Need to go through O(k) letters in each string to test for edges
    O(26k * m) = Generate all one-letter changes, then check in set
    O(n^2 * m) = Check all pairs of dict words for one-letter difference

"""

def nbrs(s: str):
    alpha = string.ascii_lowercase
    nbrs = []
    chars = list(s)
    for i, a in enumerate(chars):
        for c in alpha:
            if a == c:
                continue
            new_chars = chars[:]
            new_chars[i] = c
            nbrs.append("".join(new_chars))
    return nbrs

def transform_string(D: Set[str], s: str, t: str) -> int:

    # build graph
    graph = {}
    for w in D:
        if w not in graph:
            graph[w] = []
        w_nbrs = nbrs(w)
        for v in w_nbrs:
            if v in D:
                graph[w].append(v)

    # BFS
    D.remove(s)
    q = [(s,0)]
    while q:
        curr, step = q.pop()
        curr_nbrs = graph[curr]
        for n in curr_nbrs:
            if n in D:
                q.insert(0,(n, step + 1))
                D.remove(n)
                if n == t:
                    return step + 1
    return -1

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_transformability.py',
                                       'string_transformability.tsv',
                                       transform_string))
