#!/usr/bin/env python

import fileinput
from pprint import pprint, pformat


def arrayManipulation(n, queries):
    # queries is list of lists
    # pprint(n)
    # pprint(queries)

    arr = [0] * n

    for q in queries:
        a = q[0] - 1
        b = q[1] - 1
        k = q[2]

        arr[a] += k
        if b < len(arr) - 1:
            arr[b + 1] -= k

    m = 0
    s = 0
    for i in arr:
        s += i
        m = max(s, m)

    return m


if __name__ == '__main__':
    fi = fileinput.FileInput()
    nelements, nqueries = map(int, fi.readline().split(' '))
    queries = []
    for _ in xrange(nqueries):
        queries.append(map(int, fi.readline().split(' ')))

    result = arrayManipulation(nelements, queries)

    print result
